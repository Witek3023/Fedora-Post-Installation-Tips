# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Fedora-Post-Installation-Tips '
copyright = '2024, Witek3023'
author = 'Witek3023'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'style_nav_header_background': '#343131',
    'logo_only': True,
    'style_external_links': True,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'includehidden': True,
    'titles_only': False,
    'prev_next_buttons_location': 'bottom',
    'style_nav_header_background': '#343131',
    'display_version': True,
    'navigation_depth': 3,
    'collapse_navigation': True,
    'sticky_navigation': True,
    'style_nav_header_background': '#343131',
    'logo_only': False,
    'titles_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'both',
}

# -- Options for EPUB output
epub_show_urls = 'footnote'
