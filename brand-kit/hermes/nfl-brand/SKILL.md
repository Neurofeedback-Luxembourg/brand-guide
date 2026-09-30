---
name: nfl-brand
description: Neurofeedback Luxembourg brand rules — LOADER. Use for ANY copy, design, social post, email, slide, image prompt, statistics entry or review reply for Neurofeedback Luxembourg, recoveriX Luxembourg or Brain-Curator/CURATOR. Holds no rules itself; reads the live shared brand kit.
---
<!-- brand-kit VERSION 2.1.4 -->
# nfl-brand (loader — reads the shared brand kit)

This file holds **no brand rules**. The only source is the shared kit in GitHub `Neurofeedback-Luxembourg/brand-guide` → `brand-kit/` (public). Never answer from memory or from an older copy.

Base URL: `https://raw.githubusercontent.com/Neurofeedback-Luxembourg/brand-guide/main/brand-kit/`

1. Read `VERSION` (e.g. `curl -fsS <base>VERSION`). Say which kit version you use when asked.
2. Read `skill/SKILL.md` and follow it exactly. Read the files it names from `skill/references/` (`brand-guide.md`, `business-facts.md`, `carried-from-brand-lock-v1.3.md`) — same base URL.
3. Figures: only from the data file named in `figures.md` (or its primary source), with source and year.
4. Visuals: colours and fonts from `tokens/tokens.css`; logos only from `logos/` (never redraw).
5. If any fetch fails: stop brand work, say "brand kit unreachable", and do not fall back to memory or to old files.

Before anything is published, run the `nfl-brand-review` skill.
