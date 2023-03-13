class Lingkaran:
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari
         
    def Luas(self):
        return 22/7 * (self.jari_jari ** 2)

Lingkaran = Lingkaran(21)
print(f"Luas Lingkaran : {Lingkaran.Luas()}")