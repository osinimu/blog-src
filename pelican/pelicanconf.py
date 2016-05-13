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


BIO = \
	u'''
		<p>Full name: <strong>{name}</strong>.</p>
		
		<p>
		</p>
		<p>I enjoy reading. I appreciate writing; and I try to be good at this myself. Some other interests include singing, technology, and psychology.
		</p>
		<p>In my spare time, I listen to podcasts about different topics ranging from startups to technology, innovations, psychology and more.
		<br/>
		<br/><b>Email: </b> christopherajulo [at] gmail [dot] com
		</p>
	'''
	
AUTHOR_SHORTBIO = u''

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
        ('goodreads', 'http://goodreads.com/user/'),
          )
		  
		  
DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search')

DEFAULT_PAGINATION = 200



# Settings for current theme
THEME = u"dopetrope"

SHOW_ARTICLE_AUTHOR = True
SHOW_ARTICLE_CATEGORY = True

MENUITEMS = (
	('Home', '/'),
	('About', '#about')
)

BOOTSTRAP_FLUID = True

FAVICON = 'images/favicon.png'

DISPLAY_ARTICLE_INFO_ON_INDEX = True

ABOUT_ME = u''
AVATAR =

DISQUS_NO_ID = True

DISQUS_DISPLAY_COUNTS = TRUE


SITESUBTITLE = SITE_TAGLINE

ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
TAG_URL = 'tags/{slug}.html'
TAG_SAVE_AS = 'tags/{slug}.html'
TAGS_URL = 'tags.html'
CATEGORY_URL = ('category/{slug}/')
CATEGORY_SAVE_AS = ('category/{slug}/index.html')


