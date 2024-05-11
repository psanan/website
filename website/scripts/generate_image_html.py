#!/usr/bin/env python
"""Generate image HTML."""

import argparse
import os
import subprocess

import html_utils
import utils

THIS_DIR = os.path.dirname(os.path.realpath(__file__))
IMAGES_DIR_PREFIX = os.path.join(THIS_DIR, "..")
IMAGES_DIR = os.path.join(IMAGES_DIR_PREFIX, "site", "images")
IGNORE_FILES = [".DS_Store", utils.SMALL_DIRNAME]


def _grid_html(directory, base_directory_prefix):
    if not os.path.isdir(directory):
        raise Exception(f"{directory} is not a directory")
    print('<div class="grid-container">')
    for filename in sorted(os.listdir(directory)):
        path = os.path.join(directory, filename)
        if os.path.isdir(path) or filename in IGNORE_FILES:
            continue
        print("".join(html_utils.figure_grid_html_lines(path, base_directory_prefix)),
              end="")
    print('</div> <!--grid-container-->')


def grid_main():
    demo_post_name = "swiss-cantonal-highpoints"
    demo_dir = os.path.join(IMAGES_DIR, demo_post_name)
    description = f"""Prepares files and prints HTML to use an image dir in a post. E.g
    mkdir -p {demo_dir}
    cp img1.jpg {demo_dir}
    # Pipe output to macOS clipboard
    python {__file__} -q {demo_post_name} | pbcopy"""
    parser = argparse.ArgumentParser(
        description=description,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--quick-directory', '-q', required=True)
    parser.add_argument('--generate', action='store_true')
    parser.add_argument('--no-generate', dest='generate', action='store_false')
    parser.set_defaults(generate=True)
    args = parser.parse_args()

    directory = os.path.join(IMAGES_DIR, args.quick_directory)

    if args.generate:
        utils.create_small_images(directory)

    _grid_html(directory, IMAGES_DIR_PREFIX)


if __name__ == "__main__":
    grid_main()
