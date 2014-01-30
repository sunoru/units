# -*- coding:utf-8 -*-
# filename: setup.py
# by スノル

from setuptools import setup
import sciNote

setup(
    name = 'sciNote',
    version = sciNote.get_version(),
    description = 'Use Python for scientific calculation.',
    author = u'スノル',
    author_email = 's@sunoru.com',
    url = 'https://github.com/sunoru/sciNote',
    py_modules = ['sciNote'],
)
