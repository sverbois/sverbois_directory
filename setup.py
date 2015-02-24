# -*- coding: utf-8 -*-

import os

from setuptools import setup
from setuptools import find_packages

version = '1.0.dev0'

install_requires = [
    'ColanderAlchemy',
    'Kotti',
]


setup(
    name='sverbois_directory',
    version=version,
    description="A directory for Kotti",
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Framework :: Kotti",
    ],
    author="Sébastien Verbois",
    author_email='sebastien.verbois@unamur.be',
    url='https://github.com/sverbois/sverbois_directory',
    keywords='kotti pyramid sqlalchemy bootstrap',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    tests_require=[],
    dependency_links=[],
    entry_points={
        'fanstatic.libraries': [
            'sverbois_directory = sverbois_directory.fanstatic:library',
        ],
    },
    extras_require={},
)
