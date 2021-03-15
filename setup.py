from setuptools import setup

setup(
    name='potatoutils',
    version='0.0.1',
    description='bunch of handy data structures and stuff',
    py_modules=["helloworld"],
    package_dir={'':'src'}
)

"""

import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

setup(
    name='potatoutils',
    version='0.0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='',
    long_description=open('README.txt').read(),
    install_requires=[],
    url='',
    author='Dorijan Cirkveni AKA Mouse Potato Does Stuff',
    author_email='mousepotato@tutanota.com'
)
# packagedir={'': 'src'},
# packages=find_packages(exclude=['tests*']),

"""
