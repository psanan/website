"""Utility functions used in multiple scripts."""

import datetime
import os


SMALL_DIRNAME = "small"

def copyright_string(html=True):
    """Produces a copyright string, with an option for HTML."""
    year_string = f"2023-{datetime.date.today().year}"
    c_string = "&copy;" if html else "Copyright"
    return f"{c_string} {year_string} Patrick Sanan"


def figure_small_path(path):
    """Returns the small-image path corresponding to a given image or directory."""
    if os.path.isdir(path):
        return os.path.join(path, SMALL_DIRNAME)
    return os.path.join(os.path.dirname(path), SMALL_DIRNAME,
                        os.path.basename(path))
