# Donald Brewer (Wakpa) — Artist Portfolio

Live site: https://donald-brewer-wakpa-archive.netlify.app

This source-controlled static portfolio includes 26 artist-authorized painting reproductions with individual artwork pages; 12 gallery and auction records for works outside the current portfolio; further named print editions; a profile of the artist's work and projects; and a history of exhibitions, awards, publications, and collections.

## Public pages

- `index.html`: gallery-led homepage, About Don, Public Art and commissions.
- `paintings/*.html`: 26 individual painting pages, plus `paintings/other-works.html` listing gallery, auction and historical print references.
- `exhibitions/index.html`: five historical exhibitions (1988–1992), two Heard Museum artist-market appearances (2007 and 2010), two awards (1989 and 1990), and collection/archival references.
- `publications/index.html`: dated media appearances, 1995 painter directory, 2001 record cover credit, university artist biography, print editions and a YouTube artist-profile video.
- `artwork/`: twenty-six photographs of artwork reproduced with the artist's explicit permission, from his Fine Art America listings.

The site presents only what is known, in plain language for the public. It does not flag gaps, unverified items, or work in progress.

## Regeneration and validation

Run the following in order from the repository directory:

```sh
python update_catalog_sources.py
python build_portfolio.py
python incorporate_sources.py
python qa_check.py
```

The site uses static HTML and CSS; no Node build dependencies are needed.

## Deployment

Deploy only the public site files (`index.html`, `style.css`, `artwork/`, `paintings/`, `exhibitions/`, `publications/`) with the Netlify CLI. The build scripts, catalog data, and README are working files and are not part of the published site.

Artwork images copyright Donald Brewer (Wakpa). Reproduced with permission. The site is independent of referenced holding institutions and the Cheyenne River Sioux Tribe.

Current deployment is manual via Netlify CLI; GitHub continuous deployment has not been configured.
