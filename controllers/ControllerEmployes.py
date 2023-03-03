from PyQt5.QtGui import QRegExpValidator, QRegularExpressionValidator, QValidator

from models.Employe import Employe, EmployeListModel
from PyQt5.QtCore import pyqtSlot, QDateTime, QDate
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QTabWidget, QPushButton, QSpinBox, QLineEdit, QCalendarWidget, QDateEdit, \
    QComboBox
import config
import xml.etree.ElementTree as ET
import re


class EmailLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

        print("init")
        validator = QRegularExpressionValidator(QtCore.QRegularExpression(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"), self)
        self.setValidator(validator)

    def focusInEvent(self, event):
        print("focus in")
        super().focusInEvent(event)

    def focusOutEvent(self, event):
        print("focus out")
        input_text = self.text()
        if self.validator().validate(input_text, 0)[0] != QValidator.Acceptable:
            print("Invalid email address")

        super().focusOutEvent(event)




class TabEmployeController:
    def __init__(self, tab_widget):
        self.tab_widget = tab_widget
        self.btnAjouter = tab_widget.findChild(QPushButton, 'btnAjouter')
        self.btnAjouter.clicked.connect(self.ajouter)

        self.model = EmployeListModel()

        self.edtNomEmploye = tab_widget.findChild(QLineEdit, 'edtNomEmploye')
        self.edtAdresseEmploye = tab_widget.findChild(QLineEdit, 'edtAdresseEmploye')
        self.edtVilleEmploye = tab_widget.findChild(QLineEdit, 'edtVilleEmploye')
        self.cbxProvince = tab_widget.findChild(QComboBox, 'cbxProvince')
        self.edtCodePostal = tab_widget.findChild(QLineEdit, 'edtCodePostal')
        self.edtTelephone = tab_widget.findChild(QLineEdit, 'edtTelephone')

        self.edtCourriel = tab_widget.findChild(QLineEdit, 'edtCourriel')
        self.edtCourriel.setModel(EmailLineEdit())

        self.edtNoEmploye = tab_widget.findChild(QLineEdit, 'edtNoEmploye')
        self.edtNAS = tab_widget.findChild(QLineEdit, 'edtNAS')
        self.dtEmbauche = tab_widget.findChild(QDateEdit, 'dtEmbauche')
        self.dtArret = tab_widget.findChild(QDateEdit, 'dtArret')

        self.dtEmbauche.setDateTime(QDateTime.currentDateTime())
        self.dtArret.setDateTime(QDateTime.currentDateTime())

        self.edtTelephone.setInputMask("999-999-9999")
        self.edtCodePostal.setInputMask("A9A 9A9")
        self.edtNAS.setInputMask("999 999 999")

        self.edtCourriel.editingFinished.connect(self.verifierCourriel)

    def displayError(self, error):
        print(error)

    def verifierCourriel(self):
        # check if the text field is a courriel
        print(self.edtCourriel.text())




    def ajouter(self):
        print("ajouter")
        try:
            print(self.edtCourriel.validator.state)
            # check if ever

            # do some validation

            self.model.ajouter(
                Employe(self.edtNomEmploye.text(), self.edtAdresseEmploye.text(), self.edtVilleEmploye.text(),
                        self.cbxProvince.currentText(), self.edtCodePostal.text(), self.edtTelephone.text(),
                        self.edtCourriel.text(), self.edtNoEmploye.text(), self.edtNAS.text(),
                        self.dtEmbauche.date().toPyDate(), self.dtArret.date().toPyDate()))
        except Exception as e:
            print(e)
