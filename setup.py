"""with help from https://python-packaging.readthedocs.io/en/latest/minimal.html"""

from setuptools import setup

setup(
    name='disfunctools',
    version='0.1',
    description='My own humble extension to `itertools`, `functools`, and the like, primarily for my own projects.',
    url='https://github.com/gerberl/disfunctools',
    author='Luciano Gerber',
    author_email='L.Gerber@mmu.ac.uk',
    license='BSD-3',
    packages=['disfunctools'],
    zip_safe=False
)