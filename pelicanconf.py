#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Çağlar Sayın'
SITENAME = 'Çağlar Sayın'
SITEURL = 'blog.caglarsay.in'
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
USE_FOLDER_AS_CATEGORY = True

#STATIC_PATHS = ['images', 'pdfs']

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ('github', 'https://github.com/caglarsayin/'),
    ('twitter', 'https://twitter.com/caglarsayin'),
    ('google-plus', 'https://plus.google.com/115769740138097262397/about'),
    ('linkedin', 'http://www.linkedin.com/pub/caglar-sayin/10/921/720'),
)

#Theme special
COVER_IMG_URL = '/theme/images/cover.jpg'
PROFILE_IMAGE_URL = '/theme/images/profile.png'
TAGLINE = 'Homo-Sapiens, Computer Engineer, Security Researcher, Sailor, a Bike Owner and Traveler'
#DISQUS_SITENAME - Set this to enable disqus comments in articles.
#GOOGLE_ANALYTICS - Set the Google Analytics code (eg. "UA-000000-00")

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
