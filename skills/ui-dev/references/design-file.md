# The product and design files

Two files in `docs/` carry a project's design facts, with the brand pack beside them in
`docs/brand/` (brands.md). Tools read DESIGN.md's YAML front matter; prose alone sets nothing. A
standalone page with no brand and no project may go without either file; say so, and the checks
that read them do not apply.

## PRODUCT.md

The product record, facts only, no visual direction. Sections: Platform (`web`, or `ios`, `android`,
`adaptive`, which switches the detector off), Stack (a new project only), Users, Product Purpose,
Positioning, Operating Context, Capabilities and Constraints, Brand Commitments, Evidence on Hand,
Product Principles, Accessibility and Inclusion. Draw each claim from the project's own records. It
is written once and touched when a fact changes.

## DESIGN.md

The brand's visual identity and the project's design system in one file: the brand's sourced
values as tokens, the rationale for each, and what the build has added since. It points at
`docs/brand/` for files and sources and at PRODUCT.md for audience and positioning, and restates
neither.

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
parse them. Extra sections are preserved by every consumer, which is where the brand's logos,
motion, voice and unknowns go, after the eight (brands.md); a duplicate heading makes the file
invalid. Extra front-matter keys are accepted silently unless one looks like a misspelt spec key.
Prose may use descriptive colour names that correspond to the tokens.

## Writing it well

An agent reads a token's name as its job and the prose as its limits, so the file works only when
both are there.

- **A token is a decision, named by its role.** `primary`, `surface`, `text-muted`, `border-subtle`,
  never `blue` or `gray-1`: a name that describes appearance gives an agent nothing to choose by.
  Writing the block is the moment to audit: drop a value nothing uses, merge two values doing one
  job, and correct one used for the wrong job.
- **Each decision carries its reasoning and its boundary.** Value, then what it is for, then why,
  then where it must not go: "Deep Indigo (`primary`) for primary buttons, selected states and key
  calls to action; never a large background or decoration, because it overpowers the interface."
  The boundary is the part that stops drift, and the part most files leave out. Name the token in
  the prose so the rule and the value stay joined.
- **Components are built from the tokens, in every state.** A component entry references tokens
  (`{colors.primary}`), never a literal the block already names. Default alone is not enough: give
  hover, active, focus, disabled and loading, as sibling keys in the front matter where the eight
  properties can express the state and in the Components prose where they cannot (a focus ring, an
  opacity, a spinner).

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
A calm, professional interface for a healthcare scheduling platform. Sources: docs/brand/sources/.

## Colors
- **Primary (#1A1C1E):** deep ink for headlines, core text and the one filled button on a screen.
  Never a page background, because the interface is meant to read as paper.
- **Tertiary (#B8422E):** the sole driver for interaction: links, the focus ring, a selected tab.
  Never decoration, so that colour always means something can be pressed.

## Do's and Don'ts
- Do use the primary colour only for the single most important action per screen.
- Don't mix rounded and sharp corners in one view.
```

## Three ways it gets written

1. **From the brand's guidelines**: onboarding (brands.md) translates the supplied material's sourced rules into the token block and body, naming each source. The usual route when a brand exists.
2. **From existing code**: `extract-design-md`, when installed, scans stylesheets, theme files and component styles without building; otherwise the agent reads the same places and writes the file. The route for a redesign.
3. **From Stitch**: a project iterated in Stitch without a prior file exports its DESIGN.md with the project zip, and Stitch's design-system panel edits it in place. The route when there was no brand and the direction was found in Stitch.

## Keeping it honest

- `npx -p @google/design.md designmd lint docs/DESIGN.md` runs nine rules: a broken token reference (error), no `primary` colour, a component whose text and background fall below 4.5:1, colour tokens no component uses, colours without any typography, sections out of order, missing optional sections, a top-level key that looks like a misspelt spec key, and a token count. Run it whenever the file changes; exit code 1 means an error. The shorter `npx @google/design.md lint` form prints nothing on Windows.
- `npx -p @google/design.md designmd diff before.md after.md` reports tokens added, removed and changed and flags a regression.
- `npx -p @google/design.md designmd export --format css-tailwind docs/DESIGN.md` emits a Tailwind v4 `@theme` block of CSS variables; `--format json-tailwind` emits a Tailwind v3 `theme.extend` object; `--format dtcg` emits W3C design tokens for a project that styles through CSS variables.
- The detector's four design-system rules fire only on values declared in the front matter, so an undeclared colour, font, size or radius in the CSS is reported against this file. A prose-only DESIGN.md is invisible to it. It walks up from the edited file and stops at the first folder holding a `package.json`, a `.git` or an `.impeccable/`, and looks there only, in that folder itself, its `docs/` and its `.agents/context/`; it looks above that folder only when a root declares it as a workspace. So where the interface has its own `package.json` in a subfolder (`frontend/`), a `docs/DESIGN.md` at the repo root is never reached and the four rules stay silent. Prove them after placing the file: `detect` a scratch stylesheet beside the real ones holding one colour outside the palette, and expect a finding. `impeccable doctor --json` prints the `designPath` and `productPath` it resolved, and takes both from one folder, which is why PRODUCT.md sits beside DESIGN.md.
- The detector keeps a sidecar at `.impeccable/design.json` holding what the eight-property component schema cannot (shadows, motion, breakpoints, tonal ramps, full component CSS). Keep it at least `{"schemaVersion": 2, "extensions": {}}` and touch it after every DESIGN.md edit, or the detector notes the file is newer than its sidecar on every session. `impeccable doctor --json` reports drift between them.
