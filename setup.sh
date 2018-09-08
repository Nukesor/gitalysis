#!/usr/bin/bash

virtualenv -p python venv
venv/bin/pip install --upgrade pip

# Install cython manually since pip fucks up some dependencies
venv/bin/pip install cython numpy
venv/bin/python setup.py develop
