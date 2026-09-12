# ui-dev

A reusable Taste-based design and implementation workflow for Claude Code and Pi. It supports websites and web applications, with stylistic intensity adapted to the task, local brand packs, Stitch exploration and quiet Impeccable detector checks.

One maintained repository supplies two skills and two small agent integrations. It does not install Impeccable's skills, require Claude's /design command or automatically connect external services.

## What is shared

- **ui-dev:** discovery, brand onboarding, concepts, human approval, Stitch handoff, implementation and browser verification.
- **anti-ai-slop-writing:** Benedict's writing guidance, used when authoring visible prose; the selected brand voice and market conventions take precedence.
- **Grilling:** Matt Pocock's separately installed skill is invoked to resolve design decisions for new or materially revised directions. It is not bundled; ui-dev applies the same design-tree method directly if unavailable.
- **Impeccable CLI:** one pinned detector used by both integrations. Claude uses native plugin hooks; Pi uses an extension that translates its events into the detector's protocol.

The source retains `skills/taste-skill/` to make upstream comparisons straightforward. Its declared skill name is `ui-dev`; the generated distribution also names the folder `skills/ui-dev/`. Other upstream skills remain in the source repository for reference but are not shipped or loaded by the Pi package manifest.

## Build and check

Node.js 22.18 or newer is required. From the maintained repository:

```powershell
npm ci
npm test
npm run check
npm run build
claude plugin validate ./dist/ui-dev --strict
```

`dist/ui-dev/` is generated output containing only the intended skills, scripts and metadata. Rebuilding replaces that directory. Never make maintained edits there.

The generated package can also be copied to a separate location. In that location, run `npm ci --omit=dev` before loading it. This installs the executable dependency, not any Impeccable skills. Dependency installation is explicit; hooks do not run an installer on every edit. The upstream CLI shim may fetch a checksum-verified platform binary if its optional platform package is unavailable.

## Claude Code

Load the generated plugin for a session:

```powershell
claude --plugin-dir "C:/Users/BenedictS/code/ui-dev/dist/ui-dev"
```

Then invoke:

```text
/ui-dev:ui-dev Design a website for <brand>.
```

The plugin exposes `ui-dev` and `anti-ai-slop-writing`, plus PostToolUse and Stop hooks. Do not load the source repository root with `--plugin-dir`: Claude would discover the optional upstream skills still held there. No marketplace or global installation is required for this local workflow.

For persistent loading on Claude Code versions supporting skills-directory plugins, place the prepared generated package under `~/.claude/skills/ui-dev/` and restart. This is a copy: rebuild and replace it deliberately when upgrading. Keep your maintained Git repository separate from the installed copy.

## Pi

Install the maintained local package:

```powershell
pi install "C:/Users/BenedictS/code/ui-dev"
```

Start a new session or reload resources, then invoke:

```text
/skill:ui-dev Design a website for <brand>.
```

Pi's package manifest selects only the two intended skills and the detector extension. A generated standalone package works too: install that directory after its dependencies are installed. Local installs reference the directory rather than copying it.

If the original writing skill is already discovered separately, avoid loading duplicate copies. Pi reports name collisions and keeps the first discovered skill. Select one source through Pi's resource configuration; in Claude, avoid invoking a separate original copy for ui-dev work. Nothing here disables or removes your existing skills automatically.

## Stitch and browser access

Set up an authenticated Stitch MCP connection in each agent using https://stitch.withgoogle.com/docs/mcp/setup/. Claude Code uses its MCP support; Pi needs an MCP adapter such as the one already used in Benedict's environment. Reuse an existing connection rather than adding a duplicate. This package does not store credentials or install an MCP adapter.

The skill discovers available tools and verifies access by listing projects. For each new or materially revised direction, it writes the exact generated prompt to `docs/design/<surface>/stitch-brief.md`, submits that prompt through MCP and records the returned project/screen identifiers. You review the resulting design rather than manually recreating the prompt in Stitch.

If a connection or human-only action is missing, the skill explains what you need to do, where to do it and what to return. Browser automation must also be available for rendered verification. Missing access is reported, not silently replaced with a claim of success.

## Brand packs and collaboration

Both agents use the same default local library:

```text
~/.claude/brands/<brand>/
  BRAND.md
  sources/
  assets/logos/
  assets/fonts/
  assets/images/
  assets/icons/
```

Only create folders that contain material. The location is a shared local convention, not a Claude dependency; an explicitly supplied library path can override it. Original sources remain unchanged. The agent extracts a sourced profile, identifies unknowns and asks for approval before first use. Missing guidance permits project-specific design choices, including dark themes; it is not a blanket prohibition.

For a missing brand, the skill offers onboarding or an explicitly unbranded direction. For a new design, you choose a concept and later approve a named rendered package before production implementation. Each handoff states what is ready, what you must decide/do, the relevant project/screens and what to return. The agent does work its tools permit; it does not send you into Stitch unnecessarily. Small changes within an approved direction skip concept generation and Stitch.

## Automatic checks

Clean acknowledgements are quiet. Findings still reach the agent. Direct successful edits trigger checks; broader findings are deferred until completion. The adapters preserve source tool output and bound automatic completion follow-ups. An aesthetic finding does not overrule an approved brand or design.

Run the packaged CLI from the project being checked:

```powershell
node "C:/Users/BenedictS/code/ui-dev/scripts/impeccable.ts" detect --help
node "C:/Users/BenedictS/code/ui-dev/scripts/impeccable.ts" hooks status
```

Use the actual package path; findings also print executable exception commands. Record narrow exceptions with evidence. Do not run `impeccable install`, `update` or `hooks on` to wire this integration: those commands manage upstream skill installations and manifests, not ui-dev's adapters.

Hooks are active wherever the plugin/package is enabled, not only after manually invoking the skill. Existing `.impeccable/config.json` settings and upstream disable flags are respected. Disable ui-dev's extension/plugin through the agent's normal resource controls when unwanted. No Impeccable configuration is overwritten automatically.

Limitations: direct edit hooks do not cover arbitrary shell writes; a final explicit scan of all changed UI files is still required. Upstream also bounds findings/files and can suppress repeated edits. The detector is not a browser, an accessibility certification or evidence of production readiness. Missing binaries and adapter errors are reported as incomplete checks. Brand design-system sidecars are not generated automatically.

## Upstream upgrades

Ask: **“Review upstream Taste changes for ui-dev.”** The skill follows `references/upgrades.md`: locate the maintained repository, fetch without touching working files, compare with `upstream.json`, recommend adopt/adapt/skip, wait for your selection and apply targeted changes. It then checks the result and records the reviewed commit. It does not overwrite the customised skill or install optional upstream skills.

The configured `upstream` remote is https://github.com/Leonxlnx/taste-skill.git. A package-manager update retrieves a maintained ui-dev version; it is not the selective Taste review procedure. Do not customise installer-managed caches that updates can replace.

## Verification scope

Automated tests exercise the real pinned detector in temporary projects without Impeccable skill folders, immediate/deferred/quiet behaviour, adapter response formats, the generated package and Pi's actual resource loader. TypeScript and Claude's plugin validator provide additional structural checks.

These checks do not establish live model behaviour, authenticated Stitch access, a complete design/build session or rendered website quality. A full model evaluation run was deliberately not performed. No package was enabled globally during development.

## Attribution

Taste source and history: https://github.com/Leonxlnx/taste-skill. Its original MIT licence and copyright are retained in LICENSE. The selected upstream baseline is recorded in upstream.json. The writing skill is copied from Benedict's local anti-ai-slop-writing skill, with brand-precedence integration; do not imply it is part of upstream Taste.

Impeccable: https://github.com/pbakaus/impeccable, used as an Apache-2.0 executable dependency rather than a copied detector or skill collection. This is ui-dev's integration, not an upstream-supported hooks-only installer.

Claude plugin documentation: https://code.claude.com/docs/en/plugins

Pi packaging: https://github.com/earendil-works/pi-mono/tree/main/packages/coding-agent/docs/packages.md

Google Labs Stitch workflow references and the originating reel/prompt are linked in `skills/taste-skill/references/stitch.md`. The reel is inspiration, not verification evidence.
