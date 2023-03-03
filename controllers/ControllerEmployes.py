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

        self.charger()

        self.listViewEmployes = tab_widget.findChild(QListView, 'listViewEmployes')

        self.listViewEmployes.setModel(self.model)
        self.listViewEmployes.selectionModel().selectionChanged.connect(self.selectionChanged)

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

    def selectionChanged(self, selected, deselected):
        if len(selected.indexes()) > 0:
            employe = self.model.get(selected.indexes()[0].row())
            self.edtNomEmploye.setText(employe.nom)
            self.edtAdresseEmploye.setText(employe.adresse)
            self.edtVilleEmploye.setText(employe.ville)
            self.cbxProvince.setCurrentText(employe.province)
            self.edtCodePostal.setText(employe.codePostal)
            self.edtTelephone.setText(employe.telephone)
            self.edtCourriel.setText(employe.courriel)
            self.edtNoEmploye.setText(employe.noEmploye)
            self.edtNAS.setText(employe.NAS)
            self.dtEmbauche.setDate(employe.dateEmbauche)
            self.dtArret.setDate(employe.dateArret)
        else:
            self.edtNomEmploye.setText("")
            self.edtAdresseEmploye.setText("")
            self.edtVilleEmploye.setText("")
            self.cbxProvince.setCurrentText("")
            self.edtCodePostal.setText("")
            self.edtTelephone.setText("")
            self.edtCourriel.setText("")
            self.edtNoEmploye.setText("")
            self.edtNAS.setText("")
            self.dtEmbauche.setDate(QDate.currentDate())
            self.dtArret.setDate(QDate.currentDate())


    def charger(self):
        tree = ET.parse(config.xmlpath)
        root = tree.getroot()

        employes = root.findall('./employes/employe')
        for employe in employes:
            self.model.ajouter(
                Employe(employe.find('nom').text, employe.find('adresse').text, employe.find('ville').text,
                        employe.find('province').text, employe.find('codePostal').text, employe.find('telephone').text,
                        employe.find('courriel').text, employe.find('noEmploye').text, employe.find('NAS').text,
                        datetime.datetime.strptime(employe.find('dateEmbauche').text, "%Y-%m-%d").date(),
                        datetime.datetime.strptime(employe.find('dateArret').text, "%Y-%m-%d").date()))

        self.model.layoutChanged.emit()

    def closeEvent(self, event):
        tree = ET.parse(config.xmlpath)
        root = tree.getroot()
        employes = ET.SubElement(root, 'employes')
        for employe in self.model.getAll():
            print(employe.ville)
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

        tree = ET.ElementTree(root)

        ET.indent(tree)
        tree.write(config.xmlpath, encoding="utf-8", xml_declaration=True)
        event.accept()