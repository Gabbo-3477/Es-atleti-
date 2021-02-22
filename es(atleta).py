'''
Aggiungi alla classe Atleta un metodo per visualizzare i dati del giocatore.
'''
class Atleta:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def effettua_visita_medica(self,visita_medica):
        self.visita_medica = True
    def informazioni(self):
        
        if self.visita_medica == True:
            print("L'atleta",self.name,"ha ricevuto la visita medica.")
        if self.visita_medica == False:
            print("L'atleta",self.name,"non ha ricevuto la visita medica.")
    def squadra(self, squadra):
        self.squadra = squadra
        
        dizionario = {"Nome":self.name,"Età":self.age,"Altezza":self.height,"Peso" : self.weight, "Squadra": self.squadra}
        print(dizionario)


atl1 = Atleta("Gabrile Iotti", 15, "1.75 m", "62 kg")
atl1.effettua_visita_medica(True)
atl1.informazioni()
atl1.squadra("Torre")
atl2 = Atleta("Matteo Dotti", 16, "1.70 m", "74 kg")
atl2.effettua_visita_medica(False)
atl2.informazioni()
atl2.squadra("Jolly")