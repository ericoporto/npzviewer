#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtCore
from pathlib import Path
import os.path
import numpy as np

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, filelist, **kwargs):
        QtWidgets.QWidget.__init__(self)
        self.button = QtWidgets.QPushButton('Load .npz file', self)
        self.plaintext = QtWidgets.QPlainTextEdit(self)
        self.plaintext.setReadOnly(True)
        
        self.button.clicked.connect(self.handleButton)

        self.centralwidget = QtWidgets.QWidget()
        self.setCentralWidget(self.centralwidget)
        layout = QtWidgets.QVBoxLayout(self.centralwidget)
        layout.addWidget(self.button)
        layout.addWidget(self.plaintext)
        self.setAcceptDrops(True)
        self.opemFileIfDropped(filelist)

    def openFileByName(self, np_filename):
        my_np_file = Path(np_filename)
        if not my_np_file.is_file():
          return

        npz_loaded_file = np.load(my_np_file)

        k_files = npz_loaded_file.__dict__['files']

        k_files.sort()

        self.plaintext.clear()

        for k in k_files:
          self.plaintext.appendPlainText(k +' :')
          self.plaintext.appendPlainText(str(npz_loaded_file[k]))
          self.plaintext.appendPlainText('---')

        #print (np_filename)


    def opemFileIfDropped(self, filelist):
        if (isinstance(filelist, str)):
            if (".npz" in filelist):
                self.openFileByName(filelist)

        else:
            matching = [s for s in filelist if ".npz" in s]
            if len(matching) > 0:
                self.openFileByName(matching[0])

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            extension = os.path.splitext(event.mimeData().urls()[0].toLocalFile())[1]
            if extension == '.npz':
                event.accept()
                return
        
        event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls:
            extension = os.path.splitext(event.mimeData().urls()[0].toLocalFile())[1]
            if extension == '.npz':
                event.accept()
                return
        
        event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
            self.opemFileIfDropped(event.mimeData().urls()[0].toLocalFile())

        else:
            event.ignore()

    def handleButton(self):
        np_filename = QtWidgets.QFileDialog.getOpenFileName(
            self, 'Open File', "~", "NPZ file (*.npz);;All Files (*)")[0]

        self.openFileByName(np_filename)

