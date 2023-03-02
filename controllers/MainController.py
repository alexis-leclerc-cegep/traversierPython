from PyQt5 import QtWidgets, uic
import config
from controllers.ControllerTraversier import *
import xml.etree.ElementTree as ET

Ui_MainWindow, QtBaseClass = uic.loadUiType(config.qt_creator_file)

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.tabTraversier = TabTraversierController(self.tabTraversier)

