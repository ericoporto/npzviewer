from setuptools import setup
from codecs import open
from os import path

setup(
    name='npzviewer',
    version='0.1.0',
    description='A PyQt5 Hello World',
    author='erico',
    author_email='eri0onpm@gmail.com',
    license='GPLv2',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)'
    ],
    keywords='hello world',
    install_requires=['pyqt5','numpy'],
    packages = ["npzviewer"],
    package_dir = {"": "src"},
    scripts = ["npzviewer"]
)
