#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open("requirements.txt") as f:
    requirements = [req.strip() for req in f.readlines()]

setup(
    name='proyecto-next-journal',
    version='0.1.0',
    description="Descripción corta del proyecto.",
    author="Magdalena Segura",
    url='https://github.com/maggiegsegura/proyecto-next-journal',
    packages=[
        'scripts',
    ],
    package_dir={'scripts': 'scripts'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
    ],
)
