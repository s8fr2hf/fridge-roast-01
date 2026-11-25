"""Fridge Roast: One Line, Biggest Laugh.

Writes a single original line (at most 200 characters) roasting a smart
fridge to entry.txt in the output directory.

Pure Python standard library. The output directory is MAKEFUN_OUTPUT_DIR
when set, otherwise /output.
"""

import os

LINE = (
    "My smart fridge pushed a firmware update overnight, and now the ice "
    "maker only works if I agree to the new terms \u2014 the milk expired, "
    "but the EULA is forever."
)

MAX_CHARS = 200


def main() -> None:
    line = LINE.strip()
    if not line:
        raise SystemExit("entry line is empty")
    if len(line) > MAX_CHARS:
        raise SystemExit(
            "entry line is %d characters, over the %d limit"
            % (len(line), MAX_CHARS)
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
