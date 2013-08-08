#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = 'gitjoy',
    version = '1.0',
    description = 'flask project',
    long_description = __doc__,
    author = 'baijian',
    author_mail = 'jian.baij@gmail.com',
    url = '',

    package_dir = {'': 'src'},
    packages = find_packages('src'),
    include_package_data = True,
    zip_safe = False,

    install_requires = [
        'Flask==0.9',
        'Flask-SQLAlchemy==0.16',
        'Flask-OAuth==0.12',
        'Flask-Login==0.1.3',
        'Flask-Assets==0.8',
        'Flask-Script==0.5.3',
        'Flask-WTF==0.8.3',
        'Flask-Mail==0.7.6',
        'Flask-FlatPages==0.3',
        'Flask-Cache==0.12',
        'SQLAlchemy==0.8.0',
        'pygit2==0.17.3',
        'markdown2==2.1.0',
    ],
)
