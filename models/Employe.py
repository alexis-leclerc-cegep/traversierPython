import datetime
import Personne

class Employe(Personne):
    def __init__(self, nom: str, adresse: str, ville: str, province: str, codePostal: str, telephone: str, courriel: str, noEmploye: int, NAS: str, dateEmbauche: datetime, dateArret: datetime):
        super().__init__(nom, adresse, ville, province, codePostal, telephone, courriel)
        self.noEmploye = noEmploye
        self.NAS = NAS
        self.dateEmbauche = dateEmbauche
        self.dateArret = dateArret

    def __str__(self):
        return self.nom + " " + self.noEmploye

