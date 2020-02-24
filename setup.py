#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 17:52:30 2020
@author: Thomas Berrod
"""
from setuptools import setup, find_packages

setup(
    name='pywpipe',
    version='0.1',
    description='private package for named pipe server',
    url='git@github.com:cosmegitrobot/pywpipe.git',
    author='BenjaminMuylDesign, Nedeleg Bigi, Thomas Berrod',
    author_email='bmuyl@mac.com, nedelegbigi@gmail.com, thomasberrod42@gmail.com',
    license='unlicense',
    packages=find_packages(exclude=("tests", "sh")),
    install_requires=[],
    zip_safe=False
)
