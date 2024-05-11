"""Utility functions not directly related to HTML processing"""

import datetime
import os
import subprocess
import sys

SMALL_DIRNAME = "small"
IMAGE_DIR_IGNORE_FILES = [".DS_Store", SMALL_DIRNAME]


def copyright_string(html=True):
    """Produces a copyright string, with an option for HTML."""
    year_string = f"2023-{datetime.date.today().year}"
    c_string = "&copy;" if html else "Copyright"
    return f"{c_string} {year_string} Patrick Sanan"


def eprint(*args, **kwargs):
    """Print to stderr."""
    print(*args, file=sys.stderr, **kwargs)


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
        if os.path.isdir(filename) or filename in IMAGE_DIR_IGNORE_FILES:
            continue
        small_path = os.path.join(small_directory, filename)
        # Use Imagemagick's "convert" to
        # resize the largest dimension to 300px
        eprint(f"Info: Generating {small_path}")
        subprocess.run(["convert", "-resize", "300x300>", path, small_path],
                       check=True)
        expected_filenames.add(filename)
    for filename in os.listdir(small_directory):
        if filename in IMAGE_DIR_IGNORE_FILES:
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
