# Handoff from the statistics-site session (30 Sept 2026)

From now on brand work runs in its own Claude Code session. The statistics session (nfl-web, data.neurofeedback-luxembourg.com) only reads brand rules from this repo and the Claude Design system; it never edits brand files.

## Current rulebook (4 October 2026)

Brand Guide v2.1.3 (approved 2 October 2026) is the only rulebook (`guide/brand-guide.md`); §11 states visual identity, voice and languages. Kit version: 2.1.5. Brand Guide v2.1.2 and the carried-over Brand Lock reference are archived in `guide/superseded/`. This upgrade is local to `beast1/brand-guide-v2.1.3`; it has not been pushed or merged.

## Historical work finished and merged (30 September 2026)
- Brand Guide v2.1.2 canonical text at that time (now `guide/superseded/brand-guide-v2.1.2.md`), v2.1.1 / v2.1 / Brand Lock v1.3 marked SUPERSEDED.
- nfl-brand skill v2.1.3 (PR #5): g.tec recoveriX intended purpose word for word (recoveriX PRO Instructions for Use V2.18.01, Rev. 2.6, 2021, §2.1–2.2, Drive https://drive.google.com/file/d/1CSYNFKFmbVPCCHnlEiY6vEZyOblXLAxW/view), statistics-only-from-data-file rule, calm service pages, no citation fragments; `references/statistics-figures.json` snapshot. Zip + rules .md on François's Desktop. Gems / custom GPT packs retired.
- Live-site breach fixes on neurofeedback-luxembourg.com (13 pages, Elementor data, backups in ~/.local/backups/2026_09_30/wp-brand-fixes/): ADHD, home (x2), FAQ (80% success rate, 1,600 brains, "no risk"), insomnia, migraine, neuromodulation, autism, depression, neurofeedback training, values & history, PBM article (CE marking, contraindications).
- Authority figures corrected on BrainMap/ADHD pages, 3 blog articles (all Linguise languages), both op-eds, brain-curator.org, GitHub organisation profile (`Neurofeedback-Luxembourg/.github`, "accredited" removed — no accreditation document found in Drive).
- Summer 2025 landing pages (EN `lp-accelerated-neurofeedback-summer-2025` and French twin `lp-neurofeedback-accelere-ete-2025`, pages 18759 / 18128): unpublished (draft), 301 to the PBM page per language via Cloudflare Worker `nfl-lp-summer-2025-redirect` (code in nfl-web `workers/lp-redirect/`, 20 routes incl. www, one hop each, tested).
- Claude Design system "Neurofeedback Luxembourg" (artifact EowsRsZbAGGmPPDbLET8k3) versions 8–9: 10 statistics-site components, tokens muted / lilac-soft / rule, website horizontal logo. See PROPOSED-COMPONENTS.md — the brand session owns them from now on.

## Open — for the brand session
1. François's decisions pending on unclear website claims: (a) insomnia page + sleep article "90% EEG improved / 82% symptom reduction" (Arns & Pérez-Elvira 2019) and the unverified "AAPB Level 3" line; (b) autism article "26% vs 3%" with no source; (c) high-potential article "Lucas, 12 … 40% reduction" (looks invented); (d) migraine page client brain-map caption "after 15 sessions, anxiety and hypervigilance disappear" (consent + outcome); (e) PBM service page outcome timelines ("1–3 sessions…") and a PBM article "very few side effects, a safe choice".
2. Cloudflare "Purge Everything" (François's click; the API token lacks cache-purge) so Linguise translations served by APO show the corrections.
3. Hermes: kanban task_20260930_BzO5OU — install nfl-brand v2.1.3; no ACK yet.
4. g.tec: ask for the current recoveriX Instructions for Use; replace the 2021 wording if newer.
5. Google Ads: paused campaigns "Accelerated_Neurofeedback_UK" and "Neurofeedback_accéléré_FR" (16 ads) still point to the retired landing pages (they now redirect to PBM) — François to change or remove.
6. Main-site tracking issues found (not changed, François to decide): YouTube embeds set cookies before consent; Google Ads tag loaded twice (Site Kit gtag + GTM) → possible double counting; the site font is Inter (brand says Source Sans 3).
7. "Brand kit for all agents" — not started here.
