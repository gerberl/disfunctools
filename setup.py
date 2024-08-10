"""with help from https://python-packaging.readthedocs.io/en/latest/minimal.html"""

from setuptools import setup, find_packages

setup(
    name='disfunctools',
    version='0.1',
    description='My own humble extension to `itertools`, `functools`, and the like, primarily for my own projects.',
    author='Luciano Gerber',
    author_email='L.Gerber@mmu.ac.uk',
    license='BSD-3',
    packages=find_packages(),
)