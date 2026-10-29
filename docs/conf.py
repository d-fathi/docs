# Configuration file for the Sphinx documentation builder.
#
# Full list of options:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------
import os
import sys

# the documentation lives in <project>/docs, the package in <project>/pyams
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('..'))


# -- Project information -----------------------------------------------------

project = 'PyAMS'
copyright = '(c) 2019-2026, PyAMS'
author = 'd.fathi'

# The full version, including alpha/beta/rc tags
release = '0.3.0'
version = '0.3.0'


# -- General configuration ---------------------------------------------------

extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.napoleon',
              'sphinx.ext.autosectionlabel',
              'sphinx.ext.mathjax',
              'sphinx_rtd_theme',
              'sphinx_math_dollar']
# 'sphinx_panels' was removed: it is no longer maintained, it does not work
# with recent Sphinx versions and no page of this documentation uses it.

# Make section labels unique (every model page has "Parameters", ...).
autosectionlabel_prefix_document = True
suppress_warnings = ['autosectionlabel.*']

# autodoc: the package needs numpy / matplotlib; they are mocked if absent
autodoc_mock_imports = ['numpy', 'matplotlib', 'scipy']
autodoc_member_order = 'bysource'

# math: $...$ for inline formulas (sphinx_math_dollar), \( \) and \[ \] too.
mathjax3_config = {
    'tex': {
        'inlineMath': [['$', '$'], ['\\(', '\\)']],
        'displayMath': [['$$', '$$'], ['\\[', '\\]']],
        'processEscapes': True,
    },
}
mathjax_config = {            # MathJax 2 (Sphinx < 4)
    'tex2jax': {
        'inlineMath': [['$', '$'], ['\\(', '\\)']],
        'displayMath': [['$$', '$$'], ['\\[', '\\]']],
    },
}

# Add any paths that contain templates here, relative to this directory.
templates_path = []

# Patterns to ignore when looking for source files.
# (the example scripts in examples/*.py are only used by literalinclude)
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']
html_logo = "logo.png"
html_favicon = "logo.png"
html_theme_options = {
    "navigation_depth": 5,
    "collapse_navigation": True,
    "logo_only": True,
}

html_show_sourcelink = False
highlight_language = 'python'

html_context = {
    "display_github": True,
    "github_user": "d-fathi",
    "github_repo": "pyams_lib",
    "github_version": "main",
    "conf_py_path": "/docs/",
    "pypi_project": "https://pypi.org/project/pyams-lib/"
}
