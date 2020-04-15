#!/bin/env python
from setuptools import setup, find_packages

setup(
    name='{{Name}}',
    version='{{Version}}',
    include_package_data=True,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            '{{Command}}={{ProjectSlug}}:cli',
            ]
        },
    install_requires=[
        'click',
        #Add other requirements here
    ]
)
