#!/usr/bin/python
import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from ui.mainwindow import MainWindow


def main():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow._open_home_panel()
    mainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()