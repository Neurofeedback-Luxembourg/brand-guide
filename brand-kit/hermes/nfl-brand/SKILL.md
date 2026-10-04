---
name: nfl-brand
description: Neurofeedback Luxembourg brand rules — LOADER. Use for ANY copy, design, social post, email, slide, image prompt, statistics entry or review reply for Neurofeedback Luxembourg, recoveriX Luxembourg or Brain-Curator/CURATOR. Reads the live shared brand kit and applies standing drafting instructions.
---
<!-- brand-kit VERSION 2.1.5 -->
# nfl-brand (loader — reads the shared brand kit)

Brand Guide v2.1.3 (approved 2 October 2026) is the only rulebook, including visual identity, voice and languages in §11. The shared kit is in GitHub `Neurofeedback-Luxembourg/brand-guide` → `brand-kit/` (public). Never answer from memory or from an older copy.

Base URL: `https://raw.githubusercontent.com/Neurofeedback-Luxembourg/brand-guide/main/brand-kit/`

1. Read `VERSION` (e.g. `curl -fsS <base>VERSION`). Say which kit version you use when asked.
2. Read `skill/SKILL.md` and follow it exactly. Read the files it names from `skill/references/` (`brand-guide.md`, `business-facts.md`) — same base URL.
3. Figures: only from the data file named in `figures.md` (or its primary source), with source and year.
4. Visuals: colours and fonts from `tokens/tokens.css`; logos only from `logos/` (never redraw).
5. If any fetch fails: stop brand work, say "brand kit unreachable", and do not fall back to memory or to old files.

Before anything is published, run the `nfl-brand-review` skill.

## Standing rules for drafting
Apply the brand guide as standing instructions, not just as a source to read.
Every health-related piece ends with the exact §1 disclaimer in the language of the piece:
- EN: "Neurofeedback is brain training, not a medical treatment, and does not replace medical advice."
- FR: « Le neurofeedback est un entraînement cérébral, pas un traitement médical, et ne remplace pas un avis médical. »
- DE: „Neurofeedback ist ein Gehirntraining, keine medizinische Behandlung, und ersetzt keine ärztliche Beratung."
For recoveriX, use g.tec's intended-purpose wording instead, as §1 requires.
Every number carries its source; mark unconfirmed dates as unconfirmed.
Write missing links as a visible placeholder, never invent them.
