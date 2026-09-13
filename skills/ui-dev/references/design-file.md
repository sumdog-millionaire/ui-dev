# The product and design files

Two files at the repo root carry a project's design facts. Tools read DESIGN.md's YAML front
matter; prose alone sets nothing.

## PRODUCT.md

The product record, facts only, no visual direction. Sections: Platform (`web`, or `ios`, `android`,
`adaptive`, which switches the detector off), Stack (a new project only), Users, Product Purpose,
Positioning, Operating Context, Capabilities and Constraints, Brand Commitments, Evidence on Hand,
Product Principles, Accessibility and Inclusion. Draw each claim from the project's own records. It
is written once and touched when a fact changes.

## DESIGN.md

The project's design system, written from the built world. It starts as the brand pack's facts
(brands.md) translated into tokens and evolves with each build. Nothing is copied between the pack
and this file: this file points at the pack for sources.

The spec, version `alpha`, has two layers:

**YAML front matter**, the machine-readable tokens, which are what Stitch and the detector actually
read. Keys: `version` (`alpha`), `name`, `description`, `omitted` (sections left out, with reasons),
`colors` (a map of token name to hex; `primary` is required), `typography` (a map of level to
`fontFamily`, `fontSize`, `fontWeight`, `lineHeight`, `letterSpacing`, and optionally
`fontFeature`, `fontVariation`), `rounded` (level to dimension), `spacing` (level to dimension or
number), `components` (component to `backgroundColor`, `textColor`, `typography`, `rounded`,
`padding`, `size`, `height`, `width`; variants as sibling keys like `button-primary-hover`; values
may reference tokens as `{colors.primary}`). Recommended names: colours `primary`, `secondary`,
`tertiary`, `neutral`, `surface`, `on-surface`, `error`; typography `headline-display`,
`headline-lg`, `headline-md`, `body-lg`, `body-md`, `body-sm`, `label-lg`, `label-md`, `label-sm`;
rounded `none`, `sm`, `md`, `lg`, `xl`, `full`.

**Markdown body**, the human rationale, in eight `##` sections in this order, any of which may be
omitted: Overview (or Brand & Style), Colors, Typography, Layout (or Layout & Spacing), Elevation &
Depth (or Elevation), Shapes, Components, Do's and Don'ts. Headings are verbatim because tools
parse them. Extra sections are preserved by every consumer; a duplicate heading makes the file
invalid. Prose may use descriptive colour names that correspond to the tokens.

A minimal example:

```markdown
---
version: alpha
name: Daylight Prestige
colors:
  primary: "#1A1C1E"
  secondary: "#6C7278"
  tertiary: "#B8422E"
  neutral: "#F7F5F2"
typography:
  headline-lg:
    fontFamily: Public Sans
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.02em
  body-md:
    fontFamily: Public Sans
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
rounded:
  sm: 4px
  md: 8px
spacing:
  sm: 8px
  md: 16px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.neutral}"
    rounded: "{rounded.md}"
    padding: 12px
---

## Overview
A calm, professional interface for a healthcare scheduling platform. Sources: data/brand/acme/.

## Colors
- **Primary (#1A1C1E):** deep ink for headlines and core text.
- **Tertiary (#B8422E):** the sole driver for interaction.

## Do's and Don'ts
- Do use the primary colour only for the single most important action per screen.
- Don't mix rounded and sharp corners in one view.
```

## Three ways it gets written

1. **From the brand pack**: the agent translates BRAND.md's sourced rules into the token block and body, naming the pack as the source. The usual route when a pack exists.
2. **From existing code**: `extract-design-md`, when installed, scans stylesheets, theme files and component styles without building; otherwise the agent reads the same places and writes the file. The route for a redesign.
3. **From Stitch**: a project iterated in Stitch without a prior file exports its DESIGN.md with the project zip, and Stitch's design-system panel edits it in place. The route when there was no brand and the direction was found in Stitch.

## Keeping it honest

- `npx @google/design.md lint DESIGN.md` runs eight rules: a broken token reference (error), no `primary` colour, a component whose text and background fall below 4.5:1, colour tokens no component uses, colours without any typography, sections out of order, missing optional sections, and a token count. Run it whenever the file changes; exit code 1 means an error.
- `npx @google/design.md diff before.md after.md` reports tokens added, removed and changed and flags a regression.
- `npx @google/design.md export --format tailwind DESIGN.md` emits a `theme.extend` object; `--format dtcg` emits W3C design tokens for a project that styles through CSS variables.
- The detector's four design-system rules fire only on values declared in the front matter, so an undeclared colour, font, size or radius in the CSS is reported against this file. A prose-only DESIGN.md is invisible to it.
- The detector keeps a sidecar at `.impeccable/design.json` holding what the eight-property component schema cannot (shadows, motion, breakpoints, tonal ramps, full component CSS). Keep it at least `{"schemaVersion": 2, "extensions": {}}` and touch it after every DESIGN.md edit, or the detector notes the file is newer than its sidecar on every session. `impeccable doctor --json` reports drift between them.
