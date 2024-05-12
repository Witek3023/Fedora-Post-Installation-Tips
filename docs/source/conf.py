# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Fedora-Post-Installation-Tips'
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



# -- Options for HTML output

html_theme = "sphinx_rtd_theme"

# -- Options for EPUB output
epub_show_urls = 'footnote'

html_theme_options = {
    'logo_only': False,  
    'display_version': False,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': True,
    'style_nav_header_background': '#333',
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 3
}
