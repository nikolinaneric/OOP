from abc import ABC, abstractmethod

class Posuda_za_voce(ABC):
    @abstractmethod
    def dodaj_vocku(self):
        pass
    
    @abstractmethod
    def broj_vocki(self):
        pass
    
    @abstractmethod
    def preostali_prostor(self):
        pass

class Cjediljka(ABC):
    @abstractmethod
    def cijedjenje(self):
        pass
