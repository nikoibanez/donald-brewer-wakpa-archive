# Donald Brewer (Wakpa) — artist portfolio

The live artist portfolio is at https://donald-brewer-wakpa-archive.netlify.app.

This repository contains a static, accessible gallery of 26 publicly listed paintings with artist-authorized reproductions, individual artwork pages with descriptive alternative text, an artist biography, public-art history, commission inquiries, and a separate research archive that preserves 37 catalog records.

## Structure
- `index.html` — artist-led homepage and painting gallery
- `paintings/*.html` — 26 individual artwork pages
- `research/index.html` — publication dates, catalog sources, collection references, and project documentation
- `artwork/` — 26 artist-authorized painting reproductions, sourced from Fine Art America listings
- `style.css` — typography and responsive layout
- `catalog.json` — catalog data with artwork descriptions
- `catalog.original.json` — source record data used for generation
- `build_portfolio.py` — reproducible static site generator
- `qa_check.py` — validates local links, basic heading semantics, and image text
- `ARTWORK-PERMISSIONS.md` — artist authorization context

## Editorial approach
The original paintings lead; descriptions are based on visual inspection, not invented symbolism. Dates of online posting are not assumed to be dates of creation. No artificial artwork or archival metadata tags appear in the public gallery. Research details live in the separate research section and the collapsible source information on each artwork page.

## Publishing
Run `python build_portfolio.py` then `python qa_check.py`. The website has no build dependency. Publish the repository root with Netlify. The current production site was deployed manually by Netlify CLI. GitHub-to-Netlify continuous deployment is not yet configured.

Artwork copyright © Donald Brewer (Wakpa). Reproduced with permission for his portfolio. Other use may require separate permission.
