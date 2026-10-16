# Donald Brewer (Wakpa) — Artist Portfolio

Live site: https://donald-brewer-wakpa-archive.netlify.app

This source-controlled static portfolio includes 26 artist-authorized painting reproductions with individual artwork pages; an independent working catalog of 38 identified auction, gallery, and online-portfolio records; further named print editions; a profile of the artist's work and projects; and a sourced history of exhibitions, awards, publications, and collections.

## Public pages

- `index.html`: gallery-led homepage, About Don, Public Art and commissions.
- `paintings/*.html`: 26 individual painting pages, plus `paintings/other-works.html` listing gallery, auction and historical print references that cannot yet be matched to locally held images.
- `exhibitions/index.html`: five historical exhibitions (1988–1992), two Heard Museum artist-market appearances (2007 and 2010), two awards (1989 and 1990), and collection/archival references.
- `publications/index.html`: dated media appearances, 1995 painter directory, 2001 record cover credit, university artist biography, print editions and a YouTube artist-profile video.
- `research/index.html`: source links, creation-versus-publication dating, primary auction catalogs, undocumented history, and a verification ledger for all twelve user-provided reference links.
- `research/sources_catalog.json`: structured provenance for exhibitions, awards, and external research links.
- `artwork/`: twenty-six photographs of artwork reproduced with the artist's explicit permission, from his Fine Art America listings.

## Regeneration and validation

Run the following in order from the repository directory:

```sh
python update_catalog_sources.py
python build_portfolio.py
python incorporate_sources.py
python qa_check.py
```

The site uses static HTML and CSS; no Node build dependencies are needed.

## Research standards

* Keep object creation dates distinct from listing, upload, publication, exhibition and auction dates.
* The Heard Museum artist-file record confirms historical exhibitions and awards. It is **not** by itself evidence of recent (within ten years) exhibitions or of the museum owning original paintings.
* Collection locations copied from an institutional biography are identified as reported; accession details and current exhibition status remain unverified.
* Facebook and WorthPoint posts that cannot be accessed independently are listed as research leads, not asserted as evidence.
* Auction sales are not curated exhibitions.
* Do not display third-party photos as if their reproduction rights were cleared merely because the artist authorized his underlying work.

Artwork images copyright Donald Brewer (Wakpa). Reproduced with permission. The site is independent of referenced holding institutions and the Cheyenne River Sioux Tribe.

Current deployment is manual via Netlify CLI; GitHub continuous deployment has not been configured.
