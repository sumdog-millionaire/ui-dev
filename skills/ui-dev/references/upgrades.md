# Review upstream Taste upgrades

Use when the user asks to review, compare or upgrade ui-dev from Taste. This is maintenance of a customised fork, not installation of a fresh upstream skill. Keep ui-dev's identity, local workflow and both agent integrations.

## Locate the maintained source

Find the ui-dev Git repository and read `upstream.json` at its root. Installed plugin caches and `dist/ui-dev/` are generated artefacts, not the source of truth. A package manager update can replace an installed checkout; make local customisations in the maintained source repository and distribute a new ui-dev version instead.

If only a generated package is available, ask for the maintained repository path. Do not edit the cache or clone over an existing directory. Inspect branch, remotes and `git status` before modifying anything. Report dirty work and preserve it; do not auto-stash, reset, clean, discard files or commit on the user's behalf.

## Fetch and compare — read-only stage

Verify that the `upstream` remote matches the repository in upstream.json. If it is missing or different, surface the discrepancy before changing it. Fetch upstream; fetching updates Git's remote references, not working files. Resolve the actual upstream default branch rather than assuming a name.

Compare `reviewedCommit` with the fetched commit, focusing first on `sourcePath` and then on related source documentation or new capabilities relevant to ui-dev. Read the changed sections in context, including removed guidance and code examples. Inspect relevant licensing changes.

Show a concise review table:

| Upstream change | Recommendation | Reason / local conflict |
|---|---|---|
| Specific change and source location | Adopt / adapt / skip | Benefit and interaction with ui-dev |

Explain what has changed to the human and recommend a selection. Wait for approval before applying changes. A request to review upgrades is not permission to replace the skill or install every optional upstream skill.

## Apply selected changes

Use a three-way comparison: the previously reviewed upstream version, the new upstream version and the customised local version. Apply selected changes in place. Prefer targeted edits; cherry-pick a commit only if its whole effect matches the approved scope. Do not blindly merge upstream/main, overwrite SKILL.md, run an upstream installer or copy the whole skills directory into the distribution.

Preserve these local decisions unless the user explicitly revises them:

- One end-to-end ui-dev skill for all web surfaces, with inferred and visible dials.
- Approved brand rules override aesthetic defaults; omitted guidance is creative freedom.
- Local brand packs with unchanged sources, assets and a reviewed BRAND.md.
- Explicit human actions and decisions; concept and rendered-package approval gates.
- Stitch for new directions, tool-neutral approved artefacts and no required /design command.
- Conditional writing guidance, protected source content and brand voice precedence.
- Quiet executable-only Impeccable integration for Claude Code and Pi, without its skills.
- Natural scrolling, equal mobile importance and tested reduced-motion behaviour.
- Honest verification rather than arbitrary animation/token/component quotas.

Do not update Impeccable or the writing skill just because Taste changed. Those dependencies have their own provenance and regression risks.

## Verify and record

Run `npm test`, `npm run check`, `npm run build` and Claude plugin validation on `dist/ui-dev`. Review the behavioural scenarios in `evals/evals.json`, especially brand conflicts, sparse packs, human handoffs and targeted changes. Run suitable agent evaluations where available; distinguish textual/structural checks from observed model behaviour and browser evidence.

Only after the approved changes pass their checks, update reviewedCommit and reviewNotes in upstream.json to record the fetched commit and adopted/adapted/skipped changes. Record a reviewed-but-skipped upstream change too, so it is not repeatedly proposed. If checks fail, leave the previous baseline and report the incomplete upgrade.

Show the final diff, tests and remaining risks. Commit only if requested. Rebuild the distribution and tell the user how to reload/reinstall it in their agent. Updating the ui-dev package retrieves our maintained version; reviewing upstream Taste is this separate procedure.
