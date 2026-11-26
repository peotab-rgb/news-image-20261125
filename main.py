#!/usr/bin/env python3
"""Entry program for news-image-20261125 (Python 3, standard library only).

Copies the entry image that sits beside this file into the output
directory requested by the harness (MAKEFUN_OUTPUT_DIR, else /output).
No network access, no extra dependencies.
"""
import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.isfile(src):
        sys.exit(f"entry.png missing: looked for {src}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
