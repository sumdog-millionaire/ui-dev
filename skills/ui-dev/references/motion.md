# Purposeful motion

Describe what motion communicates: hierarchy, narrative, feedback or state change. The approved direction determines the treatment; a numerical motion dial is not an instruction to animate every element.

## Evidence before implementation

For significant motion, describe trigger, moving subject, start/intermediate/end states, interruption/reverse behaviour, responsive geometry and reduced-motion alternative. A short storyboard at 0/25/50/100% progress is often sufficient. Build a disposable runnable prototype only when behaviour cannot be judged from it. Ordinary hover/focus feedback needs neither a storyboard nor a separate approval gate.

Static screens establish composition; a click-through flow establishes navigation. Neither alone demonstrates a working scroll-linked animation. Record what was actually observed.

## Scroll storytelling

Use normal document scrolling. Native sticky positioning holds a scene while its container's scroll distance advances the animation; the container ends naturally so following content remains reachable. Do not intercept wheel/touch input, trap scrolling or maintain an artificial locked/unlocked state. Keyboard, touch and scrollbar navigation must all work.

A travelling subject can follow different responsive paths while preserving its narrative on desktop and mobile. Derive geometry from actual containers, refresh after resize or asset layout changes, and clean up listeners/triggers. In GSAP, use function-based dimensions with refresh invalidation; do not cache travel distance only at mount.

Keep base content readable if enhancement fails. Reduced motion removes spatial travel, parallax and unnecessary pinning/delay while preserving the content and useful state changes. Repeated or long-running motion needs an appropriate pause/stop treatment.

## Tools

Use CSS transitions, sticky positioning, scroll snap and supported scroll-driven animations first. Use an existing animation library where suitable; Motion suits React state transitions and GSAP suits complex scroll timelines. A single library is not compulsory, but each animated property needs one owner. Avoid React state updates on every animation frame.

Use transform/opacity where they achieve the intended effect. Blur, large filters and canvas work need measured justification on target devices. Do not animate every section with identical blur/slide/scale treatments or delay essential content until an animation completes.

Pointer hover effects need a usable touch equivalent; core content cannot depend on hover. Native galleries and disclosure controls are preferable when they meet the design. Keep meaningful reading order and keyboard focus through animated changes.

## Text and facts

Preserve accessible reading and copying when splitting display text; visually animated spans must not create duplicate screen-reader content. Respect language-specific word segmentation and line breaking. Never count a price, date or other authoritative displayed fact from zero merely for decoration. Optional counters for appropriate marketing metrics must retain an accessible final value and honest data provenance.

Navigation must remain interruptible and reflect actual completion/state rather than a fixed timeout. Loading and animation failures must not strand the user behind an overlay.

## Brand artwork

Prefer supplied assets. Translating a logo along a path is different from deforming or redrawing it; check the pack and resolve material uncertainty before altering the mark. Keep any approved illustrative variant separate from the official logo. No particular brand, mascot or bird sequence is built into this skill.
