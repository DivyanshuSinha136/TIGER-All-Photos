import os
import sys

# Add project root to Python path
sys.path.insert(0, os.path.abspath('..'))

# Project information
project = "Pythonaibrain"
author = "Divyanshu Sinha"
release = "1.1.9"

# Extensions
extensions = [
    "myst_parser",          # Enable Markdown support
]

# Source file formats
source_suffix = {
    ".md": "markdown",
    ".rst": "restructuredtext",
}

# Root document (index.md)
master_doc = "index"

# Theme
html_theme = "sphinx_rtd_theme"

# MyST settings (optional but useful)
myst_enable_extensions = [
    "deflist",
    "html_admonition",
    "html_image",
]
