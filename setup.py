#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages

setup(
    name='range_image_proc',
    version='0.1dev',
    author='Brian Okorn',
    packages=find_packages('python'),
    package_dir={'': 'python'},
    description='Utility functions for processing range images',
    long_description=open('README.md').read(),
    package_data = {'': ['*.so']},
)

