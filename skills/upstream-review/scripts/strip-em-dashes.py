"""Replace em dashes in the vendored skills, so a re-sync from upstream keeps the house rule."""

import re
import sys
from pathlib import Path

# A spaced dash becomes a comma; an unspaced one becomes a spaced hyphen, which reads as a dash
# without teaching the habit. Inside a code fence only comment lines are touched, since a dash in
# code itself is content.
SPACED = re.compile(r"\s+[—–]\s+")
BARE = re.compile(r"[—–]")
COMMENT = re.compile(r"//|/\*|^\s*#")


def strip(text: str) -> str:
    """Return the text with every em or en dash in prose or code comments replaced."""
    out = []
    in_fence = False
    for line in text.splitlines(keepends=True):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
        if in_fence and not COMMENT.search(line):
            out.append(line)
            continue
        line = SPACED.sub(", ", line)
        line = BARE.sub(" - ", line)
        out.append(line)
    return "".join(out)


def main(roots: list[str]) -> None:
    """Rewrite every markdown file under the given folders, printing the count changed."""
    changed = 0
    for root in roots:
        for path in Path(root).rglob("*.md"):
            before = path.read_text(encoding="utf-8")
            after = strip(before)
            if after != before:
                # Keep the file's line endings as they were; git normalises the rest.
                path.write_text(after, encoding="utf-8", newline="")
                changed += 1
    print(f"{changed} files changed")


if __name__ == "__main__":
    main(sys.argv[1:])
