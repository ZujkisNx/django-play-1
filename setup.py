# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import django-play-1
version = django-play-1.__version__

setup(
    name='django-play-1',
    version=version,
    author='',
    author_email='pauliusruzgas@gmail.com',
    packages=[
        'django-play-1',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.1',
    ],
    zip_safe=False,
    scripts=['django-play-1/manage.py'],
)