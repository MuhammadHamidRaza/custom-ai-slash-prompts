# Security Policy

## Supported versions

This project is documentation and a prompt router. It does not ship a compiled
binary or run a hosted service. Security fixes are applied to the latest version
on the `main` branch and to the latest published skill package.

| Version | Supported |
|---|---|
| Latest `main` / latest release | ✅ |
| Older releases | ❌ |

## Reporting a vulnerability

**Please do not open a public issue, pull request, or discussion for a security
problem.**

Report it privately to **hr1907469@gmail.com** with:

- A short description of the issue and its impact.
- Steps to reproduce, including the exact command or file involved.
- Any relevant output, logs, or proof of concept.
- Your preferred name and contact for credit (optional).

You can expect an acknowledgement within **72 hours** and a status update within
**7 days**. If the report is valid, a fix will be prepared and released as soon
as reasonably possible, and you will be credited unless you ask to remain
anonymous.

## Scope

This project includes Python scripts and a skill package that read local files.
In scope:

- Code execution or command injection through `scripts/lookup.py`,
  `scripts/verify.py`, or `scripts/run_tests.py`.
- Path traversal or unintended file writes caused by the scripts.
- Secrets, credentials, or personal data committed to the repository.
- Prompt-injection instructions hidden in command definitions that could cause
  an assistant to ignore safety rules.
- Malicious or misleading links in the documentation.

Out of scope:

- The behavior of third-party products (ChatGPT, Claude, OpenCode, or their
  APIs).
- The quality or factual accuracy of a community prompt definition; report those
  as a normal bug.
- Social engineering or attacks that require physical access to a user's device.

## Safe design

- The scripts use only the Python standard library.
- They make no network requests.
- They read local JSON/Markdown and write only `VERIFICATION-REPORT.md` (and,
  when asked, `tests/test-results.txt`).
- No secrets, tokens, or credentials belong in this repository. If you find
  one, report it privately.

## Preferred languages

English.
