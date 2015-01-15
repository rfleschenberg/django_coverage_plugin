#!/usr/bin/env python

from setuptools import setup

setup(
    name='django_template_coverage',
    version='0.1',
    description='Django template coverage.py plugin',
    author='Ned Batchelder',
    author_email='ned@nedbatchelder.com',
    url='https://github.com/nedbat/django_coverage_plugin',
    packages=['django_template_coverage'],
    install_requires=[
        'Django',
        'coverage >= 4.0a2',
        'six',
    ],
)
