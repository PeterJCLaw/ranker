import os
import sys


sys.path.insert(0, os.path.abspath('..'))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
]

source_suffix = '.rst'
master_doc = 'index'

project = 'league_ranker'
copyright = '2015, 2017, League Ranker Contributors'

release = '1.0.0'
version = '1.0.0'

html_theme = 'alabaster'

intersphinx_mapping = {'http://docs.python.org/': None}
