#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('../README.md') as readme_file:
   readme = readme_file.read()


requirements = [
    'mxnet',
    'gluoncv',
    'Click>=6.0',
    'dlib>=19.7',
    'numpy',
]

test_requirements = [
]

setup(
    name='mobileface_landmark',
    version='1.0.0',
    description="Recognize faces from Python or from the command line",
    long_description=readme + '\n\n',
    author="becauseOfAi",
    author_email='noemail@gmail.com',
    url='https://github.com/becauseofAI/MobileFace/blob/master',
    packages=[
        'MobileFace_Landmark',
    ],
    package_dir={'MobileFace_Landmark': ''},
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='MobileFace_Landmark,mobileface',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)