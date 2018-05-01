import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name='py-ipfs-api',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    license='GPL3',
    description='Python library for IPFS',
    long_description=README,
    url='https://github.com/anthonygd/py-ipfs-api',
    author='Natán Calzolari',
    author_email='anthony@safechain.io',
    classifiers=[
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
