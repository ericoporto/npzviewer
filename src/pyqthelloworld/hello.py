#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtCore
from pathlib import Path
import numpy as np

class Window(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.button = QtWidgets.QPushButton('Load .npz file', self)
        self.button.clicked.connect(self.handleButton)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.button)

    def handleButton(self):
        np_filename = QtWidgets.QFileDialog.getOpenFileName(
            self, 'Open File', "~", "NPZ file (*.npz);;All Files (*)")[0]

        my_np_file = Path(np_filename)
        if not my_np_file.is_file():
          return

        npz_loaded_file = np.load(my_np_file)

        k_files = npz_loaded_file.__dict__['files']

        k_files.sort()

        for k in k_files:
          print(k)
          print(str(npz_loaded_file[k]))
          print('---')

        print (np_filename)

def HelloWindow():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
