#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'fosi'
SITENAME = u'osisieke'
DESCRIPTION = u"LifePages    <strong>\\</strong>"
SITE_TAGLINE = DESCRIPTION
SITEURL = 'http://osisieke.github.io'
MAIL = "christopherajulo@gmail.com"

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


PATH = 'content/'

TIMEZONE = 'Africa/Lagos'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


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
        ('goodreads', 'http://goodreads.com/user/show/41177369-tosin-damilare-james-animashaun'),
        ('github', 'http://github.com/osisieke'),
          )

DEFAULT_PAGINATION = 200

# Settings for current theme
THEME = 'dopetrope'

MENUITEMS = (
	('Home', '/'),
	('About', '#about')
)

ABOUT_TEXT = u'What is all these about'
ABOUT_IMAGE =  ""
ABOUT_LINK = "Find out more"

SITESUBTITLE = SITE_TAGLINE

COPYRIGHT = "Osisieke"


