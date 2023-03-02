import sys
from controllers.MainController import MainWindow
from PyQt5 import QtWidgets, uic
import config


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
