#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys
from PyQt5.QtWidgets import QApplication
import argparse
if os.path.isdir(os.path.join(".","src")) and os.path.isfile(
        os.path.join(".","setup.py")):
    sys.path.append(os.path.realpath("src"))
    sys.path.append(os.path.realpath("src/npzviewer"))

from npzviewer import __title__, __version__, __copyright__, __license__
from npzviewer.npzviewer import MainWindow

def main():
    """"
    npzviewer main routine

    When you use `python -m npzviewer`, the main routine is called.
    If you use `pip install npzviewer`, typing npzviewer will also call this routine.

    The objective of this function is to:
    1. load the npzviewer when called without args
    2. if the arg is a .npz file, and no additional args, load the npzviewer and open the file.npz
    3. seeing the current version by using `--version`, and not opening the npzviewer

    """

    __title__ + " comes with ABSOLUTELY NO WARRANTY \nThis is free software, and you are welcome to redistribute it"

    parser = argparse.ArgumentParser(
                prog=__title__,
                description=__title__ + ' is a .npz viewer, for numpy saved files.' + "\n" +
                   __title__ + " comes with ABSOLUTELY NO WARRANTY. \nThis is free software, and you are welcome to redistribute it." ,
                epilog=__copyright__ + ", " + __license__ +".")
    parser.add_argument('-v', '--version', action='store_true', default=False, help='get software version.')
    parser.add_argument('npzfile', nargs='?', default='no_npzfile', help='a single .npz file')
    args = parser.parse_args()

    if args.version == True:
        print(__title__ + "  v " + __version__ )
        exit()

    a = QApplication([])

    mw_arg=[]
    if 'npzfile' in args:
        mw_arg = [args.npzfile]

    mw = MainWindow(mw_arg)
    a.processEvents()
    mw.show()
    mw.raise_()
    exit(a.exec_())

if __name__ == '__main__':
    main()


