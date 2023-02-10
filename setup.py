from setuptools import setup, find_packages

setup(
    name='alexmultiply',
    version='1.0',
    description='A tutorial for creating pip packages.',
    url='https://github.com/alexvingg/test-lib',
    author='Alex',
    author_email='alexvingg@gmail.com',
    packages=find_packages(exclude=['tests', 'tests.*']),
)