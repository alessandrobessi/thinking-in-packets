// Override @preview/orange-book's part() to drop its full-page colored
// background block (main-color.lighten(70%)) while keeping the same
// title text and the same state bookkeeping the package's own
// front-matter outline reads from. Typst's state()/counter() objects are
// identified by string key, not by module scope, so calling them again
// here with the exact keys orange-book's lib.typ uses gets the *same*
// underlying state — no private import needed.
#let part-state = state("part-state", none)
#let part-location = state("part-location", none)
#let part-counter = counter("part-counter")
#let part-change = state("part-change", false)

#let part(title) = {
  pagebreak(to: "odd")
  part-change.update(x => true)
  part-state.update(x => title)
  part-counter.step()
  context {
    let her = here()
    part-location.update(x => her)
  }
  // No small "Part N" overline label — the title itself already reads
  // "Part N — Title" (per _quarto.yml), so an auto-generated label above
  // it would just repeat "Part N" a second time.
  align(center + horizon)[
    #text(size: 2.2em, weight: "bold", title)
  ]
}
