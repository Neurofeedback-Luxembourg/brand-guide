# brand-kit VERSION 2.1.4
"""Build or check the brand kit. Stdlib only.

  python3 brand-kit/build.py            regenerate everything, stamp VERSION into every file
  python3 brand-kit/build.py --no-doc   same, without re-exporting the Google Doc (no gws needed)
  python3 brand-kit/build.py --check    CI: fail if any version header or generated file is out of date

Sources: Google Doc (brand-guide.md), guide/*.md (skill references), tokens/tokens.json
(copied from the Claude Design system), logos/, tests/tests.json, skill/SKILL.md rules.
"""
import hashlib, json, re, subprocess, sys, zipfile
from pathlib import Path

KIT = Path(__file__).resolve().parent
REPO = KIT.parent
DOC_ID = "1qGMKXauGHe_9CHvJ2JLYZNz4R92Uhn_68Hz7mImsq60"
VERSION = (KIT / "VERSION").read_text().split()[0]
TEXT = {".md", ".css", ".html", ".json", ".py", ".yml"}
HEADER = re.compile(r"brand-kit VERSION (\S+)")
JSON_HEADER = re.compile(r'"kit_version": "([^"]*)"')
LOGOS = ["logo-transparent.png", "logo-reversed-transparent.png", "logo-white.png", "logo-icon-transparent.png"]
GUIDE_REFS = ["brand-guide.md", "business-facts.md", "carried-from-brand-lock-v1.3.md"]


def text_files():
    files = [p for p in KIT.rglob("*") if p.is_file() and p.suffix in TEXT and "dist" not in p.parts]
    return files + [REPO / "AGENTS.md", REPO / ".github/workflows/brand-kit-version.yml"]


def stamp(text, path):
    """Return text with its version header set to VERSION (adds one if missing)."""
    if path.suffix == ".json":
        if JSON_HEADER.search(text):
            return JSON_HEADER.sub(f'"kit_version": "{VERSION}"', text, count=1)
        return re.sub(r"^\{", '{\n  "kit_version": "' + VERSION + '",', text, count=1)
    if HEADER.search(text):
        text = HEADER.sub(f"brand-kit VERSION {VERSION}", text, count=1)
    else:
        line = {".css": f"/* brand-kit VERSION {VERSION} */", ".py": f"# brand-kit VERSION {VERSION}",
                ".yml": f"# brand-kit VERSION {VERSION}"}.get(path.suffix, f"<!-- brand-kit VERSION {VERSION} -->")
        m = re.match(r"(---\n.*?\n---\n)", text, re.S)  # keep YAML frontmatter first (SKILL.md)
        text = m.group(1) + line + "\n" + text[m.end():] if m else line + "\n" + text
    if path.name == "SKILL.md":
        text = re.sub(r"skill v\d+\.\d+\.\d+", f"skill v{VERSION}", text)
    return text


def export_doc():
    out = KIT / "dist" / "doc.txt"
    out.parent.mkdir(exist_ok=True)
    params = json.dumps({"fileId": DOC_ID, "mimeType": "text/plain"})
    subprocess.run(["gws", "drive", "files", "export", "--params", params, "--output", str(out)], check=True,
                   stdout=subprocess.DEVNULL)
    meta = subprocess.run(["gws", "drive", "files", "get", "--params",
                           json.dumps({"fileId": DOC_ID, "fields": "name,modifiedTime,version"})],
                          check=True, capture_output=True, text=True).stdout
    meta = json.loads(meta[meta.index("{"):])
    body = out.read_text(encoding="utf-8-sig").replace("\r\n", "\n").strip() + "\n"
    return (f"<!-- brand-kit VERSION {VERSION} -->\n"
            f"<!-- GENERATED from Google Doc {DOC_ID} (\"{meta['name']}\", revision {meta['version']}, "
            f"modified {meta['modifiedTime']}) by brand-kit/build.py. DO NOT EDIT: change the Google Doc and rebuild. -->\n"
            f"<!-- https://docs.google.com/document/d/{DOC_ID}/edit -->\n\n" + body)


def tokens_block():
    t = json.loads((KIT / "tokens/tokens.json").read_text())
    val = lambda v: re.sub(r"\{([\w.-]+)\}", r"var(--nfl-\1)", v)
    lines = [f"  --nfl-{c['name']}: {val(c['value'])};" for c in t["color"]["tokens"]]
    lines.append("  --nfl-gradient: linear-gradient(135deg, var(--nfl-plum-deep), var(--nfl-slate)); /* always with white text */")
    lines.append(f"  --nfl-font: {t['type']['families']['sans']}; /* never Inter or Montserrat */")
    for g in t["type"]["groups"]:
        for s in g["styles"]:
            lines.append(f"  --nfl-text-{s['name']}: {s['fontWeight']} {s['fontSize']}/{s['lineHeight']} var(--nfl-font);")
    for fam in ("spacing", "radius", "shadow"):
        lines += [f"  --nfl-{x['name']}: {x['value']};" for x in t[fam]["tokens"]]
    lines.append("  --nfl-radius: var(--nfl-radius-lg); /* legacy name used by skill/assets/brand.css */")
    return ":root {\n" + "\n".join(lines) + "\n}\n"


FONT = "@import url('https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@400;600;700&display=swap');\n"


def generated():
    """Files whose whole content is derived from other kit files: {path: text}."""
    block = tokens_block()
    out = {KIT / "tokens/tokens.css": f"/* brand-kit VERSION {VERSION} */\n/* GENERATED from tokens/tokens.json "
           "(Claude Design system \"2026_09_Neurofeedback Luxembourg\", light mode only) by build.py. DO NOT EDIT. */\n"
           + FONT + block}
    css = (KIT / "skill/assets/brand.css").read_text()
    out[KIT / "skill/assets/brand.css"] = re.sub(r":root \{.*?\n\}\n", lambda _: block, css, count=1, flags=re.S)
    for name in GUIDE_REFS:
        out[KIT / "skill/references" / name] = stamp((REPO / "guide" / name).read_text(), Path(name))
    out[KIT / "chatgpt-operator-brief.md"] = brief()
    return out


def brief():
    skill = (KIT / "skill/SKILL.md").read_text()
    rules = skill[skill.index("\n1. "):].strip()
    rules = rules.replace("`references/statistics-figures.json`, master copy in GitHub Neurofeedback-Luxembourg/nfl-web `src/data/figures.json`",
                          "GitHub Neurofeedback-Luxembourg/nfl-web `src/data/figures.json`, https://raw.githubusercontent.com/Neurofeedback-Luxembourg/nfl-web/main/src/data/figures.json")
    tests = json.loads((KIT / "tests/tests.json").read_text())["tests"]
    rows = "\n".join(f"| {t['id']} | {t['topic']} | {'; '.join(t['pass'])} | {'; '.join(t['fail_signals'])} |" for t in tests)
    return f"""<!-- brand-kit VERSION {VERSION} -->
<!-- GENERATED by brand-kit/build.py from skill/SKILL.md + tests/tests.json. DO NOT EDIT. -->
# ChatGPT operator brief — Neurofeedback Luxembourg brand (kit {VERSION})

Paste this whole page at the start of any ChatGPT task (WordPress, Surfer, second-opinion reviews). Rulebook: Brand Guide v2.1.2, Google Doc https://docs.google.com/document/d/{DOC_ID}/edit — it wins every conflict. Kit: https://github.com/Neurofeedback-Luxembourg/brand-guide/tree/main/brand-kit (colours `tokens/tokens.css`, real logos `logos/`, figures pointer `figures.md`). Answer "Which brand kit version?" with **{VERSION}**.

Where the rules below name files: `references/brand-guide.md` = https://raw.githubusercontent.com/Neurofeedback-Luxembourg/brand-guide/main/brand-kit/brand-guide.md · `references/business-facts.md` and `references/carried-from-brand-lock-v1.3.md` = the same names under https://raw.githubusercontent.com/Neurofeedback-Luxembourg/brand-guide/main/brand-kit/skill/references/ · `assets/…` = the kit's `logos/` and `tokens/tokens.css`. If you cannot open a link, say so and do not guess its content.

## Rules
{rules}

## Review checklist — the 12 brand tests
Before handing anything back, check it against every test that applies. Any fail signal = fix it or say it fails.

| # | Test | Pass if | Fail signals |
|---|---|---|---|
{rows}
"""


def check():
    errors = []
    for p in text_files():
        if not p.exists():
            errors.append(f"missing: {p.relative_to(REPO)}")
            continue
        m = (JSON_HEADER if p.suffix == ".json" else HEADER).search(p.read_text())
        if not m or m.group(1) != VERSION:
            errors.append(f"{p.relative_to(REPO)}: version header {m.group(1) if m else 'MISSING'} != VERSION {VERSION}")
    bg = (KIT / "brand-guide.md")
    if not bg.exists() or f"Google Doc {DOC_ID}" not in bg.read_text():
        errors.append("brand-kit/brand-guide.md missing or not generated from the Google Doc")
    for path, text in generated().items():
        if path.read_text() != text:
            errors.append(f"{path.relative_to(REPO)}: out of date, run build.py")
    for name in LOGOS:
        if hashlib.sha256((KIT / "logos" / name).read_bytes()).digest() != hashlib.sha256((KIT / "skill/assets" / name).read_bytes()).digest():
            errors.append(f"skill/assets/{name} differs from logos/{name}")
    print("\n".join(errors) or f"brand-kit OK — every file at VERSION {VERSION}")
    return 1 if errors else 0


def build(doc=True):
    if doc:
        (KIT / "brand-guide.md").write_text(export_doc())
    for name in LOGOS:
        (KIT / "skill/assets" / name).write_bytes((KIT / "logos" / name).read_bytes())
    for p in text_files():
        if p.exists():
            p.write_text(stamp(p.read_text(), p))
    for path, text in generated().items():
        path.write_text(text)
    z = KIT / "dist" / f"nfl-brand-skill-v{VERSION}.zip"
    z.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as f:
        for p in sorted((KIT / "skill").rglob("*")):
            if p.is_file():
                f.write(p, Path("nfl-brand") / p.relative_to(KIT / "skill"))
    print(f"built kit {VERSION}; claude.ai upload: {z.relative_to(REPO)}")
    return check()


if __name__ == "__main__":
    sys.exit(check() if "--check" in sys.argv else build(doc="--no-doc" not in sys.argv))
