#!/usr/bin/env python3
"""Universal AI Skill Router - command resolver.

Usage:
  python3 scripts/lookup.py "<full user input>"      -> JSON describing how the input resolves
  python3 scripts/lookup.py --search <keyword>       -> commands whose name/definition contains keyword
  python3 scripts/lookup.py --list [category|id]     -> list categories, or one category's commands
Pure standard library. Reads ../references/command-registry.json.
On Windows, use `python` instead of `python3`.
"""
import json, os, re, sys, difflib

HERE = os.path.dirname(os.path.abspath(__file__))
REG = json.load(open(os.path.join(HERE, '..', 'references', 'command-registry.json'), encoding='utf-8'))
CMDS = REG['commands']
BY_KEY = {c['key']: c for c in CMDS}
META = {'help', 'list', 'search'}            # router utilities, not library commands
SKILL_RE = re.compile(r'^\s*/?universal[-_ ]ai[-_ ]skill[-_ ]router\b', re.I)
TOKEN_CHARS = r'[A-Za-z0-9_\-]+'
TOK = re.compile(r'[ \t]*(/?)(' + TOKEN_CHARS + r')(?![A-Za-z0-9_\-/.])')
SLASH_TOK_AHEAD = re.compile(r'[ \t]+(?=/' + TOKEN_CHARS + r'(?![A-Za-z0-9_\-/.]))')
PLUS = re.compile(r'[ \t]*\+[ \t]*')
CONFLICTS = [  # pairs of keys that pull in opposite directions (advisory only)
    ('concise', 'deepdive'), ('concise', 'expand'), ('concise', 'walkthrough'), ('brief', 'deepdive'),
    ('eli5', 'expert'), ('eli5', 'technical'), ('eli5', 'advanced'), ('beginner', 'advanced'),
    ('formal', 'casual'), ('casual', 'professional'), ('shorten', 'expand'), ('tldr', 'deepdive'),
    ('finalanswer', 'stepbystep'), ('finalanswer', 'thinking'), ('nofluff', 'expand'), ('minimal', 'premium'),
]

def norm(s):
    return re.sub(r'[^a-z0-9]', '', s.lower())

def info(c):
    return {k: c[k] for k in ('name', 'description', 'section_id', 'section', 'subsection', 'file', 'detailed_definition')}

def suggest(key, n=3):
    out = difflib.get_close_matches(key, list(BY_KEY), n=n, cutoff=0.6)
    for k in BY_KEY:                       # substring hints (e.g. 'hooks' -> hook, hook10)
        if len(key) >= 4 and (key in k or k in key) and k not in out and len(out) < n + 2:
            out.append(k)
    return [BY_KEY[k]['name'] for k in out[:n]]

def read_chain(t, has_skill):
    """Return (list of (raw_token, had_slash)), remaining_text)."""
    toks, pos = [], 0
    m = TOK.match(t, pos)
    if not m or (not has_skill and not m.group(1)):
        return [], t
    toks.append((m.group(2), bool(m.group(1)))); pos = m.end()
    while True:
        pm = PLUS.match(t, pos)
        if pm:
            m = TOK.match(t, pm.end())
            if m and (m.group(1) or norm(m.group(2)) in BY_KEY):
                toks.append((m.group(2), bool(m.group(1)))); pos = m.end(); continue
            break
        sm = SLASH_TOK_AHEAD.match(t, pos)
        if sm:
            m = TOK.match(t, sm.end())
            toks.append((m.group(2), True)); pos = m.end(); continue
        break
    return toks, t[pos:]

def parse(text):
    t = text.strip()
    has_skill = False
    sm = SKILL_RE.match(t)
    if sm:
        has_skill, t = True, t[sm.end():].strip()
    result = {'mode': 'conversation', 'has_skill_prefix': has_skill, 'commands': [], 'unknown': [],
              'task': text.strip() if not has_skill else t, 'missing_task': False, 'possible_conflicts': [],
              'files_to_read': [], 'notes': []}
    if has_skill:
        first = TOK.match(t)
        if first and not first.group(1) and norm(first.group(2)) in META and norm(first.group(2)) not in BY_KEY:
            result.update(mode='meta', action=norm(first.group(2)), args=t[first.end():].strip(), task='')
            result['files_to_read'] = ['references/router-protocol.md']
            return result
        if not first:
            result.update(mode='meta', action='help', args='', task='')
            result['notes'].append('skill name given with no command: show help')
            return result
    toks, rest = read_chain(t, has_skill)
    if not toks:
        return result                       # normal conversation
    result['mode'] = 'command'
    seen = set()
    for raw, _ in toks:
        k = norm(raw)
        if k in seen:
            result['notes'].append(f'duplicate command ignored: {raw}'); continue
        seen.add(k)
        if k in BY_KEY:
            result['commands'].append(info(BY_KEY[k]))
        else:
            sug = suggest(k)
            auto = None
            best = difflib.get_close_matches(k, list(BY_KEY), n=2, cutoff=0.88)
            if len(k) >= 6 and best and (len(best) == 1 or
               difflib.SequenceMatcher(None, k, best[0]).ratio() - difflib.SequenceMatcher(None, k, best[1]).ratio() > 0.05):
                auto = BY_KEY[best[0]]['name']
                result['commands'].append(dict(info(BY_KEY[best[0]]), interpreted_from='/' + raw))
            result['unknown'].append({'token': '/' + raw.lstrip('/'), 'suggestions': sug, 'auto_interpreted_as': auto})
    result['task'] = rest.strip()
    result['missing_task'] = result['task'] == ''
    keys = {norm(c['name']) for c in result['commands']}
    result['possible_conflicts'] = [[BY_KEY[a]['name'], BY_KEY[b]['name']] for a, b in CONFLICTS if a in keys and b in keys]
    files = sorted({c['file'] for c in result['commands']})
    extra = []
    if any(c['detailed_definition'] for c in result['commands']) or len(result['commands']) > 1:
        extra.append('references/detailed-definitions-and-examples.md')
    if result['unknown'] or result['missing_task'] or result['possible_conflicts']:
        extra.append('references/router-protocol.md')
    result['files_to_read'] = files + extra
    return result

def search(kw):
    k = kw.lower()
    return [info(c) for c in CMDS if k in c['name'].lower() or k in c['description'].lower()]

def list_cmds(arg=''):
    arg = arg.strip().lower()
    if not arg:
        return [{'id': s['id'], 'title': s['title'], 'count': s['count'], 'file': s['file']} for s in REG['sections']]
    for s in REG['sections']:
        if arg == s['id'] or arg in s['title'].lower():
            return [info(c) for c in CMDS if c['section_id'] == s['id']]
    if arg == '7':
        return [info(c) for c in CMDS if c['section_id'].startswith('7')]
    return search(arg)

if __name__ == '__main__':
    a = sys.argv[1:]
    if not a:
        print(__doc__); sys.exit(1)
    if a[0] == '--search': out = search(' '.join(a[1:]))
    elif a[0] == '--list': out = list_cmds(' '.join(a[1:]))
    else: out = parse(' '.join(a))
    print(json.dumps(out, ensure_ascii=False, indent=2))
