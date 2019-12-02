from setuptools import find_packages, setup


with open('README.rst') as f:
    long_description = f.read()


setup(
    name='sr.comp.ranker',
    version='1.3.0',
    packages=find_packages(exclude=('tests',)),
    package_data={'sr.comp.ranker': ['py.typed']},
    namespace_packages=['sr', 'sr.comp'],
    url='https://ranker.readthedocs.io/en/latest/',
    project_urls={
        'Documentation': 'https://ranker.readthedocs.io/en/latest/',
        'Code': 'https://github.com/PeterJCLaw/ranker',
        'Issue tracker': 'https://github.com/PeterJCLaw/ranker/issues',
    },
    long_description=long_description,
    author='Student Robotics Competition Software SIG',
    author_email='srobo-devel@googlegroups.com',
    license='MIT',
    setup_requires=[
        'Sphinx >=1.3, <2'
    ],
    test_suite='tests',
    zip_safe=True,
)
