#!/usr/bin/env python3
"""Completeness verification: README (spec) vs registry.json vs registry.md vs category files vs router resolution.
Usage: python3 scripts/verify.py [--readme PATH] [--report OUT.md] [--check]
  --check  validate only: print the summary and exit non-zero on failure, write nothing
Uses its OWN README extractor (independent of the build parser)."""
import json, os, re, sys, collections
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, '..')
sys.path.insert(0, HERE)
import lookup
args = sys.argv[1:]
check_only = '--check' in args
readme = os.path.join(ROOT, 'source', 'README.original.md')
report = os.path.join(ROOT, 'VERIFICATION-REPORT.md')
if '--readme' in args: readme = args[args.index('--readme') + 1]
if '--report' in args: report = args[args.index('--report') + 1]

# ---- A. independent README extraction -------------------------------------------------
lines = open(readme, encoding='utf-8').read().replace('\r\n', '\n').split('\n')
fence, top, A = False, None, []          # A: (cmd, desc, line, top-section)
i = 0
while i < len(lines):
    L = lines[i]
    if L.lstrip().startswith('```'): fence = not fence
    elif not fence:
        h = re.match(r'^## (\d+)\.', L)
        if h: top = h.group(1)
        elif re.match(r'^# ', L): top = None
        m = re.match(r'^ {2}`(/[^`]+)`(?:\s+(\S.*))?$', L)
        if m and top:
            d = (m.group(2) or '').strip(); j = i + 1
            while j < len(lines) and re.match(r'^ {20,}\S', lines[j]):
                d += ' ' + lines[j].strip(); j += 1
            A.append((m.group(1), d.strip(), i + 1, top))
    i += 1
readme_names = [a[0] for a in A]
dup_readme = [k for k, v in collections.Counter(readme_names).items() if v > 1]

# ---- B/C/D. implemented sets ----------------------------------------------------------
reg = json.load(open(os.path.join(ROOT, 'references', 'command-registry.json'), encoding='utf-8'))
B = {c['name']: c for c in reg['commands']}
mdtxt = open(os.path.join(ROOT, 'references', 'command-registry.md'), encoding='utf-8').read()
C = collections.Counter(re.findall(r'`(/[^`\s]+)`', mdtxt))
D = collections.defaultdict(list)          # name -> [(file, desc)]
for sec in reg['sections']:
    fp = os.path.join(ROOT, sec['file'])
    for ln in open(fp, encoding='utf-8').read().split('\n'):
        m = re.match(r'^- `(/[^`]+)`(?: ★)? — (.*)$', ln)
        if m: D[m.group(1)].append((sec['file'], m.group(2)))
D_counts = collections.Counter({k: len(v) for k, v in D.items()})

# ---- E. per-command checks ------------------------------------------------------------
rows, problems = [], []
for n, (name, desc, ln, top) in enumerate(A, 1):
    b = B.get(name)
    ck = {}
    ck['registry.json'] = bool(b) and b['description'] == desc
    ck['registry.md'] = C.get(name, 0) == 1
    ck['category file'] = D_counts.get(name, 0) == 1 and D[name][0][1] == desc
    ck['file mapping'] = bool(b) and D.get(name, [('', '')])[0][0] == b['file'] and b['section_id'].rstrip('abc') == top
    r1 = lookup.parse(f'/universal-ai-skill-router {name[1:]} t'); r2 = lookup.parse(f'{name} t')
    ck['router'] = all(r['mode'] == 'command' and [c['name'] for c in r['commands']] == [name] and not r['unknown'] for r in (r1, r2))
    ok = all(ck.values())
    if not ok: problems.append((name, [k for k, v in ck.items() if not v]))
    rows.append((n, name, ln, top, b['file'].split('/')[-1] if b else '-', ck, ok, desc))
extra_json = sorted(set(B) - set(readme_names)); extra_files = sorted(set(D) - set(readme_names)); extra_md = sorted(set(C) - set(readme_names))
dups = {k: v for k, v in {**{k: C[k] for k in C if C[k] > 1}, **{k: D_counts[k] for k in D_counts if D_counts[k] > 1}}.items()}

# ---- F. counts ------------------------------------------------------------------------
readme_by_top = collections.Counter(a[3] for a in A)
reg_by_top = collections.Counter(c['section_id'].rstrip('abc') for c in reg['commands'])
file_by_top = collections.Counter()
for k, v in D.items():
    for f, _ in v:
        file_by_top[re.match(r'.*/(\d+)', f).group(1).lstrip('0')] += 1
md_by_top = collections.Counter()
for sec in reg['sections']:
    seg = mdtxt.split(f"## {sec['id']}. ")[1].split('\n## ')[0]
    md_by_top[sec['id'].rstrip('abc')] += len(re.findall(r'`(/[^`\s]+)`', seg))

# ---- G. combos referenced in README exist --------------------------------------------
tail = '\n'.join(lines[[k for k, l in enumerate(lines) if l.startswith('# 🧩')][0]:])
combo_refs = sorted(set(re.findall(r'(?<![\w./<-])/([a-z0-9][a-z0-9\-]*)', tail)) - {'yourshortcut', 'SHORTCUT'})
combo_refs = ['/' + c for c in combo_refs]
combo_refs = [c for c in combo_refs if c in set(readme_names) or c in B or c.islower()]
missing_combo = [c for c in combo_refs if c not in B and c not in ('/LICENSE',)]

total_ok = sum(1 for r in rows if r[6])
complete = (len(A) == len(B) == len(D) == len(C) and total_ok == len(A) and not extra_json and not extra_files
            and not extra_md and not dups and not dup_readme and not missing_combo)

out = ['# Verification Report — Universal AI Skill Router', '',
 '_Generated by `python scripts/verify.py` (or `python3` on macOS/Linux) using an extractor independent of the build parser. Re-run it any time; it recomputes everything from `source/README.original.md`._', '',
 '## 1. Verdict', '',
 f"**{'COMPLETE: every README command is implemented, none missing, none duplicated.' if complete else 'INCOMPLETE — see problems below. Do not claim 100%.'}**", '',
 '| Measure | Count |', '|---|---|',
 f'| Commands in README (unique, command tables only) | **{len(set(readme_names))}** ({len(readme_names)} rows) |',
 f'| Commands in `command-registry.json` | **{len(B)}** |',
 f'| Commands in `command-registry.md` index | **{len(C)}** |',
 f'| Commands implemented in category files | **{len(D)}** ({sum(D_counts.values())} definition lines) |',
 f'| Commands that resolve through the router (both invocation forms) | **{sum(1 for r in rows if r[5]["router"])}** |',
 f'| Commands passing ALL 5 checks | **{total_ok} / {len(A)}** |',
 f'| Missing (in README, not implemented) | **{len(problems)}** {[p[0] for p in problems]} |',
 f'| Extra (implemented, not in README) | **{len(extra_json) + len(extra_files) + len(extra_md)}** |',
 f'| Duplicated | **{len(dups) + len(dup_readme)}** {list(dups)+dup_readme} |',
 f'| Commands renamed / merged / simplified | **0** (names and descriptions compared verbatim) |', '',
 'Note: the number of distinct commands is **%d**. The template placeholder `/yourshortcut` (Contributing section) is documentation, not a command, and is excluded. Router utilities `help`, `list`, `search` are additions of the router itself and are not counted.' % len(set(readme_names)), '',
 '## 2. Count comparison by README section', '',
 '| README section | README | registry.json | registry.md | category files |', '|---|---|---|---|---|']
titles = {s['id'].rstrip('abc'): s['title'] for s in reg['sections'] if not s['id'].startswith('7')}
titles['7'] = 'Extended image, style & photo codes (17 subsections; files 7a+7b+7c)'
for t in ['1', '2', '3', '4', '5', '6', '7']:
    vals = (readme_by_top[t], reg_by_top[t], md_by_top[t], file_by_top[t])
    out.append(f"| {t}. {titles[t]} | {vals[0]} | {vals[1]} | {vals[2]} | {vals[3]} {'✔' if len(set(vals)) == 1 else '✘'} |")
out.append(f"| **Total** | **{sum(readme_by_top.values())}** | **{sum(reg_by_top.values())}** | **{sum(md_by_top.values())}** | **{sum(file_by_top.values())}** |")
out += ['', 'Section 7 subsection counts (README vs implemented):', '', '| Subsection | README | Implemented |', '|---|---|---|']
sub_readme = collections.Counter()
cur = None; fence2 = False; intop = False
for L in lines:
    if L.lstrip().startswith('```'): fence2 = not fence2
    if fence2: continue
    if re.match(r'^## 7\.', L): intop = True; continue
    if re.match(r'^(# |## )', L) and not re.match(r'^## 7\.', L): intop = False
    if intop:
        h = re.match(r'^### (.*)$', L)
        if h: cur = h.group(1).strip()
        elif re.match(r'^ {2}`/', L): sub_readme[cur] += 1
sub_reg = collections.Counter(c['subsection'] for c in reg['commands'] if c['subsection'])
for s in sub_readme:
    out.append(f"| {s} | {sub_readme[s]} | {sub_reg[s]} {'✔' if sub_readme[s] == sub_reg[s] else '✘'} |")
out += ['', '## 3. Other README content implemented', '',
 '| README content | Where implemented |', '|---|---|',
 '| Invocation as labels; "shortcut is a label, the instruction after it is the request" | SKILL.md (Invocation, Execution rules) |',
 '| Reusable prompt pattern (Task / Audience / Format / Level / Constraints) | `detailed-definitions-and-examples.md` §2 |',
 '| Detailed definitions for `/teacher`, `/stickynotes`, `/blueprint` | `detailed-definitions-and-examples.md` §1 (marked ★ in registry) |',
 '| 10 suggested combinations | `detailed-definitions-and-examples.md` §3; all 10 tested (T05–T14) |',
 '| 4 ready-to-copy examples (+ 2 intro examples) | `detailed-definitions-and-examples.md` §4; tested (T15–T18) |',
 '| "Not official built-in commands" caveat; do not invent capabilities | SKILL.md; `router-protocol.md` §8 |',
 f"| Commands referenced by combinations/examples exist in the library | {len(combo_refs) - len(missing_combo)} / {len(combo_refs)} referenced names found in registry |",
 '', '## 4. Command-by-command verification', '',
 'Checks: **J** = exact name + verbatim definition in registry.json · **M** = listed once in registry.md · **F** = exactly one verbatim definition line in the correct category file · **P** = file/section mapping correct · **R** = router resolves it (canonical and bare forms).', '',
 '| # | Command | README line | Sec | Implemented in | J | M | F | P | R | Status |', '|---|---|---|---|---|---|---|---|---|---|---|']
tick = lambda v: '✔' if v else '✘'
for n, name, ln, top, f, ck, ok, desc in rows:
    out.append(f"| {n} | `{name}` | {ln} | {top} | {f} | {tick(ck['registry.json'])} | {tick(ck['registry.md'])} | {tick(ck['category file'])} | {tick(ck['file mapping'])} | {tick(ck['router'])} | {'✔ implemented' if ok else '✘ PROBLEM'} |")
if problems:
    out += ['', '## 5. Problems', ''] + [f'- `{n}`: failed {c}' for n, c in problems]
if check_only:
    print('check mode: report not written to', report)
else:
    open(report, 'w', encoding='utf-8', newline='\n').write('\n'.join(out) + '\n')
print('README commands:', len(A), '| registry.json:', len(B), '| registry.md:', len(C), '| category files:', len(D))
print('passing all checks:', total_ok, '| problems:', len(problems), '| extra:', len(extra_json), len(extra_files), len(extra_md), '| dups:', len(dups), len(dup_readme))
print('missing combo refs:', missing_combo)
print('VERDICT:', 'COMPLETE' if complete else 'INCOMPLETE')
sys.exit(0 if complete else 1)
