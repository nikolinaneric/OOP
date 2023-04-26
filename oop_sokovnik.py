# Sokovnik je programiran da izvrši 100 akcija ceđenja i ubacivanja jabuka, pri čemu se
# ceđenje voća radi sa verovatnoćom 30%, a dodavanje jabuke sa verovatnoćom od 70%.
from random import random, uniform
from interfejs_sokovnik import *
class Voce:
    def __init__(self, naziv, tezina):
        self.naziv_vocke = naziv
        self.tezina_vocke = tezina

class Jabuka(Voce):
    def __init__(self,naziv,tezina,crvljivost):
        super().__init__(naziv,tezina)
        self.crvljivost = crvljivost

class SokovnikSingleton(Posuda_za_voce, Cjediljka):

    __instance = None

    @staticmethod
    def get_instance():
        if SokovnikSingleton.__instance == None:
            SokovnikSingleton()
        return SokovnikSingleton.__instance 
    def __init__(self):
        if SokovnikSingleton.__instance != None:
            raise Exception("Sokovnik je jedinstven")
        else:
            self.kapacitet = 30
            self.voce = []
            self.tezina_voca = 0
            SokovnikSingleton.__instance = self

    def dodaj_vocku(self,vocka):
        if self.kapacitet >= self.tezina_voca:
            if not vocka.crvljivost:
                self.voce.append(vocka)
                self.tezina_voca += float(vocka.tezina_vocke)
                return True
            else:
                return False

    def broj_vocki(self):
        return len(self.voce)

    def preostali_prostor(self):
        return(self.kapacitet - self.tezina_voca)

    def cijedjenje(self):
        self.kolicina_soka = 0
        for vocka in self.voce:
            self.kolicina_soka +=(float(vocka.tezina_vocke))*0.4
        return self.kolicina_soka



def main():
    sokovnik = SokovnikSingleton()
    vjerovatnoca_cijedjenja = 0.3
    vjerovatnoca_dodavanja_jabuke = 0.7
    vjerovatnoca_crvljivosti = 0.2
    broj_ubacivanja = 0
    broj_cijedjenja = 0
    broj_akcija = 0
    
    while broj_akcija < 100:

      
        if vjerovatnoca_dodavanja_jabuke >= random():
            if vjerovatnoca_crvljivosti >= random():
                crvljivost = True
            else:
                crvljivost = False
            tezina = round(uniform(1,3),2)
            if sokovnik.dodaj_vocku(Jabuka("Jabuka",tezina,crvljivost)):
                broj_ubacivanja = broj_ubacivanja +1
                broj_akcija = broj_ubacivanja + broj_cijedjenja
                print(f"Izvršeno je ubacivanje {broj_ubacivanja}. jabuke težine {tezina} kg. {broj_akcija}. akcija")

                
            if sokovnik.preostali_prostor() <= 0:
                print("Kolicina iscijedjenog soka je "+str(round(sokovnik.kolicina_soka,2))+" litara.")      
                raise Exception("PremasenKapacitet Expection")
                     

            if broj_akcija <100:
                if vjerovatnoca_cijedjenja >= random():
                    sokovnik.cijedjenje()
                    sokovnik.tezina_voca = 0
                    broj_cijedjenja = broj_cijedjenja +1
                    broj_akcija = broj_ubacivanja + broj_cijedjenja
                    print(f"Izvršeno je {broj_cijedjenja}. cijeđenje soka. {broj_akcija}. akcija")

    print(f"Količina iscijeđenog soka je {round(sokovnik.kolicina_soka, 2)} litara. Broj akcija {broj_akcija}.")


main()
