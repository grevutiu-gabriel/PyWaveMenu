'''
    This started in July 24th 2014
'''

import sys, os, time

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.uic import *


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
        exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = Main()
    mainwindow.setWindowTitle('PyWaveMenu v.0.1')
    mainwindow.show()
    sys.exit(app.exec_())