---
name: upstream-review
description: Review what has changed in the repositories this plugin took skills and text from (Taste, Emil Kowalski's skills, Impeccable, Google's Stitch skills) since each was last reviewed, and adopt the changes worth having into our customised copies. Use when the user asks to review, sync, upgrade or update the plugin's upstreams, or asks whether a source skill has moved on. Never replaces a file wholesale.
disable-model-invocation: true
---

# Upstream review

This plugin holds customised copies of other people's work, and the record of where each piece came
from is `upstream.json` at the plugin root. Each entry names a repository, the path inside it that
we took from, the commit last reviewed, which of our files carry the result, and notes on what was
adapted. The review walks that list, shows what has changed upstream since the reviewed commit, and
applies only what the user chooses. Our copies carry local edits on purpose, so a change is always
merged into them, never pasted over them.

## 1. Fetch, read-only

For each entry, clone the repository shallowly into a temporary folder outside the plugin
(`git clone --depth 200` is enough to reach the reviewed commit; deepen if it is not there), and
resolve the default branch rather than assuming its name. Nothing in the plugin is touched in this
step. Record the fetched head commit and date.

Diff `sourcePath` and every `alsoWatch` path between `reviewedCommit` and the head. Read each changed
section in context, including removed text and changed code examples, because a removal upstream
is often the most useful signal. Check the licence file for changes too.

## 2. Table the changes

Show one table per upstream, one row per distinct change:

| Upstream change | Where in ours | Recommendation | Reason |
|---|---|---|---|
| what changed, with the upstream file and section | the file of ours it would touch, or "not carried" | adopt, adapt or skip | the benefit, and any local decision it collides with |

Recommend with a reason every time. A change that contradicts a decision recorded in the entry's
`reviewNotes` is recommended as skip with that decision named, so the user can overrule it knowingly.
Then wait for the user's choices. A request to review is not permission to apply.

## 3. Apply what was chosen

Apply each chosen change to our copy by hand, comparing three things: the reviewed upstream version,
the new upstream version, and ours. Keep every local edit that the change does not deliberately
replace. For a vendored skill (Emil Kowalski's), re-run the em-dash strip afterwards, since upstream
text carries them and the house rule does not:

```powershell
python skills/upstream-review/scripts/strip-em-dashes.py skills/<name>
```

For text that was lifted rather than vendored (Impeccable, Google's Stitch skills), rewrite the
passage in the voice of the file it lives in; the reference files carry no lineage, only what an
agent needs to act.

## 4. Check, then record

Run the plugin's checks before recording anything: `claude plugin validate . --strict` from the
plugin root, a search for em dashes across `skills/`, and a read of every description that changed,
to confirm no two skills now trigger on the same phrase. If a check fails, fix it or leave the
entry's `reviewedCommit` where it was and say the review is incomplete.

Only when the checks pass, set the entry's `reviewedCommit` to the fetched head and rewrite its
`reviewNotes` to say what was adopted, adapted and skipped in this review. Record the skipped changes
too, so the next review does not propose them again. Show the final diff. Commit only if the user
asks, with a message that says which upstream moved and what was taken.
