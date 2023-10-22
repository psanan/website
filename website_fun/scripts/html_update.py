#!/usr/bin/env python
"""Utilities to automatically update HTML source"""

import argparse
import os
import re

import image_utils

HEADER_TAG_PREFIX = "<!--END HEADER"
FOOTER_TAG_PREFIX = "<!--START FOOTER"

THIS_DIR = os.path.dirname(os.path.realpath(__file__))
HEADER_TEMPLATE_PATH = os.path.join(THIS_DIR, "..", "templates", "header.html")
FOOTER_TEMPLATE_PATH = os.path.join(THIS_DIR, "..", "templates", "footer.html")


def update_header_and_footer(path, header_lines, footer_lines):
    """Overwrite header and footer, if custom comments are found."""
    lines_out = []
    if not path.endswith(".html"):
        raise Exception(f"{path} isn't an HTML file")
    with open(path, "r") as f:
        header_comment_found = False
        footer_comment_found = False
        for line in f:
            if not header_comment_found:
                header_comment_found = line.lstrip().startswith(
                    "<!--END HEADER")
                if header_comment_found:
                    lines_out.extend(header_lines)
                    continue
            if header_comment_found and not footer_comment_found:
                footer_comment_found = line.lstrip().startswith(
                    "<!--START FOOTER")
            if footer_comment_found:
                lines_out.extend(footer_lines)
                break
            if header_comment_found:
                lines_out.append(line)
        if not header_comment_found:
            print(
                f"WARNING: no header comment ({HEADER_TAG_PREFIX}) found. {path} will not be updated"
            )
        elif not footer_comment_found:
            print(
                f"WARNING: no footer comment ({FOOTER_TAG_PREFIX}) found. footer will not be updated for {path}"
            )
    with open(path, "w") as f:
        f.writelines(lines_out)

def _is_grid_item_div_open(line):
    return line.lstrip().startswith("<div") and "grid-item" in line


# This requires a class in the closing tag, which is ugly - properly, use a stack to deal with nested item divs
def _is_grid_item_div_close(line):
    return line.lstrip().startswith("</div") and "grid-item" in line

def _process_grid_item_div_lines(lines):
    # TODO instead, go through the lines looking for
    # alt text
    # image location
    # caption
    # and pass to  figure_grid_html in image_utils
    # probably requires regex
    alt=""
    href=""
    caption=""
    for line in lines:
        m = re.search('alt\w*=\w*"([^"]*)"', line)
        if m:
            if alt:
                print("WARNING - two alt strings found in grid item! Not processing")
                return lines
            alt = m.group(1).strip()
        if "<figcaption>" in line:
            if caption:
                print("WARNING - two captions found in grid item! Not processing")
                return lines
            caption = line.replace("<figcaption>","").replace("</figcaption>","").strip()
        m = re.search('href\w*=\w*"([^"]*)"', line)
        if m:
            if href:
                print("WARNING - two hrefs found in grid item! Not processing")
                return lines
            href = m.group(1).strip()
    if not href:
        print("WARNING. href not found in grid item - not processing!", lines)
        return lines

    # Use caption as alt text if none provided
    if not alt:
        alt = caption

    return image_utils.figure_grid_html(
        input_path = href,
        base_directory_prefix = "",
        alt = alt,
        caption = caption)


def update_figures(path):
    if not path.endswith(".html"):
        raise Exception(f"{path} isn't an HTML file")
    lines_out = []
    with open(path, "r") as f:
        grid_item_div_open = False
        grid_item_div_lines = []
        item_div_open = False
        for line in f:
            new_grid_item_div_open = _is_grid_item_div_open(line)
            if new_grid_item_div_open:
                if grid_item_div_open:
                    print(f"grid-item div opened when one already open in {path}. Aborting")
                    return
                grid_item_div_open = True

            if grid_item_div_open:
                grid_item_div_lines.append(line)
            else:
                lines_out.append(line)

            new_grid_item_div_close = _is_grid_item_div_close(line)
            if new_grid_item_div_close:
                if not grid_item_div_open:
                    print(f"grid-item closed when one not already open in {path}. Aborting")
                    return
                grid_item_div_open = False
                lines_out.extend(_process_grid_item_div_lines(grid_item_div_lines))
                lines_out.append("\n")
                grid_item_div_lines = []
        if grid_item_div_open:
            print(f"grid-item div never closed in {path}. Aborting")
            return
    # write to a different path!
    with open(path + ".new", "w") as f:
        f.writelines(lines_out)






def _update_directory(directory):
    """Update all HTML files in a directory"""
    if not os.path.isdir(directory):
        raise Exception(f"{directory} is not a directory")
    with open(HEADER_TEMPLATE_PATH, "r") as f:
        header_lines = f.readlines()
    with open(FOOTER_TEMPLATE_PATH, "r") as f:
        footer_lines = f.readlines()
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        print(f"Attempting to update {filename}")
        update_header_and_footer(os.path.join(directory, filename), header_lines, footer_lines)

        # For now, an out-of-place process!
        update_figures(os.path.join(directory, filename))


def update_main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--directory', '-d', required=True)
    args = parser.parse_args()

    _update_directory(args.directory)


if __name__ == "__main__":
    update_main()
