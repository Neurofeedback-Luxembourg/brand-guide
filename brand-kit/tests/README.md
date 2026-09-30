<!-- brand-kit VERSION 2.1.4 -->
# Brand tests — how any agent is scored

`tests.json` holds the 12 brand tests (from the brand system check of 30 Sept 2026). Each has an `id`, the `prompt` to send, `pass` criteria (all must hold) and `fail_signals` (any one = fail).

## Running a test
1. Start a **new** chat/session of the agent with its normal brand setup (claude.ai skill, ChatGPT operator brief, `AGENTS.md` for Codex/agy, Hermes skill). An open chat keeps old rules.
2. Send the `prompt` exactly as written.
3. Score: **PASS** only if every `pass` item holds and no `fail_signal` appears. Otherwise **FAIL**, with the item that broke.
4. Visual tests (9, 10): open the output. Test 9 passes only with light mode, the plum-deep→slate gradient with white text, Source Sans 3 and a real logo file from `logos/`.

## Which tests, when
- **After any kit change:** tests 1, 3 and 9 on every agent (maintenance order: Google Doc → rebuild kit → François replaces one file in the claude.ai brand project → re-run 1, 3, 9).
- **Monthly (Hermes):** `drift_check.py` for versions, then every test marked `"automatable": true` on Hermes itself, scored by the rules above; report to Telegram, Marketing topic.
- **Before publishing anything:** the reviewing agent checks the piece against every test that applies (see the `nfl-brand-review` skill in `review/`).

Record a result as: agent · date · kit VERSION · test id · PASS/FAIL · the failing item (quote).
