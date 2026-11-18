# ChartFrame

A diagram with everything that travels with it: title, share menu, the SVG chart, a one-line takeaway with its source, "About this figure" for method notes, "Show as table" with the data, and the brand line.

- White ground with a 2 px `lilac` border, `radius-lg`, padding `space-6`.
- Charts are SVG drawn at build time, readable without JavaScript, values labelled directly (no legend), series colours `plum` and `deep-blue`; `role="img"` with a `<title>` and a `<desc>` listing every value.
- On scroll, lines draw and end labels fade in; with reduced motion the final state shows.
- The same frame, with logo, source and short URL, is exported as 1200 × 630 (Open Graph), 1080 × 1080 and 1080 × 1350 PNG for social posts.
