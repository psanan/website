#!/usr/bin/env python
"""Updates HTML source."""

# TODO for release
# - Refactor so all HTML-heavy stuff is in html_utils, move imagemagick to utils.py and get rid of image_utils.py
# - Scan through carefully for confusing things, unneccessary complexity, etc.
# - Look for stuff to delete or shrink
# - pass pylint (and YAPF google style) perfectly
# - squash to a new main branch (back up old history locally I guess)
# - make public

import argparse
import os
import re
import sys

import utils
from html_utils import *

def _update_directory(directory):
    """Updates all HTML files in a directory. Returns if anything changed."""
    if not os.path.isdir(directory):
        raise Exception(f"{directory} is not a directory")
    anything_changed = False
    skipped_filenames = []
    print(f"Updating HTML in {directory}:")
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        path = os.path.join(directory, filename)

        # Proceed somewhat inefficiently, opening and overwriting
        # the file several times.
        if should_skip(path):
            skipped_filenames.append(filename)
            continue
        print(f"  {filename}")
        if update_header_and_footer(path):
            anything_changed = True
        if update_figures(path):
            anything_changed = True

    if skipped_filenames:
        print("Skipped the following files:")
        for filename in skipped_filenames:
            print(f"  {filename}")

    return anything_changed


def main():
    description = """Updates HTML and returns a non-zero exit code if anything changed."""
    parser = argparse.ArgumentParser(
        description=description,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser = argparse.ArgumentParser()
    parser.add_argument('--directory', '-d', default=DEFAULT_SITE_PATH)
    args = parser.parse_args()

    return _update_directory(args.directory)


if __name__ == "__main__":
    sys.exit(1 if main() else 0)
