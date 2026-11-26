#!/usr/bin/env python3
"""Deliver the news-image entry for 25 November 2026.

This program is the entrypoint of the make.fun bounty
"Sum up 25 November's world news in one image". It takes the
pre-rendered front-page image that ships beside this file and
places a copy in the harness output directory. Nothing is
downloaded and nothing is generated at run time: the image is
already in the repository, so every run produces the same bytes.

Standard library only.
"""

from pathlib import Path
import os
import shutil
import sys


def locate_source() -> Path:
    """Return the path of the entry image next to this program."""
    here = Path(__file__).resolve().parent
    return here / "entry.png"


def output_directory() -> Path:
    """Return the harness output directory, creating it if needed."""
    target = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target.mkdir(parents=True, exist_ok=True)
    return target


def main() -> None:
    source = locate_source()
    if not source.is_file():
        sys.exit(
            f"entry.png missing: looked for {source} "
            "(the image must sit beside this program)"
        )
    destination = output_directory() / "entry.png"
    shutil.copyfile(source, destination)


if __name__ == "__main__":
    main()
