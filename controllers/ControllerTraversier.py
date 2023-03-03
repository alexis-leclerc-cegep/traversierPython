from models.Traversier import Traversier
from PyQt5.QtCore import pyqtSlot, QDateTime, QDate
from PyQt5.QtWidgets import QMainWindow, QTabWidget, QPushButton, QSpinBox, QLineEdit, QCalendarWidget, QDateEdit
import config
import xml.etree.ElementTree as ET


class TabTraversierController:
    def __init__(self, tab_widget):
        self.tab_widget = tab_widget
        self.btnEnregistrer = tab_widget.findChild(QPushButton, 'btnEnregistrer')
        self.btnEnregistrer.clicked.connect(self.on_save_button_clicked)

        self.edtNomTraversier = tab_widget.findChild(QLineEdit, 'edtNomTraversier')

        self.sbxCapaciteVehicule = tab_widget.findChild(QSpinBox, 'sbxCapaciteVehicule')
        self.sbxCapacitePersonne = tab_widget.findChild(QSpinBox, 'sbxCapacitePersonne')
        self.calAnneeFab = tab_widget.findChild(QDateEdit, 'calAnneeFab')
        self.calMiseService = tab_widget.findChild(QDateEdit, 'calMiseService')

        # set its datetime to todays date
        self.calAnneeFab.setDateTime(QDateTime.currentDateTime())
        self.calMiseService.setDateTime(QDateTime.currentDateTime())

        nom = self.edtNomTraversier.text()
        capaciteVehicule = self.sbxCapaciteVehicule.value()
        capacitePersonne = self.sbxCapacitePersonne.value()
        anneeFabrication = self.calAnneeFab.date().toPyDate()
        dateMiseService = self.calMiseService.date().toPyDate()

        self.charger()

        traversier = Traversier(nom, capaciteVehicule, capacitePersonne, anneeFabrication, dateMiseService)


    def on_save_button_clicked(self):
        self.enregistrer()

    def charger(self):
        tree = ET.parse(config.xmlpath)
        root = tree.getroot()
        traversier = root.find("traversier")
        nom = traversier.find("nom").text
        capaciteVehicule = int(traversier.find("capaciteVehicule").text)
        capacitePersonne = int(traversier.find("capacitePersonne").text)
        anneeFabrication = traversier.find("anneeFabrication").text
        dateMiseService = traversier.find("dateMiseService").text

        self.edtNomTraversier.setText(nom)
        self.sbxCapaciteVehicule.setValue(capaciteVehicule)
        self.sbxCapacitePersonne.setValue(capacitePersonne)
        self.calAnneeFab.setDate(QDate.fromString(anneeFabrication, "yyyy-MM-dd"))
        self.calMiseService.setDate(QDate.fromString(dateMiseService, "yyyy-MM-dd"))


    def enregistrer(self):
        root = ET.Element("root")
        traversier = ET.SubElement(root, "traversier")
        nom = ET.SubElement(traversier, "nom")
        nom.text = self.edtNomTraversier.text()
        capaciteVehicule = ET.SubElement(traversier, "capaciteVehicule")
        capaciteVehicule.text = str(self.sbxCapaciteVehicule.value())
        capacitePersonne = ET.SubElement(traversier, "capacitePersonne")
        capacitePersonne.text = str(self.sbxCapacitePersonne.value())

        anneeFabrication = ET.SubElement(traversier, "anneeFabrication")
        anneeFabrication.text = str(self.calAnneeFab.date().toPyDate())
        dateMiseService = ET.SubElement(traversier, "dateMiseService")
        dateMiseService.text = str(self.calMiseService.date().toPyDate())
        tree = ET.ElementTree(root)
        ET.indent(tree)

        # get its hash and check if its the same as file already on disk
        # if not, save it

        tree.write(config.xmlpath)
        print("Saved")


    def closeEvent(self, event):
        self.enregistrer()
        event.accept()
