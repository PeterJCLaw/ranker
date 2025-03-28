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
copyright = '2013-2019, 2021-2025, League Ranker Contributors'

release = version = subprocess.check_output(
    [
        'python',
        str(Path(__file__).parent.parent / 'setup.py'),
        '--version',
    ],
    text=True,
)

html_theme = 'alabaster'

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}
