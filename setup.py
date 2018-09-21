"""Setuptools file for gitalysis."""
from setuptools import setup, find_packages

setup(
    name='gitalysis',
    author='Arne Beer',
    author_email='privat@arne.beer',
    version='0.1.1',
    description='The data mining tool for data from Gitalizer. Used to analyse privacy implications of exposing Git metadata',
    keywords='git github metadata data-mining privacy',
    url='http://github.com/nukesor/gitalizer',
    license='MIT',
    install_requires=[
        # Models, Database and config
        'gitalizer~=0.1',

        # Location handling
        'cython~=0.28',
        'cartopy~=0.16',
        'pycountry~=18.2',
        'geopy',

        # Machine learning
        'scikit-learn~=0.19',

        # Visualization
        'numpy~=1.7',
        'pandas~=0.21',
        'seaborn~=0.8',
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Environment :: Console',
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'gitalysis=gitalysis:cli',
        ],
    }
)
