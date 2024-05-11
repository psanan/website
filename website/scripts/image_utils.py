#!/usr/bin/env python
"""Utilities to work with images"""

import argparse
import os
import sys
import subprocess

from utils import eprint

SMALL_DIRNAME = "small"
IGNORE_FILES = [".DS_Store", SMALL_DIRNAME]

THIS_DIR = os.path.dirname(os.path.realpath(__file__))
IMAGES_DIR_PREFIX = os.path.join(THIS_DIR, "..")
IMAGES_DIR = os.path.join(IMAGES_DIR_PREFIX, "site", "images")


def _get_small_path(path):
    """Returns the small-image path corresponding to a given image or directory."""
    if os.path.isdir(path):
        return os.path.join(path, SMALL_DIRNAME)
    return os.path.join(os.path.dirname(path), SMALL_DIRNAME,
                        os.path.basename(path))




def create_small_images(directory):
    """Use Imagemagick to create small versions of images in a directory."""
    small_directory = _get_small_path(directory)
    if not os.path.exists(small_directory):
        os.makedirs(small_directory)
    expected_filenames = set()
    for filename in sorted(os.listdir(directory)):
        path = os.path.join(directory, filename)
        if os.path.isdir(filename) or filename in IGNORE_FILES:
            continue
        small_path = os.path.join(small_directory, filename)
        # Use Imagemagick's "convert" to
        # resize the largest dimension to 300px
        eprint(f"Info: Generating {small_path}")
        subprocess.run(["convert", "-resize", "300x300>", path, small_path],
                       check=True)
        expected_filenames.add(filename)
    for filename in os.listdir(small_directory):
        if filename in IGNORE_FILES:
            continue
        if filename in expected_filenames:
            expected_filenames.remove(filename)
        else:
            _eprint(
                f"Warning! Unexpected small file {filename} found in {small_directory}"
            )
    if expected_filenames:
        _eprint(f"ERROR! {small_directory} is missing {expected_filenames}")
    return small_directory


def figure_grid_html_lines(input_path,
                           base_directory_prefix,
                           alt="",
                           caption=""):
    """Produce an HTML figure snippet for a given image within a grid.

    Includes paths relative to the provided base_directory prefix."""

    if base_directory_prefix:
        path = input_path.removeprefix(base_directory_prefix).removeprefix(
            os.sep)
    else:
        path = input_path
    small_path = _get_small_path(path)

    # default caption to make it easier to write real captions
    if not caption:
        caption = path

    lines = []
    lines.append('<div class="grid-item">\n')
    lines.append('<figure>\n')
    lines.append(f'<a href="{path}">\n')
    lines.append(f'<img src="{small_path}" alt="{alt}"/>\n')
    lines.append('</a>\n')
    lines.append(f'<figcaption>{caption}</figcaption>\n')
    lines.append('</figure>\n')
    lines.append('</div> <!--grid-item-->\n')
    return lines


def _grid_html(directory, base_directory_prefix):
    if not os.path.isdir(directory):
        raise Exception(f"{directory} is not a directory")
    print('<div class="grid-container">')
    for filename in sorted(os.listdir(directory)):
        path = os.path.join(directory, filename)
        if os.path.isdir(path) or filename in IGNORE_FILES:
            continue
        print("".join(figure_grid_html_lines(path, base_directory_prefix)),
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
        create_small_images(directory)

    _grid_html(directory, IMAGES_DIR_PREFIX)


if __name__ == "__main__":
    grid_main()
