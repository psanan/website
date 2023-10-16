#!/usr/bin/env python

import argparse
import os
import subprocess

IGNORE_FILES = [".DS_Store"]

# This should include a class so these figures can be flexbox'd
# the 300 and the 350 below should be constants, and I'm not sure it works as intended for both portrait and landscape
def filename_to_figure(path, small_path):
    """Produce an html figure snippet for a given paths to an image and thumbnail"""
    lines = []
    lines.append('<figure>')
    lines.append(f'<a href="{path}">')
    lines.append(f'<img src="{small_path}" width="300" />')
    lines.append('</a>')
    lines.append(f'<figcaption><em>{path}</em></figcaption>')
    lines.append('</figure>')
    return "\n".join(lines)


def _mkdir_p(path):
    if not os.path.exists(path):
        os.makedirs(path)


# Currently if directory is a relative path, this needs to
# be run from somewhere it makes sense
def _shrink(directory, filename):
    small_dir = os.path.join(directory, "small")
    small_path = os.path.join(small_dir, filename)
    _mkdir_p(small_dir)
    # Requires Imagemagick's "convert" to work
    subprocess.run([
        "convert", "-auto-orient", "-thumbnail", "350x",
        os.path.join(directory, filename), small_path
    ])
    return small_path


def _process_directory(directory):
    if not os.path.isdir(directory):
        raise Exception(f"{directory} is not a directory")
    for filename in sorted(os.listdir(directory)):
        path = os.path.join(directory, filename)
        if os.path.isdir(path):
            continue
        if filename in IGNORE_FILES:
            continue
        small_path = _shrink(directory, filename)
        print(filename_to_figure(path, small_path))


def _main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--directory', '-d', required=True)
    args = parser.parse_args()
    _process_directory(args.directory)


if __name__ == "__main__":
    _main()
