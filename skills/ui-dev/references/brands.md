# The brand pack

A brand lives under `docs/` in the working repository, tracked in git, so the identity travels with
the code that wears it. `DESIGN.md` carries everything visual in the open spec (design-file.md), and
the pack beside it carries what that spec has no place for: the written voice, the files, and the
evidence.

```text
docs/
  DESIGN.md               # Visual identity: tokens, rationale, logos, motion (design-file.md)
  PRODUCT.md              # Product record (design-file.md)
  brand/
    TONE-OF-VOICE.md      # Written voice
    assets/
      logos/
      fonts/
      images/
      icons/
      patterns/
    sources/              # Original guidelines and supplied evidence, unchanged
      README.md           # What was read, where it came from, rights and restrictions
      _research/          # Extraction notes, each rule cited to document and page
```

`DESIGN.md` sits in `docs/` and not inside `docs/brand/` because the detector looks for it in
exactly three places, a project's own folder, its `docs/` and its `.agents/context/`, and its
design-system rules switch off silently when the file is anywhere else (design-file.md says how it
picks the project folder and how to prove the rules fire). `PRODUCT.md` sits beside it because the
detector takes both from one folder.

A value is written once. Colours, type, radii, spacing and component styling are `DESIGN.md`'s and
appear nowhere in the pack; audience, positioning and anti-references are `PRODUCT.md`'s and
`DESIGN.md` points at them. A layout task reads `DESIGN.md`; a copy task reads TONE-OF-VOICE.md.

Create only directories with supplied material; a sparse pack is valid. Use portable relative paths,
written from the repo root. Where a client's assets may not be committed, gitignore
`docs/brand/assets/` and `docs/brand/sources/` alone and say so; the markdown stays tracked. A repo
holding more than one product gives each its own `docs/` inside that product's folder, which is how
the detector resolves the file that governs an edit.

Onboarding a brand may be the whole task; it has no design read and ends at the approval step below.

## What the pack adds to DESIGN.md

The spec's token block and eight sections are in design-file.md. A consumer preserves a section it
does not know, so the brand's remaining facts go in the same file, after the spec's sections:

```markdown
---
status: draft | approved
approved: <who and when, only after actual approval>
sources: <files, dates or version labels>
stitch: <assets/{id} and its scope, once a design system is registered (stitch.md)>
# then the spec's keys: version, name, description, colors, typography, ...
---

## Overview
The one overarching frame, where the brand has one: the idea everything else serves. Then the
scene the interface is used in. Audience and positioning are PRODUCT.md's.

<!-- Colors to Do's and Don'ts, as the spec orders them -->

## Logos
Which file for which background and space, as a decision table. Clear space, minimum size, allowed
backgrounds, colour treatments and explicit transformation and animation restrictions.

## Imagery and icons
Approved assets, subject and style guidance, cropping and credit requirements.

## Motion
Durations, curves and what motion is for. Say when none were supplied.

## Writing voice
The two or three governing lines a layout task needs, quoted; everything else is in
docs/brand/TONE-OF-VOICE.md.

## Observed, not stated
Patterns derived from the brand's finished digital work where the guidelines are silent, each
naming the work it was read from.

## Project choices
What the agent proposed and the user approved for this project where the brand is silent: a type
scale, a dark theme, a motion language. Never presented as the brand's own rule.

## Unknowns and conflicts
Missing information, unreadable evidence and unresolved contradictory sources.
```

The Logos table is the decision layer over the asset files, however short. File names rarely say
which to reach for, because the choice turns on the background, the space and what must be legible,
so the table is ordered by those questions and ends at a path.

## Missing packs

If the repo has no `docs/DESIGN.md` and no pack, offer onboarding or an explicitly unbranded
direction. Do not silently create an identity.

Read the original guidance in `sources/` before relying on a rule whose meaning is uncertain. Resolve
logo variants, backgrounds and fonts by their documented role, not by whichever file is easiest to
find. For conflicting versions, ask which source is authoritative.

## Onboarding

1. Accept guidelines, examples, URLs and asset folders. Inspect the actual supplied material with suitable document/image tools. Identify unreadable files or missing capabilities; never claim to have extracted them.
2. Copy originals without modification into `sources/` and approved reusable assets into the relevant `assets/` directory. Where a source already lives in this repository under version control, record its path and the extraction commit in `sources/README.md` rather than copying it. Preserve existing files; do not overwrite a different asset with the same filename. Record each asset's relative path, source location and the applicable rights and restrictions in `sources/README.md`.
3. Draft `DESIGN.md`: the token block and the spec's sections from the brand's stated values (design-file.md), then the sections above. Each sourced rule names its source file and page or section where available. Mark unknowns and contradictory evidence rather than manufacturing certainty. Summarise sources; retain exact required wording separately where precision matters.
4. Draft TONE-OF-VOICE.md using the outline below, wherever voice material exists. Preserve approved and rejected copy verbatim, because a paraphrased example teaches the wrong thing. Reproduce banned lists in full rather than summarising them. Correct source typos before an example reaches a prompt, and list every correction so the change is visible.
5. Check what the material does not cover. Brand guidelines are often print-first and may state no type scale, grid, spacing, components or motion. Say so plainly rather than inventing rules. Derive the missing patterns from the client's own finished digital work and record them under "Observed, not stated", so a reader can tell what the brand said from what the brand did.
6. Lint the file (design-file.md), then show the profile, unresolved material questions and asset inventory. Ask for approval once before first use. For material later changes, show the changes and obtain approval again. Record only approval actually given.

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

An omitted rule is not a prohibition. A pack containing only a logo and palette can support a
complete project design. The agent may propose typography, motion and a dark theme that respect the
supplied rules; record these under "Project choices", never among the brand's sourced rules.

Pause for material ambiguity, not every missing field. Altering or deforming an existing logo needs a clear decision if permissions are uncertain. Keep sourced logos intact while that decision is open. Functional accessibility and project constraints remain requirements; report a conflict rather than quietly substituting a different brand treatment.
