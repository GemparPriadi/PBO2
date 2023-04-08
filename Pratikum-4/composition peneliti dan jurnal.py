# Nama  : Gempar Priadi
# Kelas : R1/T21A
# Nim   : 210511036


class Penulis:
    def __init__(self, name):
        self.name = name
        self.karya = Karya()
        print("Karya Gempar Priadi")

class Judul:
    def __init__(self, name, sience):
        self.name = name
        self.sience = sience

class Karya:
    def __init__(self):
        self.items = []
        
    def add_item1(self, item):
        self.items.append(item)
        print("Judul: ", item.name,", Tahun", item.sience)

    def add_item2(self, item):
        self.items.append(item)
        print("Judul: ", item.name,", Tahun", item.sience)
    
    def add_item3(self, item):
        self.items.append(item)
        print("Judul: ", item.name,", Tahun", item.sience)

    def remove_item(self, item):
        self.items.remove(item)

penulis = Penulis(" ")
judul1 = Judul("Dashboard Information System Performa Akademik Mahasiswa", 2023)
judul2 = Judul("Transformasi Pendidikan Melalui Inovasi Teknologi", 2022)
judul3 = Judul("Analisis Kinerja Pelayanan Surat-Menyurat Berbasis Web Di SMPN 1 Panguragan Kab.Cirebon ",2021)
print("-"*150)
penulis.karya.add_item1(judul1)
penulis.karya.add_item2(judul2)
penulis.karya.add_item3(judul3)
penulis.karya.items
print("-"*150)
print(" ")