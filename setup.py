#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = 'demo',
    version = '1.0.dev',
    description = 'test python project',
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
    ],

    #dependency_links = ['http://xxx.xx.com'],
)

