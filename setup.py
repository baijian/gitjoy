#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = 'demo',
    version = '0.1.dev',
    description = 'test python project',
    author = 'baijian',
    author_mail = 'baijian@anjuke.com',
    url = '',
    package_dir = {'': 'src'},
    packages = find_packages('src'),
    install_requires = [
        'Flask',
        'Flask-SQLAlchemy',
    ],
)

