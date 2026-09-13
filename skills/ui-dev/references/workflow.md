# Workflow

## Terms

- **Brand pack**: the client's identity as they gave it, in `data/brand/<slug>/` in the working repo: BRAND.md, TONE-OF-VOICE.md, ASSET-INDEX.md, sources and assets (brands.md).
- **Design file**: the project's `DESIGN.md` at the repo root, tokens and rationale in the open spec, written from the pack and evolving with the built world (design-file.md).
- **Direction**: the project-specific composition, typography, palette, hierarchy and interaction intent for a surface.
- **Approved package**: the chosen Stitch screens, one per device type the surface needs, a motion storyboard where narrative motion is in scope, and the design file updated to match. The approved package is authoritative for the build.

## At every gate and every hand-off to an outside tool, say

What is ready (with the preview, file or project link); what the user must decide or do, as
numbered steps naming the tool and the screens; the recommendation and its consequence; what to
return (a selection, a screen id, a confirmation); and what happens next and whether the agent is
waiting. "Please confirm" and "review the design" are not instructions. Silence, a successful
import and a rendered preview are not approval.

If a task is possible through available tools, do it rather than assigning it. If login, visual
judgement or an unavailable tool needs a person, state the exact blocker and the shortest steps.
Read the current interface rather than inventing button names.

## 1. Discover

Read the request, the project's instructions, existing design documentation, framework and
dependencies. Identify the audience, the task, the required content and the scope: a new direction,
a material redesign, or a targeted change. Inspect an existing surface before proposing changes and
preserve its routes, behaviour, data and accessibility unless the request changes them.

Resolve the brand with brands.md. If no pack exists, ask what the user wants: onboard a brand into a
pack, or proceed without one. State the design read with its mode and dials and load the mode's
reference. Ask which device types the surface needs. For a new or materially revised direction,
invoke `grilling` with the brief, the findings, the brand constraints and the open decisions, and
follow its rounds until the frontier is empty; if `grilling` is not installed, say so once and ask
the same way. For a targeted change inside an approved direction, skip the gates below and Stitch,
and apply only the relevant rules.

**Complete when** scope, brand or explicit no-brand choice, content constraints, the mode, the dials
and the device types are clear, and for a new direction the decision frontier is empty.

## 2. Direction: first gate

For a new direction, register the design system in Stitch, then generate the first screens for each
device type and up to five variants at the reimagine range, so the choice is between rendered
directions (stitch.md). Present them with a recommendation and ask the user to select or revise
one. Selecting a direction authorises exploration, not the production build.

**Complete when** the user has selected a direction.

## 3. Render and approve: second gate

Follow stitch.md's route: the agent hands the project over, the user iterates in Stitch, and the
agent fetches the screens the user names. The outcome is a rendering per device type, a motion
storyboard where narrative motion is in scope (motion.md), and the design file updated with the
resolved tokens, the supported themes, the responsive rules and the open limitations. Offer Stitch's
prototype view for checking hover states and input sizing before build; a runnable prototype (the
`prototype` skill) only when the open question is how an interaction feels.

Show the rendered direction, its interaction intent and its limitations, name the screens to
inspect, and ask for approval of an identifiable version.

**Complete when** the user approves a named version and any issue that affects the build is
answered or explicitly deferred.

## 4. Implement

Read verification.md and define the checks before changing code. Reuse the current stack,
components, semantic HTML, native CSS and installed dependencies; add a library only when the
approved behaviour needs it. Keep the raw export unchanged in the evidence folder and translate the
design into the project's own code, extracting tokens and components only where they carry real
shared meaning. Motion is written by `animate`. Protected text and facts are never edited for fit;
use layout or progressive disclosure instead.

Work in small coherent changes, each with its focused check, following the project's own commit
policy.

## 5. Verify and deliver

Follow verification.md against the running build and the approved package. Report the implemented
scope, the exact checks and results, where the evidence is, and what remains failing or untested.
Start the project's development server only when useful to the review, on its documented command.
