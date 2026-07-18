// Override of @preview/orange-book's bundled typst-show.typ partial,
// identical to the sibling project's override except for this book's own
// cover artwork. The full-bleed cover image is prepended here, before
// #show: book.with(...) runs, because that content is inserted into the
// pandoc body, which book() always renders *after* its own front matter
// (title page, blank verso, TOC) — too late to be the first thing the
// reader sees. Deliberately not using book()'s own `cover:` parameter
// either: it unconditionally overlays a title/subtitle/author text block
// on top of the image, and this cover art already has the title and
// author hand-lettered into the illustration itself.
//
// paper: "a4" is explicit and required, not cosmetic: at this point in
// the document, page.typ's own #set page(...) (default "us-letter") is
// the only page rule in effect — book()'s "a4" default (its own
// hardcoded paper-size, never overridden by this project) only takes
// over once #show: book.with(...) below actually runs. Without this, the
// cover would silently render on a US Letter page while every page after
// it is A4, visibly cropping the artwork.
#page(margin: 0pt, paper: "a4")[
  #image("assets/cover.png", width: 100%, height: 100%)
]
#pagebreak()

#import "@preview/orange-book:0.7.1": book, part, chapter, appendices

#show: book.with(
$if(title)$
  title: [$title$],
$endif$
$if(subtitle)$
  subtitle: [$subtitle$],
$endif$
$if(by-author)$
  author: "$for(by-author)$$it.name.literal$$sep$, $endfor$",
$endif$
$if(date)$
  date: "$date$",
$endif$
$if(lang)$
  lang: "$lang$",
$endif$
  main-color: brand-color.at("primary", default: blue),
  // book()'s own default is true, which indents the first line of every
  // paragraph after the first in a block (visually reads like a tab
  // after the newline) — Quarto's own copy of this partial never
  // exposes this parameter at all, so there's no way to turn it off
  // without this override.
  first-line-indent: false,
  logo: {
    let logo-info = brand-logo.at("medium", default: none)
    if logo-info != none { image(logo-info.path, alt: logo-info.at("alt", default: none)) }
  },
$if(toc-depth)$
  outline-depth: $toc-depth$,
$endif$
$if(lof)$
  list-of-figure-title: "$if(crossref.lof-title)$$crossref.lof-title$$else$$crossref-lof-title$$endif$",
$endif$
$if(lot)$
  list-of-table-title: "$if(crossref.lot-title)$$crossref.lot-title$$else$$crossref-lot-title$$endif$",
$endif$
$if(margin-geometry)$
  padded-heading-number: false,
$endif$
)

$if(margin-geometry)$
// Configure marginalia page geometry for book context
// Geometry computed by Quarto's meta.lua filter (typstGeometryFromPaperWidth)
// IMPORTANT: This must come AFTER book.with() to override the book format's margin settings
#import "@preview/marginalia:0.3.1" as marginalia

#show: marginalia.setup.with(
  inner: (
    far: $margin-geometry.inner.far$,
    width: $margin-geometry.inner.width$,
    sep: $margin-geometry.inner.separation$,
  ),
  outer: (
    far: $margin-geometry.outer.far$,
    width: $margin-geometry.outer.width$,
    sep: $margin-geometry.outer.separation$,
  ),
  top: $if(margin.top)$$margin.top$$else$1.25in$endif$,
  bottom: $if(margin.bottom)$$margin.bottom$$else$1.25in$endif$,
  // CRITICAL: Enable book mode for recto/verso awareness
  book: true,
  clearance: $margin-geometry.clearance$,
)
$endif$
