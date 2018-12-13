# -*- coding: utf-8 -*-
from setuptools import setup
from codecs import open
import platform
import errno
import sys
import os
import re

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

datafiles = dict(data_files=[])
osname = platform.system()

with open('npzviewer/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if(int(sys.version_info.major) == 2):
    install_requires = ['numpy']
    print("!!!Please INSTALL PYQT5!!!")
else:
    install_requires = ['numpy','pyqt5']

setup(
    name='npzviewer',
    version=version,
    description='A simple PyQt5 .npz file viewer.',
    long_description=long_description,
    url='https://github.com/ericoporto/npzviewer',
    download_url = 'https://github.com/ericoporto/npzviewer/tarball/'+version,
    author='Erico Vieira Porto',
    author_email='eri0onpm@gmail.com',
    license='GPLv2',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Programming Language :: Python :: 3.5'
    ],
    keywords='numpy development',
    install_requires=install_requires,
    packages = ["npzviewer"],
    entry_points={
        'gui_scripts': [
            'npzviewer = npzviewer.__main__:main'
            ]
    }
)
