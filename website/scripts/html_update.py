#!/usr/bin/env python
"""Utilities to automatically update HTML source"""

import argparse
import os
import re
import sys

import image_utils
import utils

HEADER_TAG_PREFIX = "<!--END HEADER"
FOOTER_TAG_PREFIX = "<!--START FOOTER"
CUSTOM_HEADER_TAG_PREFIX = "<!--CUSTOM HEADER"

THIS_DIR = os.path.dirname(os.path.realpath(__file__))
DEFAULT_SITE_PATH = os.path.join(THIS_DIR, "..", "site")


def _process_header_lines(header_lines):
    # Look for a title in an h1 tag
    title = "patricksanan.org"
    for line in header_lines:
        if "<h1>" in line:
            title = line.replace("<h1>", "").replace("</h1>", "").strip()
            break
    return [
        '<!DOCTYPE html>\n',
        '<html lang="en-US">\n',
        '  <head>\n',
        '    <meta charset="utf-8" />\n',
        '    <meta name="viewport" content="width=device-width" />\n',
        '    <meta name="author" content="Patrick Sanan" />\n',
        f'    <title>{title}</title>\n',
        '    <link rel="stylesheet" href="styles/styles.css" />\n',
        '    <link href="atom.xml" type="application/atom+xml" rel="alternate" title="Atom feed" />\n',
        '  </head>\n',
        '<body>\n',
        '<div>\n',
        '<a href="index.html">patricksanan.org</a> | <a href="reports.html">trip reports</a> | <a href="music.html">music</a> | <a href="teaching-and-open-source-software.html">academic</a> | <a href="misc.html">misc.</a> | <a href="links.html">links</a> | <a href="Sanan_CV.pdf">CV</a> | <a href="contact.html">contact</a> <span style="float:right;"><a href="atom.xml" rel="alternate">feed</a> <a href="atom.xml" rel="alternate"><img src="images/feed-icon-14x14.png" style="vertical-align:middle" /></a></span>\n',
        '</div>\n',
        f'<h1>{title}</h1>\n',
        '<!--END HEADER -- This line and above can be automatically rewritten!-->\n',
    ]


def _footer_lines():
    return [
        '<!--START FOOTER -- This line and below can be automatically rewritten!-->\n',
        '<div class="footer">\n',
        '<hr>\n',
        f'{utils.copyright_string()}\n',
        '<span style="float:right;">Made with 🤷 by editing <a href="https://developer.mozilla.org/en-US/docs/Web/HTML">HTML</a></span>\n',
        '</div>\n',
        '</body>\n',
        '</html>\n',
    ]


def update_header_and_footer(path):
    """Overwrite header and footer, if custom comments are found.

    Returns whether anything changed.
    """
    if not path.endswith(".html"):
        raise Exception(f"{path} isn't an HTML file")
    lines_out = []
    with open(path, "r") as html_file:
        lines = html_file.readlines()
    header_comment_found = False
    footer_comment_found = False
    header_lines = []
    for line in lines:
        # Do not update if a custom header comment is found
        if CUSTOM_HEADER_TAG_PREFIX in line:
            print("  Not updating: Custom header marker found")
            return

        # Check for header comment, adding the header if found
        if not header_comment_found:
            header_comment_found = line.lstrip().startswith(HEADER_TAG_PREFIX)
            header_lines.append(line)
            if header_comment_found:
                lines_out.extend(_process_header_lines(header_lines))
                continue

        # Check for the footer comment, once the header comment is found
        if header_comment_found and not footer_comment_found:
            footer_comment_found = line.lstrip().startswith(FOOTER_TAG_PREFIX)

        # Once the footer comment is found, append the footer and finish
        if footer_comment_found:
            lines_out.extend(_footer_lines())
            break

        # For body lines after the header is complete, simply copy across
        if header_comment_found:
            lines_out.append(line)

    if not header_comment_found:
        print(
            f"  WARNING: no header comment ({HEADER_TAG_PREFIX}) found. {path} will not be updated"
        )
        return
    if not footer_comment_found:
        print(
            f"  WARNING: no footer comment ({FOOTER_TAG_PREFIX}) found. footer will not be updated for {path}"
        )

    if lines == lines_out:  # could be slow
        # No change
        return False

    with open(path, "w") as html_file:
        html_file.writelines(lines_out)

    # Changes
    return True


def _is_grid_item_div_open(line):
    return "<div" in line and "grid-item" in line


# This requires a class in the closing tag, which is ugly - properly, use a stack to deal with nested item divs
def _is_grid_item_div_close(line):
    return "</div" in line and "grid-item" in line


def _process_grid_item_div_lines(lines):
    alt = ""
    href = ""
    caption = ""
    for line in lines:
        match = re.search(r'alt\w*=\w*"([^"]*)"', line)
        if match:
            if alt:
                print(
                    "  WARNING - two alt strings found in grid item! Not processing"
                )
                return lines
            alt = match.group(1).strip()
        if "<figcaption>" in line:
            if "</figcaption>" not in line:
                print(
                    "  WARNING - Unclosed or multi-line figcaption found! Not processing"
                )
                return lines
            if caption:
                print(
                    "  WARNING - two captions found in grid item! Not processing"
                )
                return lines
            # Strip out any figcaption or em tags
            caption = line.replace("<figcaption>", "").replace(
                "</figcaption>", "").replace("<em>", "").replace("</em>",
                                                                 "").strip()
        else:
            # Look for href on non-caption lines (to allow links in captions)
            match = re.search(r'href\w*=\w*"([^"]*)"', line)
            if match:
                if href:
                    print(
                        "  WARNING - two hrefs found in grid item! Not processing"
                    )
                    return lines
                href = match.group(1).strip()
    if not href:
        print("  WARNING. href not found in grid item - not processing!", lines)
        return lines

    return image_utils.figure_grid_html_lines(input_path=href,
                                              base_directory_prefix="",
                                              alt=alt,
                                              caption=caption)


def _update_figures(path):
    """Updates figures for a give html file. Returns whether anything changed."""
    if not path.endswith(".html"):
        raise Exception(f"{path} isn't an HTML file")
    lines_out = []
    with open(path, "r") as html_file:
        lines = html_file.readlines()
    grid_item_div_open = False
    grid_item_div_lines = []
    line_number = 0
    for line in lines:
        line_number += 1
        new_grid_item_div_open = _is_grid_item_div_open(line)
        if new_grid_item_div_open:
            if grid_item_div_open:
                print(
                    f"grid-item div opened when one already open in {path}:{line_number}. Aborting"
                )
                return
            grid_item_div_open = True

        if grid_item_div_open:
            grid_item_div_lines.append(line)
        else:
            lines_out.append(line)

        new_grid_item_div_close = _is_grid_item_div_close(line)
        if new_grid_item_div_close:
            if not grid_item_div_open:
                print(
                    f"grid-item closed when one not already open in {path}:{line_number}. Aborting"
                )
                return
            grid_item_div_open = False
            lines_out.extend(_process_grid_item_div_lines(grid_item_div_lines))
            grid_item_div_lines = []
    if grid_item_div_open:
        print(f"grid-item div never closed in {path}. Aborting")
        return

    if lines == lines_out:  # could be slow
        # No change
        return False

    # write to a different path
    with open(path + ".new", "w") as html_file:
        html_file.writelines(lines_out)

    # Something changed
    return True


def _update_directory(directory):
    """Updates all HTML files in a directory. Returns if anything changed."""
    if not os.path.isdir(directory):
        raise Exception(f"{directory} is not a directory")
    change = False
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        print(f"{filename}")
        change = change or update_header_and_footer(
            os.path.join(directory, filename))

        # For now, an out-of-place process!
        change = change or _update_figures(os.path.join(directory, filename))

    return change


def update_main():
    """Example usage:

    ./html_update.py

    Returns True if anything changed
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--directory', '-d', default=DEFAULT_SITE_PATH)
    args = parser.parse_args()

    return _update_directory(args.directory)


if __name__ == "__main__":
    """Returns a non-zero exit code if anything changed."""
    change = update_main()
    sys.exit(1 if change else 0)