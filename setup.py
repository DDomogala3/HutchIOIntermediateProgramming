import os
import unittest

from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='hutchiointermediateprogramming',
    version='0.1',
    description='report classification for Case Report Forms',
    long_description=read('README.md'),
    license='Apache 2.0',
    url='https://github.com/WhiteAu/HutchIOIntermediateProgramming/',
    packages=find_packages(exclude=['tests', 'bin']),
    test_suite='tests',
    include_packages=True,
    install_requires=['scikit-learn',
                      'numpy',
                      'pandas']
)
