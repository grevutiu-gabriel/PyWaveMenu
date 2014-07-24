__author__ = 'helder'
'''
    This began at July,24 2014

'''

import sys, os, time

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import *


""" MainWindow class """
class Main(QMainWindow):
    # Janela principal
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)

        # Loading the UI file
        loadUi('mainwindow.ui', self)



        # conectando os sinais aos slots


    # __init__()

    @pyqtSlot()
    def close(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = Main()
    mainwindow.setWindowTitle('PyWaveMenu v.0.1')
    mainwindow.show()
    sys.exit(app.exec_())