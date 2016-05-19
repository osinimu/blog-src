#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'fosi'
SITENAME = u'osisieke'
DESCRIPTION = u"LifePages    <strong>\\</strong>"
SITE_TAGLINE = DESCRIPTION
SITEURL = 'http://osisieke.github.io'
MAIL = "christopherajulo@gmail.com"

TWITTER_USERNAME = "_fosi"

STATIC_PATHS = ['images', 'files', 'extra/robots.txt', 'extra/favicon.ico', 'extra/custom.css']

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = True


# During development, we want urls to be relative
RELATIVE_URLS = True

DEFAULT_LANG = u'en'

USE_FOLDER_AS_CATEGORY = True

PATH = 'content/'

TIMEZONE = 'Africa/Lagos'

DEFAULT_LANG = u'en'
THEME = u"pelican-bootstrap3"

THEME_STATIC_DIR = 'theme'

USE_FOLDER_AS_CATEGORY = True

SHOW_ARTICLE_AUTHOR = True

BOOTSTRAP_THEME = "simplex"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

TWITTER_CARDS = True

CC_LICENSE = "CC-BY-NC-SA"

FILENAME_METADATA='(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'

SOCIAL_WIDGET_NAME = "I am on"
LINKS_WIDGET_NAME = "Bookmarks"

GRAB_ICONS = True

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#       ('Python.org', 'http://python.org/'),
#      ('Jinja2', 'http://jinja.pocoo.org/'),
#     ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
        ('Twitter', 'http://twitter.com/_fosi'),
        ('Goodreads', 'http://goodreads.com/user/'),
          )
		  
PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = ["tipue_search"]
		  
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'authors', 'archives', 'search'))

DEFAULT_PAGINATION = 20



# Settings for current theme
THEME = u"pelican-bootstrap3"

SHOW_ARTICLE_AUTHOR = True
SHOW_ARTICLE_CATEGORY = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True

BOOTSTRAP_FLUID = True

FAVICON = 'images/favicon.png'

ABOUT_ME = u''



DISQUS_NO_ID = True
USE_OPEN_GRAPH = True 
TWITTER_CARDS = True

SHARIFF = True
SHARIFF_LANG = u'en' 
SHARIFF_ORIENTATION = u'vertical'

SHARIFF_THEME = u'standard'
SHARIFF_TWITTER_VIA = True

ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
TAG_URL = 'tags/{slug}.html'
TAG_SAVE_AS = 'tags/{slug}.html'
TAGS_URL = 'tags.html'
CATEGORY_URL = ('category/{slug}/')
CATEGORY_SAVE_AS = ('category/{slug}/index.html')



