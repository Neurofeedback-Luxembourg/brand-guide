<!-- brand-kit VERSION 2.1.5 -->
# Hermes install (loaders, not copies)

`nfl-brand/` and `nfl-brand-review/` are loader skills: they read the live kit from GitHub at use time; `nfl-brand` also states the standing drafting instructions. Brand Guide v2.1.3 (approved 2 October 2026) is the only rulebook; §11 states visual identity, voice and languages. They are what every Hermes host installs (via `francois352/hermes-config` `shared/skills/`). Loaders survive hermes-sync on Linux and Windows (no symlinks). The monthly drift check (`tests/drift_check.py`) confirms the installed `nfl-brand` is this loader.
