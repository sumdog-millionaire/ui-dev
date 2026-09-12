# ui-dev workflow

## Terms

- **Brand pack:** local source guidelines, assets and an approved BRAND.md describing the organisation's identity.
- **Design direction:** the project-specific composition, typography, palette, content hierarchy and interaction intent. It may fill gaps in the brand rules without becoming a new official brand rule.
- **Approved package:** selected rendered views, any required prototype, DESIGN.md and a motion storyboard where necessary. These artefacts are authoritative regardless of the tool that produced them.

## Human–agent collaboration

The user owns decisions; the agent does the legwork and surfaces the decisions and human-only actions needed next. At every approval gate or external-tool handoff, tell the user:

1. What is ready: the result and relevant preview, file or returned project link.
2. What they need to decide or do: concrete numbered steps, naming the tool and selected project/screens where relevant.
3. Your recommendation and the consequence of the choice, when there are alternatives.
4. What to return: a selection, confirmation, edited screen/version ID or other non-secret result.
5. What the agent will do next, and whether it is waiting for them.

Do not say only “please confirm” or “review the design”. Tell the user what to inspect and what approval means. Do not infer approval from silence, an import succeeding or a tool producing a preview. Use the current agent's interactive question tool where available; otherwise ask clearly in the conversation.

If a task is possible through available tools, do it rather than assigning it to the user. If login, account access, visual judgement or an unavailable tool requires human action, state the exact blocker and provide the shortest steps. Never request credentials in chat. Read current interfaces/docs when necessary rather than inventing button names or deep links.

## 1. Discover

Read the request, project instructions, existing design documentation, framework and dependencies. Identify the audience, task, required content and scope: new direction, material redesign or targeted change. Inspect an existing interface before proposing changes. Preserve its routes, behaviour, data and accessibility unless the request changes them.

Resolve the named brand using brands.md. If no brand is named, use an explicitly recorded project selection or ask whether to choose/onboard a pack or continue without one. Never select the first folder or infer a brand merely from the working directory. Show the Design Read and the inferred DESIGN_VARIANCE, MOTION_INTENSITY and VISUAL_DENSITY; accept conversational overrides.

For a new or materially revised direction, invoke Matt Pocock's `grilling` skill after gathering the available facts and before proposing concepts. Give it the website brief, project findings, brand constraints and the design decisions still open. Follow its design-tree rounds until the decision frontier is empty and the user confirms shared understanding. Ask the user for decisions, not facts the agent can inspect, and include a recommendation with each question. If the skill is unavailable, say so once and apply the same frontier method directly rather than making installation a blocker.

For an existing approved direction, skip grilling, concept generation and Stitch unless the change materially alters it. Apply only the relevant sections of Taste to a functional surface. The skill is not permission to redesign unrelated UI.

**Complete when:** scope, brand or explicit no-brand choice, content constraints and the three dials are clear; for a new direction, the grilling frontier is also resolved.

## 2. Choose a concept — first approval gate

For a new direction, propose two or three genuinely different concepts, not palette swaps. Use concise ASCII layouts or storyboards with desktop and mobile behaviour, the focal visual idea and the main trade-off. Reuse approved assets and describe missing ones honestly.

For significant narrative motion, read motion.md and include its key states. MotionSites is an optional source of references/prompts, not a mandatory subscription or runtime dependency. Do not copy reference sites or treat their promotional claims as acceptance evidence.

Present the concepts with a recommended choice and ask the user to select or revise one. Explain that this selects the direction to explore, not permission to build the production UI. Wait for their answer before generating the high-fidelity direction.

**Complete when:** the user has explicitly selected the concept.

## 3. Render and approve — second approval gate

Read stitch.md. Use Stitch by default for the new direction, unless the user explicitly chooses another available design tool. Claude Code's /design is not a dependency. Keep the handoff tool-neutral.

Produce desktop and mobile views with the same conceptual importance. A motion storyboard is sufficient when the behaviour is clear; make a disposable runnable prototype only for unresolved interaction behaviour. Keep it separate from production source and use clearly synthetic data where needed.

Store the selected artefacts and a concise DESIGN.md in the project's existing design area, or propose `docs/design/<surface>/` if none exists. Record the selected screen/project IDs, asset provenance, dials, semantic tokens, supported themes, responsive rules, motion and open limitations. Preserve unrelated design files; a root DESIGN.md may describe another surface.

Show the rendered direction, its interaction intent and known limitations. Follow stitch.md's human review handoff: give a usable preview/project link or screenshots, identify the screens to inspect and explain how the user can request or make changes. Ask for approval of a named version for implementation. Wait for their answer before production implementation. User edits to a design tool require fetching the latest selected artefacts, not assuming local code is current.

**Complete when:** the user approves an identifiable version of the package; unresolved issues that affect implementation are answered or explicitly deferred.

## 4. Implement

Read verification.md and define concrete checks before changing code. Reuse the current stack, components, semantic HTML, native CSS and existing dependencies. Add an animation library only when the approved behaviour needs it.

Treat imported HTML/CSS as design evidence, not mandatory production architecture. Keep the raw import unchanged while translating the selected design into maintainable project code. Extract shared tokens and components when they represent real shared meaning; avoid arbitrary line thresholds, all-values tokenisation, mandatory memoisation or new global state for convenience.

Read the bundled writing skill when creating or revising visible prose. Brand voice, market language and source integrity take precedence over its default register. Do not edit protected text or facts for visual fit. Use responsive layout or progressive disclosure instead.

Implement a small coherent change, run its focused check, fix failures and continue. Do not impose automatic commits or a 20-line deletion approval rule. Follow the project's existing mutation and commit policy.

## 5. Verify and deliver

Follow verification.md against the running implementation and approved package. Triage quiet detector findings without surrendering the design direction. A clean detector scan does not prove accessibility, visual parity or production readiness.

Report implemented scope, exact checks/results, evidence locations and remaining failures or untested conditions. Start the project's development server only when useful to the requested review; use its documented command and available port. Do not deploy, publish, spend on asset generation or install global tools merely because a template says to ship.
