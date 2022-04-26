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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import pathlib
import sys
from datetime import datetime
sys.path.insert(0, pathlib.Path(__file__).parents[2].resolve().as_posix())

html_permalinks_icon = '§'

# -- Project information -----------------------------------------------------

project = 'Daisi'
copyright = str(datetime.now().year) + ', Daisi Technology Inc.'
author = 'Daisi Technology Inc.'

# The full version, including alpha/beta/rc tags
release = '0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # "sphinx_panels",
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx_click.ext",
    "sphinx-jsonschema",
    "sphinxemoji.sphinxemoji",
    "sphinx_copybutton",
    "sphinxcontrib.yt",
    "versionwarning.extension",
    "sphinx_sitemap",
    "myst_nb",
    "sphinx.ext.doctest",
    "sphinx.ext.coverage",
    "sphinx_external_toc",
    "sphinxcontrib.autodoc_pydantic",
]

myst_enable_extensions = [
    "dollarmath",
    "amsmath",
    "deflist",
    "html_admonition",
    "html_image",
    "colon_fence",
    "smartquotes",
    "replacements",
]



# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []
copybutton_prompt_text = ">>> "

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
# html_theme = 'sphinx_rtd_theme'
# html_theme = 'sphinx_material'
# html_theme = 'insipid'
html_theme = 'sphinx_book_theme'
# html_theme = 'pydata_sphinx_theme'
# html_theme = 'sphinx_airflow_theme'
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = [
    '_static/css/custom.css',
]
html_logo = "daisi-transparent-full.svg"
html_theme_options = {
    'logo_only': True,
    'display_version': False,
}
