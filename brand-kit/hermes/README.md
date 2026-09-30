<!-- brand-kit VERSION 2.1.4 -->
# Hermes install (loaders, not copies)

`nfl-brand/` and `nfl-brand-review/` are loader skills: they hold no rules and read the live kit from GitHub at use time. They are what every Hermes host installs (via `francois352/hermes-config` `shared/skills/`). Loaders survive hermes-sync on Linux and Windows (no symlinks). The monthly drift check (`tests/drift_check.py`) confirms the installed `nfl-brand` is this loader.
