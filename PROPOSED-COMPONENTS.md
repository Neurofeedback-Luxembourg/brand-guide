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
