#!/usr/bin/env python
"""Utilities to work with images"""

import argparse
import os
import sys
import subprocess

# Non-image files which might unavoidable be found in an images directory
SMALL_DIRNAME = "small"
IGNORE_FILES = [".DS_Store", SMALL_DIRNAME]


def _get_small_path(path):
    """Returns the small-image path corresponding to a given image or directory."""
    if os.path.isdir(path):
        return os.path.join(path, SMALL_DIRNAME)
    else:
        return os.path.join(os.path.dirname(path), SMALL_DIRNAME, os.path.basename(path))


def _eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


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
        _eprint(f"Info: Generating {small_path}")
        subprocess.run(["convert", "-resize", "300x300>", path, small_path])
        expected_filenames.add(filename)
    for filename in os.listdir(small_directory):
        if filename in IGNORE_FILES:
            continue
        if filename in expected_filenames:
            expected_filenames.remove(filename)
        else:
            _eprint(
                f"Warning! Unexpected small file {filename} found in {small_directory} (perhaps you want to delete and regenerate small images manually)"
            )
    if expected_filenames:
        _eprint(
            f"ERROR! all expected small files not found in {small_directory}. Missing {expected_filenames}"
        )
    return small_directory


def figure_grid_html(input_path, base_directory_prefix):
    """Produce an html figure snippet for a given image within a grid.

    Includes paths relative to the provided base_directory prefix."""
    if base_directory_prefix:
        path = input_path.removeprefix(base_directory_prefix).removeprefix(
            os.sep)
    else:
        path = input_path
    small_path = _get_small_path(path)

    lines = []
    lines.append(f'<div class="grid-item">')
    lines.append(f'<figure>')
    lines.append(f'<a href="{path}">')
    lines.append(f'<img src="{small_path}" alt=""/>')
    lines.append(f'</a>')
    lines.append(f'<figcaption></figcaption>')
    lines.append(f'</figure>')
    lines.append(f'</div>')
    return '\n'.join(lines)


def grid_html(directory, base_directory_prefix):
    if not os.path.isdir(directory):
        raise Exception(f"{directory} is not a directory")
    print('<div class="grid-container">')
    for filename in sorted(os.listdir(directory)):
        path = os.path.join(directory, filename)
        if os.path.isdir(path) or filename in IGNORE_FILES:
            continue
        print(figure_grid_html(path, base_directory_prefix))
    print('</div>')


def grid_main():
    """Prepares files and prints HTML to use an image dir in a post.

    Typical usage is e.g.
       ./image_utils.py -d ../site/images/foo -p ../site | pbcopy
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--directory', '-d', required=True)
    parser.add_argument('--prefix-directory', '-p', default="")
    parser.add_argument('--generate', action='store_true')
    parser.add_argument('--no-generate', dest='generate', action='store_false')
    parser.set_defaults(generate=True)
    args = parser.parse_args()

    if args.generate:
        create_small_images(args.directory)
    grid_html(args.directory, args.prefix_directory)


if __name__ == "__main__":
    grid_main()
