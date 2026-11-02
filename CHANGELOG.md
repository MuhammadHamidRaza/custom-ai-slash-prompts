# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- "How to use these commands: ChatGPT vs Claude" section in `README.md`,
  explaining that shortcuts work directly in ChatGPT with no installation,
  while Claude requires uploading and enabling `universal-ai-skill-router.zip`.
- OpenCode installation instructions alongside Claude.ai, Claude Code, and the
  Skills API.
- Repository community files: `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`,
  `SECURITY.md`, issue templates, pull request template, and CI verification.
- Ready-to-upload `universal-ai-skill-router.zip` skill package.

### Changed

- Documentation now uses portable Python commands (`python` on Windows,
  `python3` on macOS/Linux).
- The README title and badges show the exact command count (763).
- `verify.py` gained a `--check` mode for CI that validates without rewriting
  `VERIFICATION-REPORT.md`.

### Fixed

- Missing `LICENSE` file referenced by the README badge.
- Missing skill ZIP referenced by `INSTALL.md`.

## [1.0.0] - 2026-11-02

### Added

- Complete slash-prompt library with **763** unique commands across nine
  categories.
- Extended image, style, and photo codes covering technical views, photography,
  3D rendering, materials, places, animals, UI, and branding.
- Universal AI Skill Router package:
  - `SKILL.md` router with canonical and README-native invocation forms.
  - `references/command-registry.json` and `command-registry.md` indexes.
  - Nine verbatim category files.
  - `references/detailed-definitions-and-examples.md` with the reusable prompt
    pattern, ten combinations, and ready-to-copy examples.
  - `references/router-protocol.md` for unknown commands, missing tasks,
    conflicting combinations, and router utilities.
- Python utilities: `lookup.py`, `verify.py`, and `run_tests.py`.
- Verification suite: 45 hand-written routing cases plus 3,815 generated cases
  (763 commands × 5 invocation forms), all passing.
- Command-by-command `VERIFICATION-REPORT.md`.

### Changed

- Contributing and support sections rewritten with open-source guidance for
  issues, pull requests, and starring the repository.

[Unreleased]: https://github.com/MuhammadHamidRaza/custom-chatgpt-slash-prompts/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/MuhammadHamidRaza/custom-chatgpt-slash-prompts/releases/tag/v1.0.0
