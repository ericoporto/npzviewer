****************************************************
npzviewer - A simple viewer for npz files from numpy
****************************************************

Install
-------

Just use pip for installing

    pip install npzviewer


Usage
-----

npzviewer supports file dropping, opening from command line, and by clicking open on it's menu.

    usage: npzviewer [-h] [-v] [npzfile]

    npzviewer is a .npz viewer, for numpy saved files.

    positional arguments:
      npzfile        a single .npz file

    optional arguments:
      -h, --help     show this help message and exit
      -v, --version  get software version.

    Copyright 2019 Erico Vieira Porto, GPLv2.


Recommended Install and Run
---------------------------

For installing `pip3` in Ubuntu, use `sudo apt install python3-pip`.

    pip3 install npzviewer

After install, just open a terminal and type:

    npzviewer

Windows install and run
-----------------------

In Windows, install Python 3 from https://www.python.org/, and then open `cmd.exe` and type (press enter after):

    python -m pip install npzviewer

To run, you can type the following in `cmd.exe` or the `run...` prompt

    python -m npzviewer
