#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os

AUTHOR = 'Patrick Sanan'
SITENAME = "patricksanan.org"
SITEURL = 'https://patricksanan.org'

PATH = 'content'

STATIC_PATHS = ['images', 'data']

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LINKS = (
        )

SOCIAL = (
        ('CV', SITEURL + '/data/Sanan_CV.pdf'),
        ('GitLab','https://gitlab.com/psanan'),
        ('GitHub','https://github.com/psanan'),
        ('LinkedIn','https://www.linkedin.com/in/patrick-sanan-80055157/'),
        ('Some Music', 'https://windfarmmusic.wordpress.com/'),
        )

# Menu
DISPLAY_CATEGORIES_ON_MENU = True
MENUITEMS = (
        ('Posts', SITEURL + '/posts_index.html'), # hack
        ('CV', SITEURL + '/data/Sanan_CV.pdf'), # hack
        )

# Posts (blog) page
INDEX_SAVE_AS = 'posts_index.html'

# Theme
THEME = 'theme'

# Other Settings
SUMMARY_MAX_LENGTH = 0

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
