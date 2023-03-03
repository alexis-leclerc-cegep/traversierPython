from PyQt5 import QtCore
from PyQt5.QtCore import Qt
import datetime
from models.Personne import Personne

class Employe(Personne):
    def __init__(self, nom: str, adresse: str, ville: str, province: str, codePostal: str, telephone: str,
                 courriel: str, noEmploye: int, NAS: str, dateEmbauche: datetime, dateArret: datetime):
        super().__init__(nom, adresse, ville, province, codePostal, telephone, courriel)
        self.noEmploye = noEmploye
        self.NAS = NAS
        self.dateEmbauche = dateEmbauche
        self.dateArret = dateArret

    def __str__(self):
        return str(self.noEmploye) + " " + self.nom

class EmployeListModel(QtCore.QAbstractListModel):
    def __init__(self, employes=None, parent=None):
        super().__init__(parent)
        self.employes = employes or []

    def data(self, index, role):
        if not index.isValid() or not (0 <= index.row() < len(self.employes)):
            return None

        employe = self.employes[index.row()]

        if role == Qt.DisplayRole: # fait comme toString
            return employe.nom + ' ' + employe.noEmploye

    def rowCount(self, index) -> int:
        return len(self.employes)

    def ajouter(self, employe):
        print("ajouter dans modele")
        self.beginInsertRows(QtCore.QModelIndex(), len(self.employes), len(self.employes))
        self.employes.append(employe)
        self.endInsertRows()

    def modifier(self, index, employe):
        self.employes[index] = employe
        self.dataChanged.emit(index, index)

    def supprimer(self, index):
        self.beginRemoveRows(QtCore.QModelIndex(), index, index)
        del self.employes[index]
        self.endRemoveRows()

    def get(self, index):
        return self.employes[index]

    def set(self, index, employe):
        self.employes[index] = employe

    def clear(self):
        self.beginResetModel()
        self.employes.clear()
        self.endResetModel()

    def getAll(self):
        return self.employes


