class Kendaraan:

    def __init__(self, jenis, merk, warna):
        self.jenis = jenis
        self.merk = merk
        self.warna = warna

    def berkendara(self):
        print("Mobil BMW ini sedang parkir.")

class SepedaMotor(Kendaraan):
    def __init__(self, jenis, merk, warna, cc):
        super().__init__(jenis, merk, warna)
        self.cc = cc

    def belok(self):    
         print("Motor Suzuki ini sedang berhenti.")

motorA = SepedaMotor("Sepeda Motor", "Suzuki", "biru", 250)
motorA.berkendara() # Output: Kendaraan ini sedang berjalan.
motorA.belok() # Output: Sepeda motor ini sedang belok.