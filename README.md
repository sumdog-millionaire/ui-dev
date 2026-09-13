# ui-dev

A Claude Code plugin for designing and building interfaces: web pages, web apps, and the phone and
native surfaces beside them. One design skill routes the work by what the visitor is there to do,
hands motion to Emil Kowalski's skills, drives Google Stitch through its MCP server, and runs the
Impeccable detector quietly after every edit.

This folder is the source. It is a git repository (`sumdog-millionaire/ui-dev`) installed in place at
`~/.claude/skills/ui-dev/`, which Claude Code loads as a plugin on every session, hooks included.
Edit here, commit here, push here. A second machine clones it to the same path.

## What is in it

| Path | Holds |
|---|---|
| `skills/ui-dev/` | the design skill: a short body that reads the brief and picks a mode, plus references loaded on demand (workflow, brands, the modes, Stitch, the design file, verification, styles, patterns, redesign, design systems, motion skeletons) |
| `skills/animate`, `animate-expo`, `review-animations`, `improve-animations`, `pick-ui-library`, `prototype`, `apple-design`, `write-swift` | Emil Kowalski's skills, vendored; `ui-dev` hands all interface motion to `animate` |
| `skills/upstream-review/` | the maintenance skill: walks `upstream.json`, diffs each source since the reviewed commit, proposes adopt, adapt or skip |
| `hooks/`, `scripts/` | the Impeccable detector adapter: a PostToolUse check after every Edit or Write, a deeper pass at the end of a turn |
| `extensions/` | the same adapter for Pi |
| `upstream.json` | every source this plugin took text or files from, with the commit last reviewed |

## Install on a machine

```powershell
git clone https://github.com/sumdog-millionaire/ui-dev.git "$HOME/.claude/skills/ui-dev"
cd "$HOME/.claude/skills/ui-dev"
npm ci --omit=dev          # the pinned Impeccable detector binary; Node 22.18 or newer
copy .env.example .env     # then put the Stitch API key in it (used only by the upload script)
```

Restart Claude Code. The plugin appears as `ui-dev@skills-dir`; `/ui-dev:ui-dev` starts design work
and `/ui-dev:upstream-review` runs the maintenance pass.

### Companions, not bundled

`ui-dev` calls these by name when they are installed and says so when they are not:

- **grilling** (Matt Pocock's plugin): resolves the design decisions for a new direction.
- **anti-ai-slop-writing** (`~/.claude/skills`): the writing standard for anything a person reads.
- Four of Google's Stitch skills, copied into `~/.claude/skills/` from
  `google-labs-code/stitch-skills`: `extract-static-html` (capture a running screen as one HTML file),
  `upload-to-stitch` (post images and HTML to Stitch over REST), `extract-design-md` (read a
  DESIGN.md out of existing source), `react-components` (turn a Stitch screen into React). Their
  own confirmation gates and folder conventions do not apply; `ui-dev`'s do.

### Stitch

Create an API key in Stitch settings, then:

```powershell
claude mcp add stitch --transport http https://stitch.googleapis.com/mcp --header "X-Goog-Api-Key: <key>" -s user
```

The same key goes in `.env` for the upload script. Nothing here stores it anywhere else.

## The detector

The hooks run Impeccable's detector (npm `impeccable`, pinned in `package.json`) on every Edit or
Write of a UI file and once more when a turn ends. Clean results are silent; findings reach the agent
with the command to record a narrow exception. The end-of-turn pass blocks the turn until findings
are dealt with, and never blocks on a repeated stop or on a fault in the engine itself. Project
settings in `.impeccable/config.json` are respected and never rewritten.

Run it by hand from the project being checked:

```powershell
node "$HOME/.claude/skills/ui-dev/scripts/impeccable.ts" detect frontend/
```

## Keeping up with upstream

`/ui-dev:upstream-review` fetches each repository in `upstream.json`, shows what changed in the
watched paths since the commit last reviewed, and waits for a choice per change. Nothing is
replaced wholesale; vendored copies keep their local edits, and the skill's own em-dash strip is
re-run on anything re-synced.

## Attribution

Taste by Leonxlnx (MIT, `LICENSE`), Emil Kowalski's skills (MIT), Impeccable by Paul Bakaus
(Apache 2.0, used as a pinned executable), and Google's Stitch skills (Apache 2.0). Commits reviewed
are in `upstream.json`.
