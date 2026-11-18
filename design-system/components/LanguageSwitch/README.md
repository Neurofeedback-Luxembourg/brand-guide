# LanguageSwitch

Globe icon with "EN · FR"; the current language is highlighted, the other is a link to the same page in that language.

- Never flags: a flag stands for a country, not a language, and is an accessibility problem.
- Current language: white box, `plum-deep` text, `aria-current="true"`; the link carries `hreflang` and `lang`.
- Targets at least 32 × 32 px; the group has `aria-label` "Language" / « Langue ».
- Always visible, also on phones (outside the menu).
