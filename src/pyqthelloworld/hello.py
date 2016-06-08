#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtCore

class Window(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.button = QtWidgets.QPushButton('Print Hello World', self)
        self.button.clicked.connect(self.handleButton)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.button)

    def handleButton(self):
        print ('Hello World!')

def HelloWindow():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
