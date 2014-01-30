# -*- coding:utf-8 -*-
# filename: setup.py
# by スノル

from os.path import join
from setuptools import setup

d = {}
sciNote_init = join('sciNote', '__init__.py')
exec(compile(open(sciNote_init).read(), sciNote_init, 'exec'), d)

setup(
    name = 'sciNote',
    version = d['__version__'],
    author = u'スノル',
    author_email = 's@sunoru.com',
    url = 'https://github.com/sunoru/sciNote',
    description = 'Use Python for scientific calculation.',
    long_description = open('README.md').read(),
    download_url = ('https://www.sunoru.com/code/sciNote-%s' %
        d['__version__']),
    include_package_data = True,
    license = 'Apache license 2.0',
    packages = ['sciNote', 'sciNote.units'],
    platforms = ["Windows", "Linux", "Max OS-X", "Unix", "Solaris"],
)
