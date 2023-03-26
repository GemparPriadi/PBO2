class Manusia:
    
    def __init__ (self, nama, umur): 
        self.nama = nama
        self.umur = umur

    def kegiatan(self):
        print(f"{self.nama} sedang olahraga.")

class Person(Manusia):
    def __init__(self, nama, umur, tanggal_lahir):
        super(). __init__ (nama, umur) 
        self.tanggal_lahir = tanggal_lahir

    def olahraga(self):
        print(f"{self.nama} sedang olahraga {self.tanggal_lahir} basket.")

PersonA = Person("Gempar Priadi", 20, "Di lapangan") 
PersonA.kegiatan()
PersonA.olahraga()