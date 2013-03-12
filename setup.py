#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = 'hello',
    version = '1.0',
    description = 'test python project',
    author = 'baijian',
    author_mail = 'baijian@anjuke.com',
    url = '',
    package_dir = {'': 'src'},
    packages = ['hello'],
    install_requires = [
        'pyzmq==2.2.0.1',
    ],
)

