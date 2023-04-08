# Nama  : Gempar Priadi
# Kelas : R1/T21A
# Nim   : 210511036

class PenulisBuku:
    def __init__(self, name):
        self.name = name
        self.karya = Karya()
        print("Penulis Gempar Priadi")

class JudulBuku:
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
        print("Judul: ", item.name,", Tahun ", item.sience)
    
    def remove_item(self, item):
        self.items.remove(item)

penulis = PenulisBuku(" ")
judul1 = JudulBuku("Cara Cepat Belajar Bahasa Pemograman PYTHON Lanjut ", 2023)
judul2 = JudulBuku("Cara Cepat Belajar Bahasa Pemograman PYTHON Dasar", 2022)
judul3 = JudulBuku("Cara Menjadi WEB Developer", 2021)
print("-"*150)
penulis.karya.add_item1(judul1)
penulis.karya.add_item2(judul2)
penulis.karya.add_item3(judul3)
penulis.karya.items
print("-"*150)
print(" ")
