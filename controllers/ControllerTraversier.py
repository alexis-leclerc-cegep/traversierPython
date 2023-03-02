from models.Traversier import Traversier
from PyQt5.QtCore import pyqtSlot, QDateTime, QDate
from PyQt5.QtWidgets import QMainWindow, QTabWidget, QPushButton, QSpinBox, QLineEdit, QCalendarWidget, QDateEdit


class TabTraversierController:
    def __init__(self, tab_widget):
        self.tab_widget = tab_widget
        self.btnEnregistrer = tab_widget.findChild(QPushButton, 'btnEnregistrer')
        self.btnEnregistrer.clicked.connect(self.on_button_clicked)

        self.edtNomTraversier = tab_widget.findChild(QLineEdit, 'edtNomTraversier')

        self.sbxCapaciteVehicule = tab_widget.findChild(QSpinBox, 'sbxCapaciteVehicule')
        self.sbxCapacitePersonne = tab_widget.findChild(QSpinBox, 'sbxCapacitePersonne')
        self.calAnneeFab = tab_widget.findChild(QDateEdit, 'calAnneeFab')
        self.calMiseService = tab_widget.findChild(QDateEdit, 'calMiseService')

        # set its datetime to todays date
        self.calAnneeFab.setDateTime(QDateTime.currentDateTime())
        self.calMiseService.setDateTime(QDateTime.currentDateTime())


    def on_button_clicked(self):
        print("Clicked")
        nom = self.edtNomTraversier.text()
        capaciteVehicule = self.sbxCapaciteVehicule.value()
        print(capaciteVehicule)
        capacitePersonne = self.sbxCapacitePersonne.value()
        print(capacitePersonne)
        anneeFabrication = self.calAnneeFab.date().toPyDate()
        print(anneeFabrication)
        dateMiseService = self.calMiseService.date().toPyDate()
        print(dateMiseService)
        print("rendu la")
        traversier = Traversier(nom, capaciteVehicule, capacitePersonne, anneeFabrication, dateMiseService)
        print(traversier)

    def closeEvent(self, event):
        print("Closing")
        event.accept()
