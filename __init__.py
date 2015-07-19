'''
    This started in July 24th 2014
'''

import sys, os, time

from PyQt4.QtGui import QApplication, QMainWindow
from PyQt4.QtCore import *
from PyQt4.uic import *

import pywt

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

""" MainWindow class """
class Main(QMainWindow):
    # Janela principal
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)

        # Loading the UI file
        loadUi('mainwindow.ui', self)


        # the plot
        self.figure = plt.figure()
        
        # canvas will show the plot itself
        self.canvas = FigureCanvas(self.figure)

        # matplotlib toolbar
        self.toolbar = NavigationToolbar(self.canvas, self)
        
        self.plotLayout.addWidget(self.toolbar)
        self.plotLayout.addWidget(self.canvas)

        # connecting signals to slots
        self.actionQuit.triggered.connect(self.close)
        self.cbbWaveletFamily.activated[str].connect(self.populateCBBWavelet)
        
        # inicialization functions
        self.populateWindow()
        
    # __init__()


    def populateWindow(self):
        self.cbbWaveletFamily.addItems(pywt.families())
        self.cbbWavelet.addItems(pywt.wavelist('haar'))
        
    # populateWindow(self)
    
    
    def populateCBBWavelet(self, family):
        self.cbbWavelet.clear()
        self.cbbWavelet.addItems(pywt.wavelist(family))
        
    # populateCBBWavelet(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = Main()
    mainwindow.setWindowTitle('PyWaveMenu v.0.1')
    mainwindow.show()
    sys.exit(app.exec_())