# Asset Manifest

Last updated: 2026-04-25

This file documents what's in `brand-guide/assets/` — when to use each
folder, what's authoritative, and what was deliberately excluded.

## Structure

```
assets/
├── logos/
│   ├── primary/                ← canonical website logos (use these in code)
│   ├── icon/                   ← square icon variants
│   ├── favicon/                ← favicon files
│   └── raw-canva-exports/      ← higher-res Canva exports + variants for design work
├── photos/
│   ├── team/
│   │   ├── 2023-photoshoot/    ← Frank Weber professional shoot (34 files, JPG)
│   │   └── francois/           ← François portraits + miniatures
│   ├── website/                ← photos used on the live site
│   └── equipment/
│       ├── pbm/                ← photobiomodulation devices
│       ├── recoverix/          ← recoveriX rig
│       └── vielight/           ← Vielight tPBM products
├── illustrations/
│   ├── (loose)                 ← brand illustrations
│   └── abstract/               ← abstract neural / BCI motifs
├── infographics/
│   ├── numbered/               ← Canva-numbered infographic series
│   └── conditions/             ← condition-specific infographics (migraines, phenotypes)
├── social-media/
│   ├── linkedin/               ← LinkedIn banners + cards
│   ├── facebook/               ← Facebook covers
│   ├── youtube/                ← YouTube thumbnails + watermarks
│   ├── campaigns/              ← campaign card series ("Optimize_Your_Brain", etc.)
│   └── educational/            ← educational social posts (training approaches series)
├── raw/                        ← original/unoptimized originals (archival)
└── archive/                    ← under-categorized files for later triage
```

## Where logos come from

Three sources, listed in order of preference:

1. **`logos/primary/`** — canonical, used by the live website. These have
   been through size optimization. Use these unless you have a reason not to.
2. **`logos/raw-canva-exports/`** — direct exports from the Canva NFB
   brand kit (`kAFp79HE62Y`). Higher resolution, less optimized. Use for
   print, large-format, or when primary versions don't fit your need.
3. **The Canva brand kit itself** — for new variants, design in Canva first,
   export to `raw-canva-exports/`, then optimize into `primary/` if it'll
   be used on the web.

## What was deliberately excluded

When this folder was first organized (2026-04-25, from
`C:\Users\Neurofeedback LXBG\Pictures\` → 178 files), the following were
NOT copied because they aren't brand assets:

- **Client medical files** (Otis PBM session captures) — confidentiality.
- **AI playground experiments** (Copilot_, Gemini_Generated, image_fx_,
  Leonardo_Phoenix, NotebookLM, image (1).jpg, etc.) — not brand-grade.
- **Random screenshots** (Settings, NVIDIA Overlay, Pomelli, Dr Tomozei) — irrelevant.
- **Memes / Optical Illusions / Feedback{GUID}** — personal/unrelated.
- **CBD farmer photos** (Steve Wampach Kraut Vum Bauer) — different brand.
- **Hash-named files of unknown provenance** — couldn't verify origin.
- **Personal contact info** (Tom Proost screenshot) — privacy.
- **Facebook download** (398588473_*) — likely third-party.

If any of the above were excluded by mistake, copy them into `archive/`
and re-categorize.

## Photo rights

All photos in this manifest were confirmed by François as cleared for use
(2026-04-25). The `2023-photoshoot/` set is by Frank Weber and was
commissioned by NFL. AI-generated illustrations created in NeuroClaw
ImageGen are owned by NFL.

After 2026-08-02, EU AI Act Article 50 requires AI-generated marketing
content to be labeled. See `tokens/brands/nfl/compliance.json`.

## Open triage items

- `photos/team/francois/2022_09_28_gaufre.jpeg` (11MB) — likely a personal
  meal photo, may not be brand. Confirm or move to archive.
- Several "image (1).jpg", "image (2).jpg" loose files were dropped — if
  any were important, recover from
  `C:\Users\Neurofeedback LXBG\Pictures\` (still intact).
