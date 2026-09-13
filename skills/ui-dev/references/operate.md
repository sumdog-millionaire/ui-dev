# Operate

Read when the design read picks operate: app UI, dashboards, editors, admin, settings, tools, data
tables, authenticated surfaces, anything where the person is in a task. Familiarity is a feature.
Avoid strangeness without purpose: over-decorated buttons, mismatched controls, gratuitous motion,
display fonts where labels should be, invented affordances for standard tasks.

## Space

- Measure the element, never the window.
- Predictable structure, stable density and navigable linearity are affordances. Standard navigation patterns belong here: top bar plus side navigation, breadcrumbs, tabs, a command palette.
- Density is permitted: tables with many rows, panels with many labels, dense information when the task needs it. Data and compact UI can run denser than prose; a table at 120 characters wide is fine.
- Responsive behaviour is structural (collapse the sidebar, reflow the table, change the column count), not fluid typography. At desktop: side navigation visible, several panels at once, hover for additional information, keyboard shortcuts, context menus, drag and drop where it helps, multi-select with modifier keys.
- Repetition supports recognition; break it only when content or priority changes. Related items sit close and distinct groups sit apart, so containers are not compensating for weak proximity.
- Overlays escape their container: a dropdown positioned inside an ancestor with overflow hidden gets clipped, so reach for `<dialog>`, the popover API, `position: fixed`, or a portal.

## Type and colour

- One family is often right; a well-tuned sans carries headings, buttons, labels, body and data. A fixed rem scale with a tighter ratio (1.125 to 1.2 between steps), never fluid headings that shrink inside a sidebar.
- Colour defaults to restrained. Accent for primary actions, current selection and state indicators; a second neutral layer for sidebars, toolbars and panels. Inactive states never carry heavy or full-saturation colour.

## Labels, copy and tooltips

- Labels are factual, and every word earns its place. A title says what the thing is, plainly; an extra word stays only when it changes the meaning ("Your compass": yours, not the project's) and goes when it is only warmth ("Today's use" becomes "Usage"). Whatever fact the label needed that word for goes under it, smaller, as a clarification ("Resets at 00:00 UTC").
- Every control and every folder explains itself on hover. A list row is one line; its detail is the tooltip; the list's mechanics are said once on its header. On a touch surface the same detail is reachable by a press or an expanded row; when the surface is also the phone, which of those is a question for the round.
- Say a thing once per surface, where it is first met and seen on arrival, not at the end of a scroll or below a fold. Repeat only what answers "what do I do next?" or "what is this?". A page that lists many of the same thing carries the line once, for the page, not under every row.
- Actions use a specific verb and object when the outcome is not obvious; the same noun and verb for the same concept everywhere. A destructive action names the object and the consequence; prefer undo to confirmation when recovery is safe, and when confirmation is necessary the button names the action rather than "Yes", "OK" or "Submit".
- An error says what failed, why when that is known and useful, and how to recover; never an internal code as the message; never a promised cause the system cannot know.
- Loading text names the real operation; determinate progress when it is available, never invented. Success confirms the outcome briefly and mentions a next consequence only when it changes what the person should do.

## States

- Visible keyboard focus, logical tab order, labels, and platform-sized touch targets on every control.
- Skeletons for loading, matching the layout; loading is separate for the initial load, pagination and refresh. Large datasets paginate or virtualise. Concurrent operations disable while in flight, or update optimistically with rollback.
- An empty state distinguishes first use, cleared by the user, no results, filtered to nothing, no permission, and failure. Each says what will be here, why it matters, and gives the next useful action.
- Permission states show what is unavailable and why, not a blank.

## Cognitive load

- Single focus: the primary task completes without competing elements.
- Chunking: information in groups of at most four; decisions with at most four visible options, the rest in a menu. Action buttons: one primary, one or two secondary, the rest grouped. Navigation menus: at most five top-level items.
- One thing at a time; progressive disclosure reveals complexity only when needed.
- Working memory: the current screen never needs a fact remembered from a previous one.
- Match neighbouring mental models: terminology, disclosure, routing, save behaviour, optimistic or pessimistic patterns, all the same screen to screen.

## Motion and delight

Motion conveys state, feedback, loading and reveal; routine transitions stay fast and there is no
page-load choreography. A control used a hundred times a day gets none. Delight concentrates at the
meaningful moments, first use, completion, recovery, mastery, and matches the effort and
consequence. Never fake work or delay completion to stage a flourish. `animate` writes whatever
moves.

## Affordances

Standard affordances rather than reinvented ones (custom scrollbars, odd form controls,
non-standard modals are strangeness without purpose); a modal only when a task needs interruption
or protected focus, with inline and progressive alternatives exhausted first; consistency over
surprise, screen after screen.

## Triage when polishing

1. Broken or blocked tasks, data loss, misleading state, inaccessible paths.
2. Missing loading, empty, error, success, disabled and permission states.
3. Flow, hierarchy, responsive and design-system drift.
4. Visual and motion inconsistencies.
5. Code and asset clean-up.

Never perfect one corner while the rest sits below the same bar.
