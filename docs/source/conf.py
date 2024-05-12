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
    'style_nav_header_background': 'green',
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 3,
}

# -- Customization

# Custom logo
html_logo = 'logo.png'

# Favicon
html_favicon = 'logo.png'

# Responsive design meta tag
html_theme_options = {
    'meta': {
        'viewport': 'width=device-width, initial-scale=1.0',
    },
}

# Code block styling
html_codeblock_linenos_style = 'inline'

# Custom navigation bar
html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 3,
    'includehidden': True,
}

