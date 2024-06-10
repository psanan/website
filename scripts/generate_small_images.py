#!/usr/bin/env python
"""Generate image HTML."""

import argparse
import os

import html_utils
import utils

THIS_DIR = os.path.dirname(os.path.realpath(__file__))
IMAGES_DIR_PREFIX = os.path.realpath(os.path.join(THIS_DIR, ".."))
IMAGES_DIR = os.path.join(IMAGES_DIR_PREFIX, "site", "images")


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

    utils.create_small_images(directory)


if __name__ == "__main__":
    _main()
