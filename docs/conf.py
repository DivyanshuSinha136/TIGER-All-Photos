# docs/conf.py

import os
import sys
sys.path.insert(0, os.path.abspath('..'))  # So autodoc finds your modules

project = 'Pythonaibrain'
author = 'Divyanshu Sinha'
release = '1.1.9'  # your package version

extensions = [
    'sphinx.ext.autodoc',            # for docstring extraction
    'sphinx.ext.napoleon',           # Google style docstrings support
    'sphinx.ext.viewcode',           # add links to source code
    'sphinx_autodoc_typehints',      # type hints support
    'myst_parser',                   # markdown support
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
