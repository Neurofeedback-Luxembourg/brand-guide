# SiteHeader

The lean branded header of the statistics site (data.neurofeedback-luxembourg.com): logo, four links to the main site, the free-call button and the language switch.

- Gradient ground (`plum-deep` → `slate`) with `on-brand` text, like the main website header.
- Logo: the website's horizontal white logo (Logos › `logo-site.png`), 56 px high (40 px on phones), linking to neurofeedback-luxembourg.com.
- Links in this order: Who is Neurofeedback Luxembourg? · What we offer · recoveriX · Brain-Curator; then `nfl-btn--on-gradient` "Book a free call" (FR « Réserver un appel gratuit »).
- The LanguageSwitch sits at the far right, separated by a thin rule.
- Below 1080 px the links collapse behind an icon menu button (`aria-expanded`, `aria-controls`, visible label for screen readers); the language switch stays visible. Without JavaScript the links stay open.
- Focus: white ring on the gradient.
