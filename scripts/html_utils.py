#!/usr/bin/env python
"""Utilities to process HTML files."""

import os
import re

import utils
from utils import eprint

HEADER_TAG_PREFIX = "<!--END HEADER"
FOOTER_TAG_PREFIX = "<!--START FOOTER"
SKIP_TAG_PREFIX = "<!--DO NOT UPDATE"


def _process_header_lines(header_lines):
    # Get a title from the first h1 tag
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
        ('    <link href="atom.xml" type="application/atom+xml" '
             'rel="alternate" title="Atom feed" />\n'),
        '  </head>\n',
        '<body>\n',
        '<div>\n',
        ('<a href="index.html">patricksanan.org</a> | '
         '<a href="reports.html">trip reports</a> | '
         '<a href="music.html">music</a> | '
         '<a href="teaching-and-open-source-software.html">academic</a> | '
         '<a href="misc.html">misc.</a> | '
         '<a href="links.html">links</a> | '
         '<a href="Sanan_CV.pdf">CV</a> | '
         '<a href="contact.html">contact</a> '
         '<span style="float:right;">'
         '<a href="atom.xml" rel="alternate">feed</a> '
         '<a href="atom.xml" rel="alternate">'
         '<img src="images/feed-icon-14x14.png" style="vertical-align:middle" />'
         '</a></span>\n'),
        '</div>\n',
        f'<h1>{title}</h1>\n',
        f'{HEADER_TAG_PREFIX} -- This line and above can be automatically rewritten!-->\n',
    ]


def _footer_lines():
    return [
        f'{FOOTER_TAG_PREFIX} -- This line and below can be automatically rewritten!-->\n',
        '<div class="footer">\n',
        '<hr>\n',
        f'{utils.copyright_string()}\n',
        ('<span style="float:right;">Made with 🤷 by '
         '<a href="https://github.com/psanan/website">editing HTML</a></span>\n'),
        '</div>\n',
        '</body>\n',
        '</html>\n',
    ]


def should_skip(path):
    """Determines if an HTML file should be skipped for updates.

    This is intended to be used for things like redirects to
    preserve old URLs.
    """
    if not path.endswith(".html"):
        raise ValueError(f"{path} isn't an HTML file")
    with open(path, "r", encoding="utf-8") as html_file:
        lines = html_file.readlines()
    # Check all lines for SKIP_TAG_PREFIX
    # Consider presence of a normal header tag to mean "don't skip",
    # to avoid always scanning all of most files.
    for line in lines:
        if SKIP_TAG_PREFIX in line:
            return True
        if HEADER_TAG_PREFIX in line:
            return False
    return False


def update_header_and_footer(path):
    """Overwrites HTML header and/or footer, relying on custom coments.

    Returns whether anything changed.
    """
    if not path.endswith(".html"):
        raise ValueError(f"{path} isn't an HTML file")
    lines_out = []
    with open(path, "r", encoding="utf-8") as html_file:
        lines = html_file.readlines()
    header_comment_found = False
    footer_comment_found = False
    header_lines = []
    for line in lines:
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
        eprint(
            (f"  WARNING: no header comment ({HEADER_TAG_PREFIX}) found. "
             f"{path} cannot be updated.")
        )
        return True
    if not footer_comment_found:
        eprint(
            (f"  WARNING: no footer comment ({FOOTER_TAG_PREFIX}) found. "
             "footer will not be updated for {path}.")
        )

    if lines == lines_out:  # could be slow
        # No change
        return False

    with open(path, "w", encoding="utf-8") as html_file:
        html_file.writelines(lines_out)

    # Changes
    return True


def _is_grid_item_div_open(line):
    return "<div" in line and "grid-item" in line


# This requires a class in the closing tag, which is ugly.
# More properly, use a stack to deal with nested divs
def _is_grid_item_div_close(line):
    return "</div" in line and "grid-item" in line

def _is_grid_container_div_open(line):
    return "<div" in line and "grid-container" in line

# This requires a class in the closing tag, which is ugly.
# More properly, use a stack to deal with nested divs
def _is_grid_container_div_close(line):
    return "</div" in line and "grid-container" in line


def _process_grid_item_div_lines(lines):
    """Examines an image grid item element and generates a standard one."""
    alt = ""
    href = ""
    caption = ""
    for line in lines:
        match = re.search(r'alt\w*=\w*"([^"]*)"', line)
        if match:
            if alt:
                eprint(
                    "  WARNING - two alt strings found in grid item! Not processing"
                )
                return lines
            alt = match.group(1).strip()
        if "<figcaption>" in line:
            if "</figcaption>" not in line:
                eprint(
                    "  WARNING - Unclosed or multi-line figcaption found! Not processing"
                )
                return lines
            if caption:
                eprint(
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
                    eprint(
                        "  WARNING - two hrefs found in grid item! Not processing"
                    )
                    return lines
                href = match.group(1).strip()
    if not href:
        eprint("  WARNING. href not found in grid item - not processing!", lines)
        return lines

    return figure_grid_html_lines(input_path=href,
                                  base_directory_prefix="",
                                  alt=alt,
                                  caption=caption)


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
    small_path = utils.figure_small_path(path)

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


def update_figures(path):
    """Updates figures for a give HTML file. Returns whether anything changed (or should)."""
    if not path.endswith(".html"):
        raise ValueError(f"{path} isn't an HTML file")
    lines_out = []
    with open(path, "r", encoding="utf-8") as html_file:
        lines = html_file.readlines()
    grid_container_div_open = False
    grid_item_div_open = False
    grid_item_div_lines = []
    line_number = 0
    for line in lines:
        line_number += 1
        if _is_grid_container_div_open(line):
            if grid_item_div_open:
                eprint(
                    ("grid-container opened with grid-item still open in "
                     f"{path}:{line_number}. Aborting figure update.")
                )
            if grid_container_div_open:
                eprint(
                    ("grid-container div opened when one already open in "
                     f"{path}:{line_number}. Aborting figure update.")
                )
                return True
            grid_container_div_open = True
        if _is_grid_item_div_open(line):
            # One could check grid_container_div_open here to require
            # that all grid-items appear inside grid-containers
            if grid_item_div_open:
                eprint(
                    ("grid-item div opened when one already open in "
                     f"{path}:{line_number}. Aborting figure update.")
                )
                return True
            grid_item_div_open = True

        if grid_item_div_open:
            grid_item_div_lines.append(line)
        else:
            lines_out.append(line)

        if _is_grid_item_div_close(line):
            if not grid_item_div_open:
                eprint(
                    ("grid-item closed when one not already open in "
                     f"{path}:{line_number}. Aborting figure update.")
                )
                return True
            grid_item_div_open = False
            lines_out.extend(_process_grid_item_div_lines(grid_item_div_lines))
            grid_item_div_lines = []
        if _is_grid_container_div_close(line):
            if grid_item_div_open:
                eprint(
                    ("grid-container closed with grid-item still open in "
                     f"{path}:{line_number}. Aborting figure update.")
                )
            if not grid_container_div_open:
                eprint(
                    ("grid-container closed when one not already open in "
                     f"{path}:{line_number}. Aborting figure update.")
                )
                return True
            grid_container_div_open = False
    if grid_item_div_open:
        eprint(f"grid-item div never closed in {path}. Aborting figure update.")
        return True
    if grid_container_div_open:
        eprint(f"grid-item div never closed in {path}. Aborting figure update.")
        return True

    if lines == lines_out:  # could be slow
        # No change
        return False

    # Overwrite
    with open(path, "w", encoding="utf-8") as html_file:
        html_file.writelines(lines_out)

    # Something changed
    return True
