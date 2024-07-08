#!/usr/bin/env python
"""Generate image HTML."""

import argparse
import os
import subprocess

import utils

THIS_DIR = os.path.dirname(os.path.realpath(__file__))
IMAGES_DIR_PREFIX = os.path.realpath(os.path.join(THIS_DIR, ".."))
IMAGES_DIR = os.path.join(IMAGES_DIR_PREFIX, "site", "images")
ALLOWED_IMAGE_EXTENSIONS = [".jpg", ".jpeg", ".png"]  # Lowercase


def _is_image(filename):
    return os.path.splitext(filename)[1].lower() in ALLOWED_IMAGE_EXTENSIONS


def _create_small_images(directory):
    """Uses Imagemagick to create small versions of images in a directory."""
    small_directory = utils.figure_small_path(directory)
    if not os.path.exists(small_directory):
        os.makedirs(small_directory)
    expected_filenames = set()
    for filename in sorted(os.listdir(directory)):
        path = os.path.join(directory, filename)
        if not _is_image(filename):
            continue
        small_path = os.path.join(small_directory, filename)
        # Use Imagemagick's "convert" to
        # resize the largest dimension to 300px
        print(f"Info: Generating {small_path}")
        try:
            subprocess.run(["convert", "-resize", "300x300>", path, small_path],
                           check=True)
        except subprocess.CalledProcessError as error:
            print("ERROR! Conversion failed:", error)
        expected_filenames.add(filename)
    for filename in os.listdir(small_directory):
        if not _is_image(filename):
            continue
        if filename in expected_filenames:
            expected_filenames.remove(filename)
        else:
            print(
                f"Warning! Unexpected small file {filename} found in {small_directory}"
            )
    if expected_filenames:
        print(f"ERROR! {small_directory} is missing {expected_filenames}")
    return small_directory


def _main():
    demo_post_name = "swiss-cantonal-highpoints"
    demo_dir = os.path.join(IMAGES_DIR, demo_post_name)
    description = f"""Generates small images in an image directory. E.g

    mkdir -p {demo_dir}
    cp img1.jpg {demo_dir}
    python {__file__} -q {demo_post_name} """
    parser = argparse.ArgumentParser(
        description=description,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--quick-directory', '-q', required=True)
    args = parser.parse_args()

    directory = os.path.join(IMAGES_DIR, args.quick_directory)

    _create_small_images(directory)


if __name__ == "__main__":
    _main()
