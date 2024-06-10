# SPDX-FileCopyrightText: 2022 Zextras <https://www.zextras.com/>
#
# SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
# sys.path.insert(0, os.path.abspath('.'))
import time
from pygit2 import Repository

# Add the correct URLs for each stage of release, which are needed to
# correctly implement the language switcher. The last one is your local
# web server, for testing purposes, so set it to your own preferences.

branch = Repository('.').head.shorthand

if branch == 'devel' :
    ughome = 'https://zextrasdoc-devel.s3-website-eu-west-1.amazonaws.com/user-guides'
elif branch == 'pre_release':
    ughome = 'https://zextrasdoc.s3-website-eu-west-1.amazonaws.com/user-guides'
elif branch == 'master':
    ughome = 'https://docs.zextras.com/user-guides'
else:
    ughome= 'http://localhost:8020/user-guides'

hubhome = 'https://docs.zextras.com/landing/zextras_documentation.html'

# -- Get current year --------------------------------------------------------
current_year = time.strftime('%Y')

# -- Project information -----------------------------------------------------

project = 'Zextras Carbonio'
copyright = '2023: ZEXTRAS'
author = 'The Zextras Team'

# The full version, including alpha/beta/rc tags
release = '24.5.0'
version = release
prev = '24.3.0'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [ 'sphinx_design', 'sphinx_copybutton',
               'sphinxcontrib.email' ]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [ '_includes', 'cli', 'glossary.rst',
                     'common/carbonio/adminpanel',
                     'common/carbonio/usage',
                     'common/carbonio/mesh',
                     'common/carbonio/web-access.rst',
                     'admincli/administration/delegatedadmin.rst' ]

rst_prolog = """

.. |product| replace:: Carbonio
.. |storage| replace:: Carbonio Advanced
.. |prev| replace:: %s
""" %prev + open("replace.txt").read()

# -- Configuration of extensions ---------------------------------------------

# copybutton, see https://sphinx-copybutton.readthedocs.io/en/latest/
copybutton_prompt_text = r'\$\s|#\s|carbonio>\s|zextras\$\s'
copybutton_prompt_is_regexp = True
copybutton_line_continuation_character = "\\"
copybutton_only_copy_prompt_lines = True

numfig = True

email_automode = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'
html_show_sourcelink = False

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = [ 'css/carbonio.css' ]
#html_js_files = [ 'js/matomo.js' ]
html_favicon = 'img/favicon.ico'
html_title = project + ' Documentation'
templates_path = [ 'common/templates' ]
html_theme_options = {
    'use_download_button': False,
    'repository_url': 'https://github.com/zextras/tech-doc/',
    'repository_branch': 'master',
    'use_repository_button': True,
    'use_issues_button': True,
    'logo': {
        'image_light': 'carbonio-black.svg',
        'image_dark': 'carbonio-white.svg',
        'text': '%s' %release,
    },
    'footer_content_items': [ 'zx-copyright.html' ],
}
html_sidebars = { "**": [ 'navbar-logo.html', 'sbt-sidebar-nav.html',
                          'locales.html', 'home.html' ] }

# Exporting variables to be available in templates

html_context = { 'hubhome' : '%s' %hubhome,
                 'ughome' : '%s' %ughome,
                 'current_language': 'en',
                 'localpath': 'carbonio',
                 'languages': [
                     ['en', '/en/html'],
                     ['it', '/it/html']
                 ]
                }

# -- Options for linkcheck output --------------------------------------------

# list of URLs to ignore
linkcheck_ignore = [ r'.*.example.com(:\d+)?/',
                     'https://my-saml-provider.org/',
                     'https://notifications.zextras.com/firebase/',
                     r'https://mycompany.okta.com/.*',
                     r'../../.*' ]

# localization options
locale_dirs = ['locales/']
gettext_compact = "carbonio"

# there are more options, but at the moment we don't need them. They
# can be found at
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-the-linkcheck-builder
