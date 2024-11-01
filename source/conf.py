import sys, os 
sys.path.insert(0,os.path.abspath("Users/leduc-beppujun/Desktop/Mandelbrot_Julia_TP"))
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Mandelbrot_Julia'
copyright = '2024, Jun Leduc'
author = 'Jun Leduc'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.napoleon', # interprete les formats de docstring de google et numpy (en plus de .rst)
              'sphinx.ext.viewcode', # Donne accès au code source depuis la doc
              'myst_parser'
             ]

# Add type of source files
source_suffix=[".rst", ".md"]

templates_path = ['_templates']
exclude_patterns = []

language = 'french'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'traditional'
html_static_path = ['_static']
