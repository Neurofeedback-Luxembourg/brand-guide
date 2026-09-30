# brand-kit VERSION 2.1.4
"""Monthly brand drift check: compare each agent's loaded/pinned brand version to brand-kit/VERSION.

  python3 brand-kit/tests/drift_check.py     prints one line per agent, exit 1 if any drift

Needs `gh` (authenticated) to read VERSION and the consumer repos' AGENTS.md pins.
Claude (claude.ai skill) and ChatGPT cannot be read from outside: they are listed as MANUAL
(run test 1 in a new chat). Stdlib only.
"""
import base64, json, os, re, subprocess, sys
from pathlib import Path

KIT_REPO = "Neurofeedback-Luxembourg/brand-guide"
# Repos that produce brand output; their AGENTS.md pins a kit VERSION (Codex + agy read it).
CONSUMERS = ["Neurofeedback-Luxembourg/nfl-web", "Neurofeedback-Luxembourg/brain-curator-site",
             "Neurofeedback-Luxembourg/neuroclaw-social-machine"]
PIN = re.compile(r"brand-kit VERSION (\d+\.\d+\.\d+)")
SKILL_V = re.compile(r"skill v(\d+\.\d+\.\d+)")


def gh_file(repo, path):
    r = subprocess.run(["gh", "api", f"repos/{repo}/contents/{path}"], capture_output=True, text=True)
    if r.returncode:
        raise RuntimeError(r.stderr.strip() or f"gh api failed for {repo}/{path}")
    return base64.b64decode(json.loads(r.stdout)["content"]).decode()


def main():
    try:
        want = gh_file(KIT_REPO, "brand-kit/VERSION").split()[0]
    except Exception as e:  # no VERSION = no check; say so loudly
        print(f"ERROR cannot read {KIT_REPO} brand-kit/VERSION: {e}")
        return 2
    rows = []
    for repo in CONSUMERS:
        try:
            m = PIN.search(gh_file(repo, "AGENTS.md"))
            rows.append((f"Codex/agy · {repo}", m.group(1) if m else "NO PIN"))
        except Exception as e:
            rows.append((f"Codex/agy · {repo}", f"ERROR {e}"))
    home = Path(os.environ.get("HERMES_HOME", Path.home() / ".hermes"))
    for name in ("nfl-brand", "nfl-brand-review"):
        skill = home / "skills" / name / "SKILL.md"
        try:
            text = skill.read_text()
            # The installed skill must be the loader (reads the live kit), never a copy of the rules.
            got = want if "(loader" in text and "raw.githubusercontent.com/Neurofeedback-Luxembourg/brand-guide" in text \
                else "COPY, not loader: " + (SKILL_V.search(text).group(1) if SKILL_V.search(text) else "old/unknown version")
            rows.append((f"Hermes · {skill}", got))
        except OSError as e:
            rows.append((f"Hermes · {skill}", f"ERROR {e}"))
    print(f"brand-kit VERSION on main: {want}")
    drift = 0
    for who, got in rows:
        ok = got == want
        drift |= not ok
        print(f"{'OK   ' if ok else 'DRIFT'} {who}: {got}")
    print("MANUAL Claude (claude.ai skill + brand project) and ChatGPT: run test 1 in a new chat; "
          f"expect Brand Guide v2.1.2 / kit {want}")
    return 1 if drift else 0


if __name__ == "__main__":
    sys.exit(main())
