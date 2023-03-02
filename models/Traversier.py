import datetime

class Traversier:
    def __init__(self, nom: str, capaciteVehicule: int, capacitePersonne: int, anneeFabrication: datetime.date, dateMiseService: datetime.date):
        self.nom = nom
        self.capaciteVehicule = capaciteVehicule
        self.capacitePersonne = capacitePersonne
        self.anneeFabrication = anneeFabrication
        self.dateMiseService = dateMiseService