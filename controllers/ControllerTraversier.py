from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QTabWidget, QPushButton


class TabTraversierController:
    def __init__(self, tab_widget):
        self.tab_widget = tab_widget
        self.btnEnregistrer = tab_widget.findChild(QPushButton, 'btnEnregistrer')
        self.btnEnregistrer.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        print("Hello World")
