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
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Typing :: Typed',
    ],
    setup_requires=[
        'Sphinx >=1.3, <2',
    ],
    test_suite='tests',
    zip_safe=True,
)
