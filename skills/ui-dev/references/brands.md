# Local brand packs

Packs live in the working repository at `data/brand/<slug>/`, gitignored. Confirm that the location is gitignored before writing into it, add `data/brand/` to `.gitignore` if it is not, and say which. When production code needs an asset, copy only the web-ready files into a tracked location such as `config/brand/`. An explicitly supplied pack path may override the default. Use portable relative paths inside each pack.

Onboarding a brand may be the whole task; it has no design read and ends at the approval step below. `extract-design-md` writes the project's design file, never the pack.

```text
<brand>/
  BRAND.md              # Visual identity
  TONE-OF-VOICE.md      # Written voice
  ASSET-INDEX.md        # Which file to use for which situation
  sources/              # Original guidelines and supplied evidence, unchanged
    _research/          # Extraction notes, each rule cited to document and page
  assets/
    logos/
    fonts/
    images/
    icons/
    patterns/
```

A layout task reads BRAND.md; a copy task reads TONE-OF-VOICE.md. ASSET-INDEX.md is the decision layer over the files, however short: which file for which background and space, and the `assets/{id}` of the brand's Stitch design system with its scope once one is registered (stitch.md).

Where a brand has a single overarching frame, one idea everything else serves, state it in BRAND.md's Identity section and TONE-OF-VOICE.md's Overarching frame section.

Create only directories with supplied material; a sparse pack is valid. The project's design system is `DESIGN.md` at the repo root (design-file.md).

## Selection and missing packs

Use the explicitly named brand or an already recorded project selection. List available pack names if selection is unclear; ask rather than choosing by folder order. If the selected pack is missing, offer onboarding or an explicitly unbranded/project-only direction. Do not silently create an identity.

Read BRAND.md and relevant original guidance before relying on a rule whose meaning is uncertain. Resolve logo variants, backgrounds and fonts by their documented role, not by whichever file is easiest to find. For conflicting versions, ask which source is authoritative.

## Onboarding

1. Accept guidelines, examples, URLs and asset folders. Inspect the actual supplied material with suitable document/image tools. Identify unreadable files or missing capabilities; never claim to have extracted them.
2. Copy originals without modification into sources/ and approved reusable assets into the relevant assets/ directory. Where a source already lives in this repository under version control, record its path and the extraction commit in sources/README.md rather than copying it. Preserve existing files; do not overwrite a different asset with the same filename. Record the relative path, source location and the applicable rights and restrictions with each asset.
3. Draft BRAND.md using the outline below. Each sourced rule names its source file and page/section where available. Mark unknowns and contradictory evidence rather than manufacturing certainty. Summarise sources; retain exact required wording separately where precision matters.
4. Draft TONE-OF-VOICE.md using the outline below, wherever voice material exists. Preserve approved and rejected copy verbatim, because a paraphrased example teaches the wrong thing. Reproduce banned lists in full rather than summarising them. Correct source typos before an example reaches a prompt, and list every correction so the change is visible.
5. Check what the material does not cover. Brand guidelines are often print-first and may state no type scale, grid, spacing, components or motion. Say so plainly rather than inventing rules. Derive the missing patterns from the client's own finished digital work and record them under BRAND.md's "Observed, not stated" section, so a reader can tell what the brand said from what the brand did.
6. Show the profile, unresolved material questions and asset inventory. Ask for approval once before first use. For material later changes, show the changes and obtain approval again. Record only approval actually given.

## BRAND.md outline

```markdown
# <Brand name>

Status: draft | approved
Approved by/date: <only after actual approval>
Source versions: <files, dates or version labels>

## Identity
Audience, positioning and relevant brand principles, with sources.

## Logos
Relative asset paths, variants, clear space, minimum size, allowed backgrounds,
colour treatments and explicit transformation/animation restrictions.

## Typography
Families, roles, weights, fallbacks, supplied font files and known licences.

## Colours
Exact supplied values and intended roles; documented contrast/theme guidance.

## Imagery and icons
Approved assets, subject/style guidance, cropping and credit requirements.

## Composition and motion
Explicit layout, shape, spacing and motion rules. Say when none were supplied.

## Observed, not stated
Patterns derived from the brand's finished digital work where the guidelines are silent,
each naming the work it was read from.

## Writing voice
The two or three governing lines a layout task needs, quoted; everything else is in
TONE-OF-VOICE.md.

## Unknowns and conflicts
Missing information, unreadable evidence and unresolved contradictory sources.

## Source and asset index
Relative paths, original locations, versions and relevant rights/restrictions.
```

## TONE-OF-VOICE.md outline

```markdown
# <Brand name>: tone of voice

Status: draft | approved
Approved by/date: <only after actual approval>
Source versions: <files, dates or version labels>

## Overarching frame
The one idea the voice serves, stated first, with its source.

## How to use this document for prompts
Which sections to paste into a writing prompt, and in what order.

## The governing scale
The brand's own axis (for example formal to conversational, or expert to friendly),
where it sits by default, and what moves it.

## Register
Default sentence length, person, tense, warmth and confidence, with sources.

## Register by content type
One entry per content type the brand produces (web copy, email, social, product UI,
legal), each saying how it departs from the default.

## Mechanics
Spelling, punctuation, capitalisation, numbers, dates, units and formatting rules.

## Vocabulary
Preferred words, banned words in full, product and feature names as written.

## Worked examples
Approved copy verbatim, and rejected copy verbatim with the reason it was rejected.

## Sub-brand overrides
Where a sub-brand or audience changes any of the above.

## Unknowns
Voice questions the sources do not answer.

## Source typos
Each correction made to a source example before it was used, old and new. Omit when empty.
```

## Creative freedom

An omitted rule is not a prohibition. A pack containing only a logo and palette can support a complete project design. The agent may propose typography, motion and a dark theme that respect the supplied rules; record these as project choices in DESIGN.md, not official brand rules in BRAND.md.

Pause for material ambiguity, not every missing field. Altering or deforming an existing logo needs a clear decision if permissions are uncertain. Keep sourced logos intact while that decision is open. Functional accessibility and project constraints remain requirements; report a conflict rather than quietly substituting a different brand treatment.
