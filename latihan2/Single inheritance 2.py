class Manusia:
    
    def __init__ (self, nama, umur): 
        self.nama = nama
        self.umur = umur

    def berbicara(self):
        print(f"{self.nama} sedang berbicara.")

class Dosen(Manusia):
    def __init__(self, nama, umur, nip):
        super(). __init__ (nama, umur) 
        self.nip = nip

    def mengajar(self):
        print(f"{self.nama} dengan NIP {self.nip} sedang mengajar.")

dosenA = Dosen("Gempar Priadi", 20, "210511036") 
dosenA.berbicara() # Output: Budi sedang berbicara.
dosenA.mengajar() # Output: Gempar Priadi dengan NIP 210511036 sedang mengajar.
