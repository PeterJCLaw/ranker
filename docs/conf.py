import subprocess
from pathlib import Path

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
]

source_suffix = '.rst'
master_doc = 'index'

project = 'league_ranker'
copyright = '2015, 2017, 2019, League Ranker Contributors'

release = version = subprocess.check_output(
    [
        'python',
        str(Path(__file__).parent.parent / 'setup.py'),
        '--version',
    ],
    text=True,
)

html_theme = 'alabaster'

intersphinx_mapping = {'http://docs.python.org/': None}
