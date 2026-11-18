# FigureCard

One sourced number as a card: claim tag, share menu, the big number, one confident sentence, a mini-visual, the "About this figure" detail and the brand line.

- `lilac` card, `radius-lg`, padding `space-6`. The number uses the `callout` style in the section accent (`plum-deep` by default); the lead card of a section is white with a 2 px accent border and a larger number.
- The headline sentence states the finding plainly, with no hedging; caveats (self-report, not a diagnosis, rolling average, method changes) go into AboutFigure with the source.
- Mini-visuals, inline SVG: 10-person pictogram (shares), 100-dot scale (small shares), bar (index or hours), comparison bars (Luxembourg vs Europe vs World). They are `aria-hidden`: the number and sentence carry the meaning.
- Brand line at the foot: logo icon, source publisher, the section's short URL.
- Motion: the number counts up once when it scrolls into view; with reduced motion the final number simply shows. Screen readers always get the final text.
