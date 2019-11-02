#!/usr/bin/python3
# -*- coding: utf-8 -*-

#    npzviewer
#    Copyright (C) 2019  Érico Vieira Porto
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from PyQt5 import QtWidgets, QtCore, QtGui
from pathlib import Path
import os.path
import numpy as np


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, filelist, **kwargs):
        QtWidgets.QWidget.__init__(self)
        self.button = QtWidgets.QPushButton('Load .npz file', self)

        self.encodingCombo = QtWidgets.QComboBox(self)
        self.encodingCombo.addItem('ASCII')
        self.encodingCombo.addItem('latin1')
        self.encodingCombo.addItem('bytes')

        self.plaintext = QtWidgets.QPlainTextEdit(self)
        self.plaintext.setReadOnly(True)
        self.plaintext.setMaximumHeight(320)

        self.button.clicked.connect(self.handleButton)

        self.centralwidget = QtWidgets.QWidget()
        self.setCentralWidget(self.centralwidget)
        layout = QtWidgets.QVBoxLayout(self.centralwidget)
        hlayout = QtWidgets.QHBoxLayout()
        hlayout.addWidget(self.button)
        hlayout.addWidget(self.encodingCombo)

        layout.addLayout(hlayout)
        layout.addWidget(self.plaintext)
        self.setAcceptDrops(True)
        self.opemFileIfDropped(filelist)

        vlayout = QtWidgets.QVBoxLayout()
        self.keysCombo = QtWidgets.QComboBox(self)
        self.indexSpin = QtWidgets.QSpinBox(self)
        self.indexSpin.setSingleStep(1)
        self.keysCombo.currentTextChanged.connect(self.comboKeyChanged)
        self.indexSpin.editingFinished.connect(self.spinIndexChanged)
        self.indexSpin.setVisible(False)
        self.matTable = QtWidgets.QTableWidget(self)

        self.selected_nparr = np.array([])

        self.npz_loaded_file = ""

        vlayout.addWidget(self.keysCombo)
        vlayout.addWidget(self.indexSpin)
        vlayout.addWidget(self.matTable)

        layout.addLayout(vlayout)

    def set2dMatrixOnTable(self, nparr):
        row_count = nparr.shape[0]
        column_count = nparr.shape[1]

        self.matTable.setRowCount(row_count)
        self.matTable.setColumnCount(column_count)

        arrmax = np.nanmax(nparr)
        arrmin = np.nanmin(nparr)

        for row in range(row_count):
            for col in range(column_count):
                value = nparr[row][col]
                cell = QtWidgets.QTableWidgetItem(str(value))
                redpercent = int(np.clip(255 * (value - arrmin) / (arrmax - arrmin), 0, 255))
                bluepercent = int(128 + (255 - redpercent) / 2)
                self.matTable.setItem(row, col, cell)
                self.matTable.item(row, col).setBackground(QtGui.QColor(redpercent, 128, bluepercent))

    def spinIndexChanged(self):
        nparr = self.selected_nparr
        if self.selected_nparr.ndim is 3:
            nparr = self.selected_nparr[int(self.indexSpin.value()), :, :]

        if nparr.ndim is 2:
            self.set2dMatrixOnTable(nparr)

    def comboKeyChanged(self, t):
        self.matTable.clear()
        self.indexSpin.setValue(0)
        self.indexSpin.setVisible(False)

        if len(t) < 1:
            return

        selected_matrix = self.npz_loaded_file[t]
        self.selected_nparr = np.array(selected_matrix)
        nparr = self.selected_nparr

        if nparr.ndim is 3:
            self.indexSpin.setVisible(True)
            self.indexSpin.setMaximum(nparr.shape[0]-1)
            self.indexSpin.setMinimum(0)
            nparr = nparr[0, :, :]

        if nparr.ndim is 2:
            self.set2dMatrixOnTable(nparr)

        elif nparr.ndim is 0:
            return
        elif nparr.ndim is 1:
            self.matTable.setColumnCount(1)
            self.matTable.setRowCount(len(nparr))
            for n, value in enumerate(nparr):  # loop over items in first column
                self.matTable.setItem(n, 0, QtWidgets.QTableWidgetItem(str(value)))

        header = self.matTable.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)

    def openFileByName(self, np_filename):
        my_np_file = Path(np_filename)
        if not my_np_file.is_file():
            return

        self.npz_loaded_file = np.load(my_np_file,encoding=self.encodingCombo.currentText())

        k_files = self.npz_loaded_file.__dict__['files']

        k_files.sort()

        self.plaintext.clear()

        self.plaintext.appendPlainText('keys are :' + str(list(self.npz_loaded_file.keys())))
        self.plaintext.appendPlainText('--- *** ---')

        self.keysCombo.currentTextChanged.disconnect()

        self.keysCombo.clear()
        self.keysCombo.addItems(list(self.npz_loaded_file.keys()))

        self.keysCombo.currentTextChanged.connect(self.comboKeyChanged)

        for k in k_files:
            self.plaintext.appendPlainText(k + ' - shape: ' + str(self.npz_loaded_file[k].shape) + ' - :')
            self.plaintext.appendPlainText(str(self.npz_loaded_file[k]))
            self.plaintext.appendPlainText('---')

        # print (np_filename)

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
