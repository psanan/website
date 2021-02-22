#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os

AUTHOR = 'Patrick Sanan'
SITENAME = "Patrick Sanan's Blog"
SITEURL = 'https://patricksanan.org/personal'

PATH = 'content'

STATIC_PATHS = ['images','data']

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LINKS = (
        ('Professional Site','https://patricksanan.org'),
        )

SOCIAL = (
         )

# Menu
DISPLAY_CATEGORIES_ON_MENU = True

# Theme
THEME = '../theme'

# Other Settings
DEFAULT_PAGINATION = 1

SUMMARY_MAX_LENGTH = None

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
