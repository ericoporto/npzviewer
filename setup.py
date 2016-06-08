from setuptools import setup
from codecs import open
from os import path

setup(
    name='pyqthelloworld',
    version='1.0.0',
    description='A PyQt5 Hello World',
    author='erico',
    author_email='a@b.c',
    license='GPLv2',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)'
    ],
    keywords='hello world',
    install_requires=['pyqt5'],
    packages = ["pyqthelloworld"],
    package_dir = {"": "src"},
    scripts = ["pyqthelloworld"]
)
