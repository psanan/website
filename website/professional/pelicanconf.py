#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os

AUTHOR = 'Patrick Sanan'
SITENAME = 'Patrick Sanan'
SITEURL = 'https://patricksanan.org'

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

# Links
LINKS = (
        ('Personal Blog', 'https://patricksanan.org/personal'),
        )

# Social widgets
SOCIAL = (
         ('GitLab','https://gitlab.com/psanan'),
         ('GitHub','https://github.com/psanan'),
         ('Bitbucket','https://bitbucket.org/psanan'),
         ('twitter', 'http://twitter.com/patricksanan')
         )

# Menu
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (
            ('Posts', SITEURL + '/posts_index.html'), # hack
            ('CV', SITEURL + '/data/Sanan_CV.pdf'), # hack
            )

# Posts (blog) page
INDEX_SAVE_AS = 'posts_index.html'

# Theme
THEME = 'theme'

# Other Settings
DEFAULT_PAGINATION = 3

SUMMARY_MAX_LENGTH = None

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
