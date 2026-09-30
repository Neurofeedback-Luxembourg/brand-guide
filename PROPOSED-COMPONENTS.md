# Proposed components from the statistics site

Built for data.neurofeedback-luxembourg.com (repo `Neurofeedback-Luxembourg/nfl-web`, styles in `src/styles/site.css`, markup in `src/components/`). Before this session split, they were already published to the Claude Design system "Neurofeedback Luxembourg" (versions 8–9, with README + live preview each). The brand session owns them from now on: review, rename or reject there; the statistics site follows.

| Component | What it is | Site source |
|---|---|---|
| SiteHeader | Gradient header: website logo, links Who is NFL? · What we offer · recoveriX · Brain-Curator, "Book a free call", language switch; icon menu under 1080 px | `src/layouts/Base.astro` |
| SiteFooter | Imprint (Servicium S.A.), address, phone, privacy, cookie settings, disclaimer | `src/layouts/Base.astro` |
| LanguageSwitch | Globe + EN · FR, current language highlighted, no flags | `src/layouts/Base.astro` |
| ClaimTag | Fact · Research finding · Our observation · Opinion, colour + shape | `src/styles/site.css` `.nfl-claim-tag` |
| FigureCard | Big number (count-up), confident headline, mini-visual, About this figure, brand line | `src/components/Card.astro` |
| AboutFigure | `<details>` holding caveats and full source | `src/components/Card.astro` |
| GuessSlider | "Guess first" range slider, reveal with gap | `src/components/Card.astro`, `public/site.js` |
| ChartFrame | SVG chart + takeaway + source + About + Show as table + brand line | `src/components/Chart.astro`, `src/lib/draw.ts` |
| ShareMenu | Plain share links (LinkedIn, Facebook, X, WhatsApp, email, copy) | `src/components/Share.astro` |
| MythStrip | "Myth or number?" reveal strip | `src/components/Myth.astro` |

New tokens used: `muted` #4a4150, `lilac-soft` #f4edf4, `rule` #cdb9cd (contrast notes in the design system tokens).

## Added with the v10 storyline (30 Sept 2026)

Not in the Claude Design system: these come from after the session split. The brand session decides.

| Component | What it is | Site source |
|---|---|---|
| SubBrandMark | Small logo mark before the recoveriX and Brain-Curator links (16 px on a white rounded backing). recoveriX = green X from the official recoverix.com logo; Brain-Curator = brain-curator.org favicon | `public/img/recoverix-mark.svg`, `public/img/brain-curator-mark.svg`, `.nfl-brand-mark` |
| RecoverixAccent | Chapter accent in recoveriX green: #00974D for decoration, #006d38 for text (6.47:1 on white) | `.accent-recoverix` |
| Byline | 40 px round author photo, "By François Altwies, founder…", Bio · LinkedIn, review date | `src/components/StatsPage.astro` `.nfl-byline` |
| AuthorBox | 96 px photo, three bio lines, Bio / LinkedIn / email | `.nfl-author` |
| ChapterLead | "Chapter N" kicker, title, one headline number and one sentence, share | `.nfl-chapter-lead` |
| Bridge | Italic slate sentence leading into the next chapter | `.nfl-bridge` |
| ClaimPill | Claim level as a small pill after the source line (replaces the ClaimTag above the number) | `.nfl-claim-tag` in `.nfl-figure-card__source` |
| OpinionBox (compact) | Signed opinion with a small photo and an "Opinion" pill, inside the chapter it belongs to | `.nfl-opinion` |
| QuizQuestion + QuizMode | Slider (or four options for range answers) per question; a dialog runs all 12 and shows "You guessed k of 12" with share links | `src/components/Quiz.astro`, `public/site.js` |
| NextStep | End-of-page block: prices, free call, phone | `.nfl-next-step` |
