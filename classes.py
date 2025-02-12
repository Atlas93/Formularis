class Alumne:
    def __init__(self, nom, cognoms, curs):
        self.nom = nom
        self.congnoms = cognoms
        self.curs = curs

    def MostrarInfo(self):
        return f"{self.nom} {self.congnoms} curs: {self.curs}"

    def convertir_a_json(self):
        return {
            "Nom": self.nom,
            "Cognom": self.congnoms,
            "Curs": self.curs
        }
    
    @classmethod
    def convertir_de_json(cls, data):
        return cls(data["Nom"], data["Cognom"], data["Curs"])
