#!/usr/bin/python

from setuptools import setup, find_packages

setup(name='lsserial',
    version='1.1.0',
    description='List linux serial ports',
    author='Charles Teinturier',
    author_email='teintu.c@gmail.com',
    scripts=['lsserial'],
    install_requires=[
        'pyserial'
    ]
)
