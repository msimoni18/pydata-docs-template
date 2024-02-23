# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------

project = 'template'
copyright = '2024, author'
author = 'author'
release = '0.1.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx_design',
    'sphinx_copybutton',
    'sphinx_togglebutton',
    'sphinx.ext.intersphinx',
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']

html_theme_options = {
    # "navbar_start": ["navbar-logo"],
    # "navbar_center": ["navbar-nav"],
    # "navbar_end": ["navbar-icon-links"],
    # "navbar_persistent": ["search-button"],
    "navbar_align": "content",
    "show_toc_level": 4,
    "show_nav_level": 4,
    "navigation_depth": 4,
    "logo": {
        "text": "flamingo",
        "image_light": "_static/flamingo.svg",
        "image_dark": "_static/flamingo.svg",
    },
}

# Overwritten by html_theme_options['logo']. If
# those don't exist, fallback is html_logo.
html_logo = "_static/flamingo.svg"

html_favicon = "_static/flamingo.svg"
