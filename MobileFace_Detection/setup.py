#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('../README.md') as readme_file:
   readme = readme_file.read()


requirements = [
    'mxnet',
    'gluoncv',
    'dlib>=19.7',
    'numpy',
]

test_requirements = [
]

setup(
    name='mobileface_detection',
    version='1.3.0',
    description="Recognize faces from Python or from the command line",
    long_description=readme + '\n\n',
    author="becauseOfAi",
    author_email='noemail@gmail.com',
    url='https://github.com/becauseofAI/MobileFace/blob/master/MobileFace_Detection/mobilefacedetnet.py',
    packages=[
        'mobileface_detection',
    ],
    package_dir={'': 'mobileface_detection'},
    package_data={
        'mobileface_detection': ['model/*.*']
    },
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='mobileface_detection,mobileface',
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