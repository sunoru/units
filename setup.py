# -*- coding:utf-8 -*-
# filename: setup.py
# by スノル

from os.path import join
from setuptools import setup, find_packages

d = {}
sciNote_init = join('src', 'units', '__init__.py')
exec(compile(open(sciNote_init).read(), sciNote_init, 'exec'), d)

setup(
    name = 'units',
    version = d['__version__'],
    author = u'スノル',
    author_email = 's@sunoru.com',
    url = 'https://github.com/sunoru/units',
    description = 'Use Python for scientific calculation.',
    long_description = open('README.md').read(),
    download_url = ('https://www.sunoru.com/code/units-%s' %
        d['__version__']),
    include_package_data = True,
    license = 'Apache license 2.0',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    zip_safe = False,
    platforms = "Independant",
)

