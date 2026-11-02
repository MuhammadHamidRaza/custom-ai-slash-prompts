#!/usr/bin/env python3
"""Runs every parse-level test: hand-written cases + registry-wide auto cases. Exit code 1 on any failure.
Usage: python3 scripts/run_tests.py [--write]   (--write saves tests/test-results.txt)
On Windows, use `python` instead of `python3`."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import lookup
ROOT = os.path.join(HERE, '..')
cases = json.load(open(os.path.join(ROOT, 'tests', 'test-cases.json'), encoding='utf-8'))
out, fails, n = [], 0, 0
def check(name, ok, detail=''):
    global fails, n
    n += 1
    if not ok:
        fails += 1; out.append(f'FAIL {name} {detail}')
# 1. hand-written cases
for c in cases:
    r = lookup.parse(c['input']); e = c['expect']
    ok = r['mode'] == e['mode']
    if 'commands' in e:
        got = [x['name'] for x in r['commands']]
        ok &= got == e['commands']
    if 'unknown' in e: ok &= [u['token'] for u in r['unknown']] == e['unknown']
    if 'task' in e: ok &= r['task'] == e['task']
    if 'missing_task' in e: ok &= r['missing_task'] == e['missing_task']
    if 'action' in e: ok &= r.get('action') == e['action']
    if 'args' in e: ok &= r.get('args') == e['args']
    if e.get('conflicts'): ok &= bool(r['possible_conflicts'])
    check(c['id'], ok, json.dumps({'got': {k: r[k] for k in ('mode', 'task')}, 'cmds': [x['name'] for x in r['commands']]}))
hand = n
# 2. every registry command, four forms
for c in lookup.CMDS:
    nm = c['name']; bare = nm.lstrip('/')
    forms = {
        'canonical': f'/universal-ai-skill-router {bare} sample task',
        'bare-slash': f'{nm} sample task',
        'no-slash-after-skill': f'/universal-ai-skill-router {bare.upper()} sample task',
        'normalized': f'/universal-ai-skill-router {bare.replace("-", "_")} sample task',
    }
    for fname, f in forms.items():
        r = lookup.parse(f)
        ok = r['mode'] == 'command' and [x['name'] for x in r['commands']] == [nm] and r['task'] == 'sample task' \
             and r['commands'][0]['file'] == c['file'] and not r['unknown']
        check(f'{nm} [{fname}]', ok, f'got {[x["name"] for x in r["commands"]]} unknown={r["unknown"]}')
    r = lookup.parse(f'/universal-ai-skill-router {bare}')
    check(f'{nm} [missing-task]', r['missing_task'] is True)
auto = n - hand
summary = [f'hand-written cases: {hand}', f'registry-wide cases: {auto} ({len(lookup.CMDS)} commands x 5 forms)',
           f'total: {n}', f'failures: {fails}', 'RESULT: ' + ('ALL PASS' if fails == 0 else 'FAILURES PRESENT')]
text = '\n'.join(out + summary)
print(text)
if '--write' in sys.argv:
    open(os.path.join(ROOT, 'tests', 'test-results.txt'), 'w', encoding='utf-8', newline='\n').write(text + '\n')
sys.exit(1 if fails else 0)
