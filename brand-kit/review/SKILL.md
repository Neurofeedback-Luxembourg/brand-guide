---
name: nfl-brand-review
description: Brand review gate for Neurofeedback Luxembourg, recoveriX Luxembourg and Brain-Curator. Use BEFORE anything is published (post, page, email, ad, image, slide) and for the monthly brand drift check. Needs the nfl-brand skill.
---
<!-- brand-kit VERSION 2.1.4 -->
# nfl-brand-review

Source: GitHub Neurofeedback-Luxembourg/brand-guide → `brand-kit/` (read `brand-kit/VERSION` first). Rules: the `nfl-brand` skill. Checklist: `brand-kit/tests/tests.json`.

## Job A — review before publishing
1. Confirm the loaded `nfl-brand` skill version equals `brand-kit/VERSION`. If not: stop, report drift, do not approve.
2. Check the piece against every test in `tests.json` that applies (figures → test 2 and `figures.md`; health content → disclaimer; recoveriX → test 7; visuals → tests 9–10; offers → 5, 6, 11; claims → 12).
3. Every number must be in the statistics data file (`figures.md`) or its primary source, with source and year.
4. Reply: **APPROVE** or **CHANGES NEEDED**, then one line per problem: test id, the exact words quoted, the fix. Never approve with an open problem. Never publish yourself unless the task says so.

## Job B — monthly drift check (Telegram, Marketing topic)
1. `git -C <brand-guide clone> pull --ff-only`, then `python3 brand-kit/tests/drift_check.py`.
2. Answer each test with `"automatable": true` yourself, in a fresh context, then score each answer against its `pass` and `fail_signals` (rules in `tests/README.md`).
3. Post one message: kit VERSION; per agent OK/DRIFT; per test PASS/FAIL with the failing quote; what François must do (for MANUAL rows: "run test 1 in a new claude.ai chat and a new ChatGPT chat").
