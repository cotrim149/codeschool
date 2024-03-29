# -*- coding: utf8 -*-
#
# This file were created by Python Boilerplate. Use boilerplate to start simple
# usable and best-practices compliant Python projects.
#
# Learn more about it at: http://github.com/fabiommendes/boilerplate/
#

import os
from setuptools import setup, find_packages


# Meta information
name = 'codeschool'
author = 'Fábio Macêdo Mendes'
version = open('VERSION').read().strip()
dirname = os.path.dirname(__file__)


# Save version and author to __meta__.py
with open(os.path.join(dirname, 'src', name, '__meta__.py'), 'w') as F:
    F.write('__version__ = %r\n__author__ = %r\n' % (version, author))


setup(
    # Basic info
    name=name,
    version=version,
    author=author,
    author_email='fabiomacedomendes@gmail.com',
    url='',
    description='A short description for your project.',
    long_description=open('README.rst').read(),

    # Classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
    ],

    # Packages and depencies
    package_dir={'': 'src'},
    packages=find_packages('src'),
    package_data={
        '': ['templates/*.*'],
        'codeschool': ['static/*.*', 'static/*/*.*', 'static/*/*/*.*'],
    },
    install_requires=['django>=1.9',
                      'django-model-utils', 'django_jinja',
                      'django-picklefield', 'wagtail',
                      'frozendict', 'markdown',
                      'django-annoying', 'django-debug-toolbar',
                      'django-extensions', 'django-guardian',
                      'ejudge>=0.3.4', 'iospec>=0.1.3'],
    extras_require={
        'testing': ['pytest'],
    },

    # Scripts
    entry_points={
        'console_scripts': ['codeschool = codeschool.__main__:main'],
    },

    # Other configurations
    zip_safe=False,
    platforms='any',
    license='GPL',
    test_suite='%s.test.test_%s' % (name, name),
)

