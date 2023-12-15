"""Utility functions used in multiple places."""

import datetime


def copyright_string(html=True):
    """Produces a copyright string, with an option for HTML."""
    year_string = "2023"
    year = datetime.date.today().year
    if year > 2023:
        year_string += f"-{year}"
    c_string = "&copy;" if html else "Copyright"
    return f"{c_string} {year_string} Patrick Sanan"
