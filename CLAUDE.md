# CLAUDE.md - AI Assistant Guide for Neurofeedback Luxembourg Brand Guide

## Project Overview

This repository contains the **official Brand & Style Guide** for **Neurofeedback Luxembourg**, a neurotechnology organization. It serves as a single-source-of-truth for all brand assets, guidelines, and specifications, designed for both human users (freelancers, internal teams) and AI systems to produce consistent, on-brand content.

**Organization:** Neurofeedback Luxembourg
**Tagline:** "Optimize Your Brain, Improve Your Life!"
**Owner:** François Altwies
**Version:** 2.0.0
**License:** MIT

## Technology Stack

This is a **pure static website** with no build tools, frameworks, or external dependencies:

- **HTML5** - Semantic markup with Open Graph and Twitter Card meta tags
- **CSS3** - Custom properties (variables), Flexbox, Grid, responsive design
- **Vanilla JavaScript** - Minimal JS for copy-to-clipboard functionality
- **Hosting:** GitHub Pages at `https://neurofeedback-luxembourg.github.io/brand-guide/`

**No build process required** - files are served directly as static assets.

## Repository Structure

```
brand-guide/
├── CLAUDE.md              # This file - AI assistant guidance
├── README.md              # Project overview and documentation
├── LICENSE                # MIT License
├── assets/                # All brand assets (~5.1 MB)
│   ├── logos/
│   │   ├── primary/       # Main logo variants (PNG, GIF)
│   │   │   ├── nfb-logo-primary.png      # HD logo (796 KB, 1563×1563)
│   │   │   ├── nfb-logo-primary.gif      # Animated logo (600×600)
│   │   │   ├── nfb-logo-canva-hd.png     # Canva HD version
│   │   │   └── nfb-logo-slogan-vertical.png  # Vertical with slogan (1080×1920)
│   │   ├── icon/          # Square icon variant
│   │   │   └── nfb-icon.png
│   │   └── favicon/       # Favicon
│   │       └── nfb-favicon.png
│   ├── social-media/      # Platform-specific assets
│   │   ├── linkedin/      # LinkedIn cover (1584×396)
│   │   └── facebook/      # Facebook cover
│   └── raw/               # Unoptimized/archival assets
│       └── nfb-background.png (2.3 MB)
├── data/
│   └── brand-tokens.json  # Machine-readable design tokens
└── docs/
    └── index.html         # Main brand guide webpage
```

## Brand Design System

### Color Palette

| Name           | Hex Code  | CSS Variable        | Usage                    |
|----------------|-----------|---------------------|--------------------------|
| NFB Purple     | `#813e68` | `--nfb-purple`      | Primary brand color      |
| NFB Blue       | `#074d79` | `--nfb-blue`        | Secondary brand color    |
| NFB Magenta    | `#9f016b` | `--nfb-magenta`     | Accent color             |
| NFB Soft White | `#e2d4e2` | `--nfb-soft-white`  | Light backgrounds/text   |

### Typography

- **Primary Font:** Myriad Pro
- **Fallback Stack:** Arial, "Helvetica Neue", sans-serif
- **System Font Stack (web):** -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, sans-serif
- **Monospace:** SF Mono, Monaco, "Cascadia Code", "Roboto Mono", Consolas, monospace

### Logo Guidelines

- **Primary logo:** Simple two-hemisphere brain icon (purple left, blue right)
- **3D/low-poly brain:** Decorative use ONLY, not for official logo placement
- **Clear space:** Maintain adequate padding around logo
- **Minimum size:** Ensure legibility at small sizes

## Key Files

| File | Purpose |
|------|---------|
| `docs/index.html` | Main brand guide webpage (entry point) |
| `data/brand-tokens.json` | Machine-readable design tokens for programmatic access |
| `assets/logos/primary/nfb-logo-primary.png` | Primary HD logo file |
| `README.md` | Project documentation and usage instructions |

## Development Workflow

### Local Development

1. Clone the repository
2. Open `docs/index.html` in a browser (no server required)
3. For live reload, use any static server:
   ```bash
   # Python
   python -m http.server 8000

   # Node.js (if npx available)
   npx serve
   ```

### Making Changes

1. **HTML changes:** Edit `docs/index.html` directly
2. **Style changes:** CSS is embedded in `<style>` tags within `index.html`
3. **Brand tokens:** Update `data/brand-tokens.json` for programmatic consumers
4. **Assets:** Add new assets to appropriate subdirectory under `assets/`

### Git Conventions

- **Commit messages:** Use conventional commits with feature flags (e.g., `feat:`, `fix:`, `docs:`)
- **Branch strategy:** Feature branches merged to main
- **Clean commits:** Keep working tree clean before committing

## Conventions for AI Assistants

### When Modifying This Codebase

1. **Preserve brand consistency:** Always use official colors from the palette
2. **Use design tokens:** Reference `brand-tokens.json` for programmatic color/font values
3. **Maintain semantic HTML:** Use appropriate heading levels, ARIA labels where needed
4. **Keep CSS organized:** Follow existing naming patterns (BEM-like: `.card__content`, `.card__actions`)
5. **Test responsiveness:** Ensure changes work on mobile viewports
6. **Update tokens:** If adding new design values, add them to `brand-tokens.json`

### When Generating Brand Content

1. **Always use the tagline:** "Optimize Your Brain, Improve Your Life!"
2. **Reference official colors:** Use hex codes from the palette, not approximations
3. **Use correct logo:** Two-hemisphere brain icon is the official logo
4. **Legal disclaimer:** Include "No diagnostic claims. For brand and communications use only." where appropriate
5. **Credit ownership:** François Altwies is the brand owner

### File Naming Conventions

- **Lowercase with hyphens:** `nfb-logo-primary.png`
- **Prefix with `nfb-`:** For brand-specific assets
- **Descriptive names:** Include purpose/variant in filename

## Current State Notes

The HTML structure in `docs/index.html` currently includes:
- Complete header with hero section and download links
- Navigation menu linking to all sections
- Logos section with asset cards
- Placeholder comment for remaining sections (`<!-- ... (rest of the HTML content) ... -->`)
- Footer with legal disclaimer
- JavaScript for copy-to-clipboard functionality

### Known Gaps

- SVG versions of logos are referenced but not present in repository
- YouTube assets mentioned in HTML but files not included
- ICO favicon format referenced but only PNG exists
- CSS styles section has placeholder comment

## API/Data Access

### Brand Tokens JSON

Access programmatically at `/data/brand-tokens.json`:

```json
{
  "brand": "Neurofeedback Luxembourg",
  "tagline": "Optimize Your Brain, Improve Your Life!",
  "colors": {
    "purple": "#813e68",
    "blue": "#074d79",
    "magenta": "#9f016b",
    "softWhite": "#e2d4e2"
  },
  "typography": {
    "primary": "Myriad Pro",
    "fallback": "Arial, \"Helvetica Neue\", sans-serif"
  }
}
```

## Deployment

- **Platform:** GitHub Pages
- **URL:** https://neurofeedback-luxembourg.github.io/brand-guide/
- **Deployment:** Automatic from repository (no CI/CD configuration needed)
- **Entry point:** `docs/index.html`

## Quick Reference for Common Tasks

| Task | Action |
|------|--------|
| Get brand colors | Read `data/brand-tokens.json` or reference table above |
| Download logo | Use `assets/logos/primary/nfb-logo-primary.png` |
| View brand guide | Open `docs/index.html` in browser |
| Add new asset | Place in appropriate `assets/` subdirectory |
| Update design tokens | Edit `data/brand-tokens.json` |
| Check brand owner | François Altwies (see governance in tokens) |
