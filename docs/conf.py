# -- Path setup --------------------------------------------------------------

import os
import sys
sys.path.insert(0, os.path.abspath('..'))  # Adjust if needed

# -- Project information -----------------------------------------------------

project = 'Pythonaibrain'
author = 'Divyanshu Sinha'

# -- General configuration ---------------------------------------------------

extensions = [
    "myst_parser",  # Markdown support
    "sphinx.ext.autodoc",  # if you use autodoc for docstrings
    "sphinx.ext.napoleon", # for Google/NumPy style docstrings (optional)
]

# Support both reStructuredText and Markdown files
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

master_doc = 'index'  # Your main file can be index.md or index.rst

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'  # ReadTheDocs theme

# Optional: Enable MyST extensions (like definition lists, admonitions)
myst_enable_extensions = [
    "deflist",
    "html_admonition",
    "html_image",
]
