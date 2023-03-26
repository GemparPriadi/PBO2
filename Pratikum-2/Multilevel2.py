class MieInstan:
    def __init__(self, name):
        self.name = name
    def Rasa(self):
        print("Mie Instan Mempuyai Banyak Rasa")
class Indomie(MieInstan):
    def __init__(self, name, rasa):
        super().__init__(name)
        self.rasa = rasa
    def Rasa(self):
        print("Indomie Memiliki Rasa Yang Enak")
class IndomieAyamGeprek(Indomie):
    def __init__(self, name, rasa, asal):
        super().__init__(name, rasa)
        self.asal = asal
    def Rasa(self):
        print("Indomie Ayam Geprek Produk Dari Indonesia Memiliki Rasa Yang Enak")
        
IndomieAyamGeprekA = IndomieAyamGeprek("Indomie Ayam Geprek", "Enak", "Indonesia")
IndomieB = Indomie("Indomie Ayam Geprek", "Enak")
MieInstanC = MieInstan("Mie Instan Apa Yang Memiliki Rasa Yang Enak?")
IndomieAyamGeprekA.Rasa()
IndomieB.Rasa()
MieInstanC.Rasa()