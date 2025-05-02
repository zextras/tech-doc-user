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
import time

hubhome = 'https://docs.zextras.com/landing/zextras_documentation.html'
# Define the languages you want to support
# Adatta questa lista alle lingue che desideri supportare
locales = ['en', 'it', 'fr']

# Path to your locale directories
locale_dirs = ['locales/']


# -- Get current year --------------------------------------------------------
current_year = time.strftime('%Y')

# -- Project information -----------------------------------------------------

project = 'Zextras Carbonio'
copyright = '2025: ZEXTRAS'
author = 'The Zextras Team'

# The full version, including alpha/beta/rc tags
release = '25.3'
version = release

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx_design', 'sphinx_copybutton',
              'sphinxcontrib.email']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

rst_prolog = """
.. |carbonio|  replace:: Carbonio
.. |product| replace:: Carbonio
.. |storage| replace:: Carbonio Advanced
"""

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
html_css_files = ['css/carbonio.css']
html_js_files = ['js/posthog.js']
html_favicon = 'img/favicon.ico'
html_title = project + ' Documentation'
html_theme_options = {
    'use_download_button': False,
    'use_repository_button': False,
    'use_issues_button': False,
    'navigation_with_keys': False,
    'logo': {
        'image_light': 'carbonio-black.svg',
        'image_dark': 'carbonio-white.svg',
        'text': '%s' % release,
    },
    'footer_content_items': ['zx-copyright.html'],
}
html_sidebars = {"**": ['navbar-logo.html', 'search-button-field.html', 'sbt-sidebar-nav.html',
                        'locales.html', 'home.html']}

# Exporting variables to be available in templates

languages = ['en', 'it', 'fr']

html_context = {
    'languages': ['en', 'it'],
    'localpath': 'docs',
    'hubhome': '%s' % hubhome,
}


def setup(app):
    app.connect('html-page-context', add_pagename)


def add_pagename(app, pagename, templatename, context, doctree):
    context['pagename'] = pagename


gettext_compact = "carbonio"

# there are more options, but at the moment we don't need them. They
# can be found at
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-the-linkcheck-builder


figure_language_filename = '{path}{language}/{basename}{ext}'
