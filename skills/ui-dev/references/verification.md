# Implementation and verification

Define success against the approved package before production edits. Use the project's own build, lint, type-check and test commands. Run focused checks as each change is made and the relevant combined checks at the end.

## Quiet detector hooks

ui-dev integrates the pinned Impeccable executable only. No Impeccable skill, creative router or manual audit skill is required. Claude Code uses plugin hooks; Pi uses an event adapter. Both scan direct successful file edits and perform a deferred deep pass. Clean acknowledgements are suppressed; findings still reach the agent.

Use the runtime's reported CLI command to manage narrow exceptions. Do not invoke an unavailable `/impeccable` skill or install its skills to resolve a finding.

- A real problem: fix it and rerun the relevant check.
- A confident false positive or approved aesthetic: record the narrowest value/file-scoped exception, with the actual evidence and reason; disclose it. Do not claim approval that was never given.
- An uncertain finding: leave it visible and ask a targeted question.

Whole-rule or whole-file suppression needs explicit approval. Do not disable checks to make a result green. Existing unrelated detector configuration must not be overwritten. A DESIGN.md belonging to another surface is not this surface's authority; resolve that mismatch before accepting drift suggestions. The integration does not generate an Impeccable design-system sidecar automatically.

Direct edit hooks do not guarantee coverage of shell writes, external generators or every file in a large repository. Finish with an explicit detector scan of all changed UI files, including shell-generated files. Use the installed CLI's `detect --help` for its current arguments. Hook silence alone is not scan evidence; missing executable, timeout or scan failure must be reported as an unperformed check.

## Browser evidence

Use an available real browser tool and the project's development server. Test at least a narrow phone, a larger phone, tablet and desktop; 375, 430, 768 and 1280 CSS pixels are useful starting points, not exhaustive support claims. Also inspect a short/landscape viewport and widths around layout changes. Compare screenshots against the selected design views.

Check:

- Required content, source facts, navigation and primary tasks remain correct. Exercise long text, empty/loading/error states and realistic item counts.
- Desktop and mobile preserve the approved concept; touch does not rely on hover. No accidental overflow or clipped text. Check zoom/reflow, not just named breakpoints.
- Keyboard order, visible focus, native semantics and accessible names work. Use visible labels rather than adding aria-label indiscriminately. Decorative images have empty alt; informative ones have meaningful descriptions. Dialog focus enters, stays appropriately contained, closes with the expected controls and returns correctly.
- Text contrast meets WCAG AA: 4.5:1 normally, 3:1 for large text (24 CSS px regular or approximately 18.7 px bold). Check controls/focus indicators and text over imagery. Aim for 44x44 CSS pixel touch targets where practical; report the actual tested accessibility criteria.
- Reduced motion is tested, not merely implemented. No compulsory delay, scroll trap or inaccessible content remains. Test reversing/interrupting motion, resizing, failed animation and slow/broken images.
- Every supported theme works. A missing brand dark theme is not a ban; an unrequested theme is not a required implementation.
- Images reserve layout space; off-screen assets load appropriately without delaying the main image. Inspect console errors, network failures and build output.
- Measure performance in a stated environment. Lighthouse/lab results are useful, but do not prove real-user INP or universal device performance. Investigate expensive filters, oversized media and heavy animation bundles.

## Completion

Record exact commands, tested browser conditions, screenshot/evidence paths and unresolved failures. Use pass, fail, not applicable and not checked honestly. Missing browser access blocks a claim of visual verification; do not replace it with source inspection. Never force every checklist entry to green or describe generated code as production-ready without the required evidence.
