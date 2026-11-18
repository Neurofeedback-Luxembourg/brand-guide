<!-- mirror note (added by build_mirror.py) -->
> **Public copy for every agent.** This folder mirrors the Claude Design System "Neurofeedback Luxembourg" (https://claude.ai/artifact/EowsRsZbAGGmPPDbLET8k3, Claude only). Files named in this README sit next to it: logos in `assets/Logos/`, photos in `assets/Photos/`, recoveriX images in `assets/recoveriX/`, colours and type in `tokens.json` / `tokens.css`, components in `components/`. Index of every file with direct links: https://raw.githubusercontent.com/Neurofeedback-Luxembourg/brand-guide/main/llms.txt · web page: https://neurofeedback-luxembourg.github.io/brand-guide/design-system/

# Neurofeedback Luxembourg

Measurement-first brain training in Luxembourg since 2014. "We measure, we train, we re-measure." This system is the visual layer of **Brand Guide v2.1.3** (Google Drive, "04_BRAND — Brand Guide v2.1.3 (APPROVED 2026-10-02)": https://docs.google.com/document/d/1NxZxOLLb2euoepbsEsnt7I4n8vNK-BRg4JSurg7MXrE/edit). Earlier versions are archived. If anything here disagrees with the Brand Guide, the Brand Guide wins.

**Brand kit:** this system matches brand-kit **2.1.5** (GitHub `Neurofeedback-Luxembourg/brand-guide` › `brand-kit/`, https://github.com/Neurofeedback-Luxembourg/brand-guide/tree/main/brand-kit), which other agents load: same 17 colours, spacing, radii, shadows, font stack and the five PNG logo files (checked 2026-10-21; the kit's token names carry an `nfl-` prefix). The vector logo (SVG, approved 2026-10-21) is newer than kit 2.1.5. Asked which brand kit version applies, answer 2.1.5. When the kit's `VERSION` changes, re-check and update this line.

## Content fundamentals

- **Three fixed rules:** never invent (every number carries its source) · never promise an outcome · protect clients (no identification or health details without written consent). Everything else is guidance.
- **Voice by channel:** op-eds and LinkedIn sharp and first person; service pages calm and reassuring; statistics and research pages neutral and sourced, confident in tone, with caveats placed next to the source rather than in front of the number; video warm and fast.
- **Claim ladder:** label statements as Fact · Research finding · Our observation · Opinion.
- **Vocabulary (preferences, not bans):** training, sessions, client, brain map, our offices. Scientific and clinical terms, condition names and study wording are fine wherever accurate.
- **Numbers:** as many as the piece needs, each with its source. Authority figures, always exactly: 3,500+ brain maps · 25,000+ sessions · since 2014 · 19 electrodes · 140+ Google reviews, 4.9/5 average.
- **Main slogan:** FR « Prenez en main votre santé mentale » · EN "Take charge of your mental health" (website hero; confirmed as the main slogan by François Altwies, 2026-10-24). Use it for covers and banners; "We measure, we train, we re-measure." stays the method line.
- **SEO keywords:** neurofeedback · qEEG (cartographie cérébrale / brain map) · BCI — interface cerveau-ordinateur / brain-computer interface (recoveriX) · photobiomodulation · stimulation du nerf vague (vagus nerve stimulation / Vagusnervstimulation). Place them early in every public text. Profiles, directories and job boards open with these keywords, never with a historical story (confirmed by François Altwies, 2026-10-24).
- **Invitation:** a free phone call — FR « rendez-vous téléphonique gratuit et sans engagement ». Phone +352 42 31 55 44 (recoveriX +352 42 31 55 55).
- **Disclaimer on health content:** EN "Neurofeedback is brain training, not a medical treatment, and does not replace medical advice." · FR « Le neurofeedback est un entraînement cérébral, pas un traitement médical, et ne remplace pas un avis médical. » · DE „Neurofeedback ist ein Gehirntraining, keine medizinische Behandlung, und ersetzt keine ärztliche Beratung." recoveriX uses g.tec's intended-purpose wording.
- **AI label:** only on AI-generated images (EU AI Act Art. 50). No "Created with AI assistance" line on reviewed, signed text.
- **Never:** fake scarcity or countdowns, "cure", "guaranteed", "100% safe", "no side effects", "miracle".

## Visual foundations

- **Light-mode brand.** `white` ground, `ink` text, `lilac` surfaces and bands, `plum-deep` and `slate` for depth. There is no dark theme on purpose; reject any "clinical dark-mode" palette on sight.
- **The gradient:** `linear-gradient(135deg, var(--plum-deep), var(--slate))`, always with `on-brand` (white) text. It carries heroes, title slides and social covers — at most one gradient area per view.
- **Accent:** `magenta` is for links, small accents, active states and the primary button. Never paragraphs, never errors.
- **Logo colours:** `plum` and `deep-blue` belong to the logo; use them for headings or large accents only.
- **Status:** `success` / `warning` / `error` for icons and borders; their `-text` variants for words. Never state by colour alone — pair with an icon or words.
- **Type:** Source Sans 3 (web) / Myriad Pro (print), one family; scale `display` → `label`. Never Inter or Montserrat.
- **Layout:** airy, rounded (`radius-lg` cards), spacing only from the `space-*` steps, data callouts in `callout` style (`plum-deep`); on statistics pages one per figure card.
- **Focus:** every control shows `focus-ring`.
- **Motion:** purposeful — count-ups, charts that draw on scroll; `prefers-reduced-motion` shows the final state with no animation.
- **Accessibility:** WCAG 2.2 AA — contrast on every pair, keyboard and visible focus, text alternative and data table for every chart, never colour alone, targets at least 24×24 px.

## Logo

The low-poly brain (magenta-plum front, steel-blue back) above "Neurofeedback-Luxembourg.com". Use the files in **Logos** — never redraw, trace or regenerate it.

- On white: `logo-transparent.png`.
- On the gradient: `logo-white.png` as a badge (white rounded box, `radius-sm`, top-right), or `logo-reversed-transparent.png` directly on the gradient.
- Small formats (avatars, favicons, stickers): `logo-icon-transparent.png`.
- Print and any size where a PNG would blur: `logo-transparent.svg` (full logo, dark text) and `logo-icon-transparent.svg` (brain only). Vector redraw of the 4096 px master, approved 2026-10-21. Good for screen and normal print (cards, flyers, A4–A3 posters); for very large signage seen up close, have a designer polish the facet edges first.
- Clear space: on every side, at least the height of the capital "N" in the wordmark (icon alone: a quarter of its width).
- Minimum size: full logo 30 mm / 120 px wide; icon 8 mm / 24 px wide.
- Still to do: white and reversed versions of the vector logo.

## Imagery and iconography

- Calm, competent, warm, light and bright; real equipment, real offices, daylight, diverse adults.
- **Photos:** the approved brand shoot is in **Photos** (Frank Weber, 2023; consent of the people shown confirmed). Use it before any stock image; its README says what each photo shows and what to avoid.
- **recoveriX:** recoveriX images live in their own **recoveriX** group. Always name and label them recoveriX, with g.tec's intended-purpose wording; its README gives the rules and what each image shows.
- Motif: the low-poly brain; optional EEG trace from slow waves to an alpha spindle — never an ECG heartbeat.
- Never: hospitals, before/after, people in distress, children in medical settings, glowing generic brains, lightbulbs, AI images of real team members or clients. AI images carry an AI label.
- No service icon set exists yet; use words, not emoji.

## Offer (for context)

(A) Training in our offices: BrainMap (qEEG), neurofeedback, Safe and Sound Protocol, tVNS, Creyos cognitive testing. Training packages include SSP and tVNS sessions; photobiomodulation is optional. (B) PBM and tVNS devices sold and rented. (C) recoveriX Luxembourg — exclusive g.tec franchise for BCI rehabilitation, presented openly and clearly labelled. (D) Research — CURATOR (FNR Industrial Fellowship with the University of Luxembourg) and published literature, presented openly. Four brands of Servicium S.A.: Neurofeedback Luxembourg, recoveriX Luxembourg, Brain-Curator/CURATOR, with François Altwies as shared signature. No longer offered, never mentioned: HRV assessment, EEG-assisted meditation, NeuroCoaching, "Brain Performance Enhancement". Prices: the website prices page is authoritative.

## Official accounts

Use these full addresses in profiles, directories and job boards (the website footer uses bit.ly short links). Checked 2026-10-24.

- Website: https://neurofeedback-luxembourg.com
- recoveriX Luxembourg website (BCI — brain-computer interface / interface cerveau-ordinateur — for motor neurorehabilitation after stroke and in multiple sclerosis): https://neurofeedback-luxembourg.recoverix.com/fr/ (also /en/, /lb/, /it/, /es/; German at the root). Confirmed by François Altwies, 2026-10-24.
- LinkedIn: https://www.linkedin.com/company/neurofeedback-luxembourg
- Facebook: https://www.facebook.com/NeurofeedbackinLuxembourg
- Instagram: https://www.instagram.com/neurofeedback_luxembourg/
- YouTube: https://www.youtube.com/@Neurofeedback_Luxembourg
- Threads: https://www.threads.com/@neurofeedback_luxembourg (confirmed by François Altwies, 2026-10-24). Some sites (e.g. Moovijob) only accept the older address https://www.threads.net/@neurofeedback_luxembourg, which opens the same account.
- X / Twitter: @Neurofeedback_L — named in the website's page metadata only; activity not checked.
- TikTok: https://www.tiktok.com/@neurofeedback_luxembourg (confirmed by François Altwies, 2026-10-24)

## Components

Plain HTML/CSS classes in `components/bundle.css` (prefix `nfl-`); no JavaScript needed. Each component card shows the markup.

### Which component when

Start from a component before designing anything new. The rule that matters most for each:

| Need | Component | Key rule |
|:-----|:----------|:---------|
| One main action (usually the free call) | **Button** | One primary per view; verbs in the reader's words, never urgency; `<a>` to go somewhere, `<button>` to do something. |
| Open a page or slide | **Hero** | The only gradient area in the view; plain title, one sentence, logo badge top-right. |
| Group one idea (a service, a step, a question) | **Card** | Lilac card; service cards go goal → how it works → what is measured → who it may suit. |
| Show one verified number | **DataCallout** | Source under it or one tap away; never an individual outcome or timeline. |
| One sourced figure with context | **FigureCard** | Claim tag, number, one plain sentence, mini-visual, About this figure, brand line. |
| Caveats, method, full source | **AboutFigure** | The careful wording lives here, so the headline can stay confident. |
| Say what kind of claim it is | **ClaimTag** | Fact · Research finding · Our observation · Opinion; shape as well as colour. |
| A chart | **ChartFrame** | SVG, values labelled on the chart, takeaway with source, data table. |
| Ask for a guess before a headline figure | **GuessSlider** | 3–4 per page at most; the number still shows without JavaScript. |
| Correct a common belief | **MythStrip** | At most one per section; the answer comes from a figure already on the page. |
| Share a card or chart | **ShareMenu** | Plain links only, no third-party share scripts. |
| Switch language | **LanguageSwitch** | EN · FR, never flags; always visible, also on phones. |
| Statistics-site header and footer | **SiteHeader**, **SiteFooter** | Gradient; the footer carries the imprint and the disclaimer. |
| End of any health piece | **Disclaimer** | Exact wording in the piece's language; never below 14 px. |
| Short state message | **StatusNote** | `-text` colours with a symbol and words; magenta never means error. |

### Statistics-site components (added 30 Sept 2026)

Built for the statistics page at data.neurofeedback-luxembourg.com and reusable for slides and social posts: **SiteHeader**, **SiteFooter**, **LanguageSwitch**, **ClaimTag**, **FigureCard**, **AboutFigure**, **GuessSlider**, **ChartFrame**, **ShareMenu**, **MythStrip**. Classes are in `components/bundle.css` (prefix `nfl-`); interactive parts (count-up, guess, copy link, menu) are progressive: every number, chart and link is complete without JavaScript. Source code: GitHub `Neurofeedback-Luxembourg/nfl-web`.

