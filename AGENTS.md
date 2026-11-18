<!-- brand-kit VERSION 2.1.5 -->
# AGENTS.md — brand-guide repo

All brand rules for every agent live in [`brand-kit/`](brand-kit/AGENTS.md). Read `brand-kit/AGENTS.md` and `brand-kit/VERSION` before any brand work.

The whole design system (brand book, colours, type, logos, photos, recoveriX images, components, official accounts) is in [`design-system/`](design-system/README.md), as plain files any agent can read. Index of every file with direct links: [`llms.txt`](llms.txt). Web page: https://neurofeedback-luxembourg.github.io/brand-guide/design-system/ . It mirrors the Claude Design System (claude.ai/artifact/EowsRsZbAGGmPPDbLET8k3); to refresh it, copy the artifact's `project/` files into `design-system/` and run `python3 design-system/build_mirror.py`.

Maintaining this repo: Brand Guide v2.1.3 (approved 2 October 2026) in the Google Doc is the only rulebook; §11 states visual identity, voice and languages. The approved local copy is `guide/brand-guide.md`; `python3 brand-kit/build.py --no-doc` rebuilds from it without network access. Never hand-edit generated files (`brand-kit/brand-guide.md`, `brand-kit/tokens/tokens.css`, `brand-kit/chatgpt-operator-brief.md`); change the source and run `python3 brand-kit/build.py`. A version bump = edit `brand-kit/VERSION`, then run the build. CI fails if any version header differs from `VERSION`.
