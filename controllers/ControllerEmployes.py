from PyQt5.QtGui import QRegExpValidator, QRegularExpressionValidator, QValidator

import datetime
from models.Employe import Employe, EmployeListModel
from PyQt5.QtCore import pyqtSlot, QDateTime, QDate
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QTabWidget, QPushButton, QSpinBox, QLineEdit, QCalendarWidget, QDateEdit, \
    QComboBox, QListView
import config
import xml.etree.ElementTree as ET
import re





class TabEmployeController:
    def __init__(self, tab_widget):
        self.tab_widget = tab_widget
        self.btnAjouter = tab_widget.findChild(QPushButton, 'btnAjouter')
        self.btnAjouter.clicked.connect(self.ajouter)

        self.model = EmployeListModel()

        self.listViewEmployes = tab_widget.findChild(QListView, 'listViewEmployes')

        self.listViewEmployes.setModel(self.model)

        self.edtNomEmploye = tab_widget.findChild(QLineEdit, 'edtNomEmploye')
        self.edtAdresseEmploye = tab_widget.findChild(QLineEdit, 'edtAdresseEmploye')
        self.edtVilleEmploye = tab_widget.findChild(QLineEdit, 'edtVilleEmploye')
        self.cbxProvince = tab_widget.findChild(QComboBox, 'cbxProvince')
        self.edtCodePostal = tab_widget.findChild(QLineEdit, 'edtCodePostal')
        self.edtTelephone = tab_widget.findChild(QLineEdit, 'edtTelephone')

        self.edtCourriel = tab_widget.findChild(QLineEdit, 'edtCourriel')

        self.edtNoEmploye = tab_widget.findChild(QLineEdit, 'edtNoEmploye')
        self.edtNAS = tab_widget.findChild(QLineEdit, 'edtNAS')
        self.dtEmbauche = tab_widget.findChild(QDateEdit, 'dtEmbauche')
        self.dtArret = tab_widget.findChild(QDateEdit, 'dtArret')

        self.dtEmbauche.setDateTime(QDateTime.currentDateTime())
        self.dtArret.setDateTime(QDateTime.currentDateTime())

        self.edtTelephone.setInputMask("999-999-9999")
        self.edtCodePostal.setInputMask("A9A 9A9")
        self.edtNAS.setInputMask("999 999 999")

    def displayError(self, error):
        print(error)

    def ajouter(self):
        print("ajouter")
        try:
            self.model.ajouter(
                Employe(self.edtNomEmploye.text(), self.edtAdresseEmploye.text(), self.edtVilleEmploye.text(),
                        self.cbxProvince.currentText(), self.edtCodePostal.text(), self.edtTelephone.text(),
                        self.edtCourriel.text(), self.edtNoEmploye.text(), self.edtNAS.text(),
                        self.dtEmbauche.date().toPyDate(), self.dtArret.date().toPyDate()))

            self.model.layoutChanged.emit()
        except Exception as e:
            print(e)

    def charger(self):
        tree = ET.parse(config.xmlpath)
        root = tree.getroot()

        employes = root.findall('employes')
        for employe in employes:
            print("nom")
        self.model.layoutChanged.emit()

    def closeEvent(self, event):
        tree = ET.parse(config.xmlpath)
        root = tree.getroot()
        employes = ET.SubElement(root, 'employes')
        for employe in self.model.getAll():
            employe_xml = ET.SubElement(employes, 'employe')
            ET.SubElement(employe_xml, 'nom').text = employe.nom
            ET.SubElement(employe_xml, 'adresse').text = employe.adresse
            ET.SubElement(employe_xml, 'ville').text = employe.ville
            ET.SubElement(employe_xml, 'province').text = employe.province
            ET.SubElement(employe_xml, 'codePostal').text = employe.codePostal
            ET.SubElement(employe_xml, 'telephone').text = employe.telephone
            ET.SubElement(employe_xml, 'courriel').text = employe.courriel
            ET.SubElement(employe_xml, 'noEmploye').text = employe.noEmploye
            ET.SubElement(employe_xml, 'NAS').text = employe.NAS
            ET.SubElement(employe_xml, 'dateEmbauche').text = employe.dateEmbauche.strftime("%Y-%m-%d")
            ET.SubElement(employe_xml, 'dateArret').text = employe.dateArret.strftime("%Y-%m-%d")

        ET.indent(tree)
        tree.write(config.xmlpath, encoding="utf-8", xml_declaration=True)
        event.accept()