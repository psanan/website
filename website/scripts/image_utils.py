#!/usr/bin/env python
"""Utilities to work with images"""

import os
import subprocess

from utils import eprint

SMALL_DIRNAME = "small"
IGNORE_FILES = [".DS_Store", SMALL_DIRNAME]

THIS_DIR = os.path.dirname(os.path.realpath(__file__))
IMAGES_DIR_PREFIX = os.path.join(THIS_DIR, "..")
IMAGES_DIR = os.path.join(IMAGES_DIR_PREFIX, "site", "images")


def figure_small_path(path):
    """Returns the small-image path corresponding to a given image or directory."""
    if os.path.isdir(path):
        return os.path.join(path, SMALL_DIRNAME)
    return os.path.join(os.path.dirname(path), SMALL_DIRNAME,
                        os.path.basename(path))


def create_small_images(directory):
    """Use Imagemagick to create small versions of images in a directory."""
    small_directory = figure_small_path(directory)
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
            eprint(
                f"Warning! Unexpected small file {filename} found in {small_directory}"
            )
    if expected_filenames:
        eprint(f"ERROR! {small_directory} is missing {expected_filenames}")
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
    small_path = figure_small_path(path)

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
