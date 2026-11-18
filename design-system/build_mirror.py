#!/usr/bin/env python3
"""Build the public mirror of the Claude Design System "Neurofeedback Luxembourg".

The Claude Design System (https://claude.ai/artifact/EowsRsZbAGGmPPDbLET8k3) is an
interactive page that only Claude can read. This folder is a plain-file copy so that
every agent (ChatGPT, Gemini, Codex, Hermes, Mistral...) and every person can use it.

What this script does (run it after copying fresh files from the artifact's project/ folder):
  1. checks that every asset named in design-system.json is here, with the right size;
  2. writes tokens.css (CSS variables with the same names as tokens.json, no prefix);
  3. makes each components/*/preview.html open on its own (adds the two stylesheets,
     turns artifact image links /_blob/<id> into ../../assets/<Group>/<file>);
  4. writes index.html (one static page: rules, colours, type, every asset, every component)
     and ../llms.txt (the plain-text index for agents, every file with its raw URL).

Usage:  python3 design-system/build_mirror.py
"""
import html
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
RAW = "https://raw.githubusercontent.com/Neurofeedback-Luxembourg/brand-guide/main/design-system/"
TREE = "https://github.com/Neurofeedback-Luxembourg/brand-guide/tree/main/design-system"
PAGES = "https://neurofeedback-luxembourg.github.io/brand-guide/design-system/"
ARTIFACT = "https://claude.ai/artifact/EowsRsZbAGGmPPDbLET8k3"
STAMP = "<!-- mirror: stylesheets added by build_mirror.py -->"


def load(name):
    with open(os.path.join(HERE, name), encoding="utf-8") as f:
        return json.load(f)


def check_assets(index):
    blob_map, problems = {}, []
    for group in index["groups"]:
        g = index["assetGroups"][group]
        for key in g["order"]:
            rec = g["files"][key]
            path = os.path.join(HERE, "assets", group, rec["name"])
            blob_map[rec["blob"]] = f"assets/{group}/{rec['name']}"
            if not os.path.exists(path):
                problems.append(f"missing: assets/{group}/{rec['name']}")
            elif os.path.getsize(path) != rec["size"]:
                problems.append(f"size differs: assets/{group}/{rec['name']} ({os.path.getsize(path)} vs {rec['size']})")
    return blob_map, problems


def token_css(tokens):
    colors = {t["name"]: t["value"] for t in tokens["color"]["tokens"]}

    def resolve(v, seen=()):
        m = re.fullmatch(r"\{([^}]+)\}", v)
        if m and m.group(1) in colors and m.group(1) not in seen:
            return resolve(colors[m.group(1)], seen + (m.group(1),))
        return v

    lines = ["/* Neurofeedback Luxembourg — generated from tokens.json by build_mirror.py. Do not edit. */",
             "@import url('https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@400;600;700&display=swap');",
             ":root {"]
    for name, value in colors.items():
        lines.append(f"  --{name}: {resolve(value)};")
    for fam, stack in tokens["type"]["families"].items():
        lines.append(f"  --font-{fam}: {stack};")
    for family in ("spacing", "radius", "shadow"):
        for t in tokens.get(family, {}).get("tokens", []):
            lines.append(f"  --{t['name']}: {t['value']};")
    lines.append("  --gradient: linear-gradient(135deg, var(--plum-deep), var(--slate));")
    lines.append("}")
    for group in tokens["type"]["groups"]:
        for s in group["styles"]:
            decl = [f"font-family: var(--font-{group['family']})", f"font-size: {s['fontSize']}",
                    f"line-height: {s['lineHeight']}", f"font-weight: {s['fontWeight']}"]
            if s.get("letterSpacing"):
                decl.append(f"letter-spacing: {s['letterSpacing']}")
            if s["name"] == "label":
                decl.append("text-transform: uppercase")
            lines.append(f".nfl-type-{s['name']} {{ {'; '.join(decl)}; }}")
    return "\n".join(lines) + "\n"


def fix_previews(blob_map):
    comp_dir = os.path.join(HERE, "components")
    names = []
    for comp in sorted(os.listdir(comp_dir)):
        p = os.path.join(comp_dir, comp, "preview.html")
        if not os.path.isfile(p):
            continue
        names.append(comp)
        with open(p, encoding="utf-8") as f:
            src = f.read()
        out = re.sub(r"/_blob/([0-9a-f]{32})",
                     lambda m: "../../" + blob_map[m.group(1)] if m.group(1) in blob_map else m.group(0), src)
        if STAMP not in out:
            out = out.replace("<head>", "<head>" + STAMP +
                              '<link rel="stylesheet" href="../../tokens.css"><link rel="stylesheet" href="../bundle.css">', 1)
        if out != src:
            with open(p, "w", encoding="utf-8") as f:
                f.write(out)
    return names


def first_sentence(md_path):
    if not os.path.exists(md_path):
        return ""
    with open(md_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                return line
    return ""


def all_files():
    out = []
    for root, dirs, files in os.walk(HERE):
        dirs.sort()
        for fn in sorted(files):
            rel = os.path.relpath(os.path.join(root, fn), HERE).replace(os.sep, "/")
            if rel.startswith("__pycache__"):
                continue
            out.append(rel)
    return out


def write_llms(index, tokens, comps):
    e = lambda p: RAW + p.replace(" ", "%20")
    L = ["# Neurofeedback Luxembourg — brand and design system",
         "",
         "> Public, plain-file copy of the Claude Design System \"Neurofeedback Luxembourg\" (brand rules, colours, type, "
         "logos, photos, recoveriX images, components). Readable by any agent or person without a login. "
         "Brand Guide v2.1.3 (approved 2026-10-02) is the rulebook; the brand kit (brand-kit/) carries the same rules as agent instructions.",
         "",
         "Read in this order: design-system/README.md (the brand book: voice, slogan, SEO keywords, colours, logo rules, imagery, official accounts), "
         "then tokens.json or tokens.css, then the README of the asset group you need. Use the asset files exactly as they are; never redraw the logo.",
         "",
         f"- Web page (images visible): {PAGES}",
         f"- Folder on GitHub: {TREE}",
         f"- Original (Claude only): {ARTIFACT}",
         "",
         "## Rules",
         "",
         f"- [Brand book — design system README]({e('README.md')}): content rules, main slogan, SEO keywords, visual foundations, logo, imagery, offer, official accounts, components",
         f"- [Brand kit — rules for every agent](https://raw.githubusercontent.com/Neurofeedback-Luxembourg/brand-guide/main/brand-kit/AGENTS.md)",
         f"- [Brand Guide v2.1.3 (full rulebook)](https://raw.githubusercontent.com/Neurofeedback-Luxembourg/brand-guide/main/brand-kit/brand-guide.md)",
         f"- [Business facts](https://raw.githubusercontent.com/Neurofeedback-Luxembourg/brand-guide/main/brand-kit/skill/references/business-facts.md)",
         "",
         "## Tokens",
         "",
         f"- [tokens.json]({e('tokens.json')}): {len(tokens['color']['tokens'])} colours, type scale, spacing, radii, shadows, each with a usage note",
         f"- [tokens.css]({e('tokens.css')}): the same as CSS variables (--plum-deep, --space-4, ...)",
         f"- [design-system.json]({e('design-system.json')}): index of asset groups and files",
         ""]
    for group in index["groups"]:
        g = index["assetGroups"][group]
        L.append(f"## Assets — {group}")
        L.append("")
        L.append(f"- [README — rules and what each file shows]({e(f'assets/{group}/README.md')})")
        for key in g["order"]:
            rec = g["files"][key]
            L.append(f"- [{rec['name']}]({e(f'assets/{group}/' + rec['name'])}) ({rec['type']}, {round(rec['size']/1024)} KB)")
        L.append("")
    L.append("## Components (HTML/CSS, prefix nfl-)")
    L.append("")
    L.append(f"- [bundle.css]({e('components/bundle.css')}): all component classes; load tokens.css first")
    for c in comps:
        summary = first_sentence(os.path.join(HERE, "components", c, "README.md"))
        readme = f" [guidelines]({e(f'components/{c}/README.md')})" if os.path.exists(os.path.join(HERE, "components", c, "README.md")) else ""
        L.append(f"- {c}: {summary}{readme} · [preview]({e(f'components/{c}/preview.html')})")
    L.append("")
    with open(os.path.join(REPO, "llms.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(L))


def write_index_html(index, tokens, comps):
    esc = html.escape
    colors = tokens["color"]["tokens"]
    by_name = {t["name"]: t["value"] for t in colors}

    def val(v):
        m = re.fullmatch(r"\{([^}]+)\}", v)
        return by_name.get(m.group(1), v) if m else v

    sw = "".join(
        f'<li><span class="chip" style="background:{esc(val(t["value"]))}"></span><div><b>{esc(t["name"])}</b>'
        f'<code>{esc(val(t["value"]))}</code><small>{esc(t["usage"])}</small></div></li>' for t in colors)
    ty = "".join(
        f'<li><small class="lbl">{esc(s["name"])} · {esc(s["fontSize"])}/{esc(s["lineHeight"])} · {s["fontWeight"]}</small>'
        f'<div class="nfl-type-{esc(s["name"])}">{esc(s.get("sample", s["name"]))}</div></li>'
        for g in tokens["type"]["groups"] for s in g["styles"])
    groups_html = ""
    for group in index["groups"]:
        g = index["assetGroups"][group]
        tiles = ""
        for key in g["order"]:
            rec = g["files"][key]
            p = f"assets/{group}/{rec['name']}"
            dark = ' class="dark"' if any(k in rec["name"] for k in ("reversed", "site")) else ""
            tiles += (f'<li><a href="{esc(p)}"{dark}><img src="{esc(p)}" alt="{esc(rec["name"])}" loading="lazy"></a>'
                      f'<code>{esc(rec["name"])}</code><small>{round(rec["size"]/1024)} KB · '
                      f'<a href="{esc(RAW + p)}">raw link</a></small></li>')
        groups_html += (f'<section><h2>{esc(group)}</h2><p><a href="assets/{esc(group)}/README.md">Rules and what each file shows (README)</a></p>'
                        f'<ul class="tiles">{tiles}</ul></section>')
    comps_html = "".join(
        f'<li><b>{esc(c)}</b> <small>{esc(first_sentence(os.path.join(HERE, "components", c, "README.md")))}</small> '
        f'<a href="components/{esc(c)}/preview.html">preview</a>'
        + (f' · <a href="components/{esc(c)}/README.md">guidelines</a>' if os.path.exists(os.path.join(HERE, "components", c, "README.md")) else "")
        + "</li>" for c in comps)
    page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>NFL Design System</title>
<meta name="description" content="Neurofeedback Luxembourg brand and design system: rules, colours, type, logos, photos, recoveriX images and components, as plain files any agent can read.">
<link rel="stylesheet" href="tokens.css">
<link rel="alternate" type="text/plain" href="../llms.txt" title="Index for agents">
<style>
body{{margin:0;background:var(--white);color:var(--ink);font-family:var(--font-sans);font-size:17px;line-height:26px}}
header{{background:var(--gradient);color:var(--on-brand);padding:var(--space-12) var(--space-4)}}
header .in,main{{max-width:1080px;margin:0 auto}}
header h1{{margin:0 0 var(--space-2);font-size:36px;line-height:44px}}
header p{{margin:0;max-width:60ch}} header a{{color:var(--on-brand)}}
header img{{height:72px;width:auto;background:var(--white);border-radius:var(--radius-sm);padding:var(--space-2) var(--space-3);float:right;margin-left:var(--space-4)}}
main{{padding:var(--space-8) var(--space-4) var(--space-16)}}
h2{{color:var(--plum-deep);font-size:28px;line-height:36px;margin:var(--space-12) 0 var(--space-3)}}
a{{color:var(--link)}} a:focus-visible{{outline:none;box-shadow:var(--focus-ring)}}
.box{{background:var(--lilac);border-radius:var(--radius-lg);padding:var(--space-6)}}
.box ol{{margin:var(--space-2) 0 0;padding-left:1.2em}}
ul{{list-style:none;padding:0;margin:0}}
.sw{{display:grid;gap:var(--space-3);grid-template-columns:repeat(auto-fill,minmax(240px,1fr))}}
.sw li{{display:flex;gap:var(--space-3);align-items:flex-start}}
.sw li div{{display:flex;flex-direction:column}}
.chip{{flex:none;width:40px;height:40px;border-radius:var(--radius-sm);border:1px solid var(--rule)}}
.sw code,.tiles code{{font-size:14px;color:var(--muted)}} small{{font-size:14px;line-height:20px;color:var(--muted)}}
.ty li{{padding:var(--space-3) 0;border-bottom:1px solid var(--lilac)}} .lbl{{display:block}}
.tiles{{display:grid;gap:var(--space-6);grid-template-columns:repeat(auto-fill,minmax(220px,1fr))}}
.tiles li{{display:flex;flex-direction:column;gap:var(--space-1)}}
.tiles a:has(img){{display:block;background:var(--lilac-soft);border-radius:var(--radius-lg);aspect-ratio:4/3;overflow:hidden}}
.tiles a.dark{{background:var(--gradient)}}
.tiles img{{width:100%;height:100%;object-fit:contain;display:block}}
.cp li{{padding:var(--space-2) 0;border-bottom:1px solid var(--lilac)}}
footer{{font-size:14px;color:var(--muted);max-width:1080px;margin:0 auto;padding:0 var(--space-4) var(--space-12)}}
</style>
</head>
<body>
<header><div class="in">
<img src="assets/Logos/logo-transparent.png" alt="Neurofeedback Luxembourg logo">
<h1>Neurofeedback Luxembourg — design system</h1>
<p>Brand rules, colours, type, logos, photos, recoveriX images and components, as plain files. Any agent or person can read this page and every file in it without a login.</p>
</div></header>
<main>
<div class="box"><b>For AI agents</b> (ChatGPT, Gemini, Codex, Mistral, Claude...): start with the plain-text index
<a href="../llms.txt">llms.txt</a>, which lists every file with a direct link. Then:
<ol>
<li><a href="README.md">README.md</a> — the brand book: voice, main slogan, SEO keywords, colours, logo, imagery, official accounts.</li>
<li><a href="tokens.json">tokens.json</a> / <a href="tokens.css">tokens.css</a> — every colour, type style, spacing step and radius.</li>
<li>The README of the asset group you need, then the files as they are. Never redraw the logo.</li>
</ol>
Folder on GitHub: <a href="{TREE}">{TREE}</a></div>

<h2>Colours</h2>
<ul class="sw">{sw}</ul>

<h2>Type — Source Sans 3</h2>
<ul class="ty">{ty}</ul>
{groups_html}
<section><h2>Components</h2>
<p>Plain HTML/CSS classes (prefix <code>nfl-</code>) in <a href="components/bundle.css">components/bundle.css</a>; load <a href="tokens.css">tokens.css</a> first.</p>
<ul class="cp">{comps_html}</ul></section>
</main>
<footer>Copy of the Claude Design System “Neurofeedback Luxembourg”. If anything here disagrees with Brand Guide v2.1.3, the Brand Guide wins. Photos: Frank Weber, 2023. recoveriX images: g.tec medical engineering.</footer>
</body>
</html>
"""
    with open(os.path.join(HERE, "index.html"), "w", encoding="utf-8") as f:
        f.write(page)


README_NOTE = ("<!-- mirror note (added by build_mirror.py) -->\n"
               "> **Public copy for every agent.** This folder mirrors the Claude Design System \"Neurofeedback Luxembourg\" "
               f"({ARTIFACT}, Claude only). Files named in this README sit next to it: logos in `assets/Logos/`, photos in "
               "`assets/Photos/`, recoveriX images in `assets/recoveriX/`, colours and type in `tokens.json` / `tokens.css`, "
               f"components in `components/`. Index of every file with direct links: {RAW.rsplit('design-system/', 1)[0]}llms.txt · "
               f"web page: {PAGES}\n\n")


def add_readme_note():
    p = os.path.join(HERE, "README.md")
    with open(p, encoding="utf-8") as f:
        src = f.read()
    if "<!-- mirror note" not in src:
        with open(p, "w", encoding="utf-8") as f:
            f.write(README_NOTE + src)


def main():
    index, tokens = load("design-system.json"), load("tokens.json")
    blob_map, problems = check_assets(index)
    if problems:
        print("\n".join(problems))
        sys.exit(1)
    add_readme_note()
    with open(os.path.join(HERE, "tokens.css"), "w", encoding="utf-8") as f:
        f.write(token_css(tokens))
    comps = fix_previews(blob_map)
    write_index_html(index, tokens, comps)
    write_llms(index, tokens, comps)
    print(f"ok: {len(blob_map)} assets checked, {len(comps)} component previews, tokens.css, index.html, llms.txt")


if __name__ == "__main__":
    main()
