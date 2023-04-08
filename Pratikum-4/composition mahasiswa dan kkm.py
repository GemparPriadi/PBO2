# Nama  : Gempar Priadi
# Kelas : R1/T21A
# Nim   : 210511036

class Mahasiswa:
    def __init__(self, name):
        self.name = name
        self.anggota = Anggota()
        print("Daftar Nama Mahasiswa Kelompok KKM")

class Kelompok_KKM:
    def __init__(self, name):
        self.name = name

class Anggota:
    def __init__(self):
        self.items = []

    def add_item1(self, item):
        self.items.append(item)
        print("Kelompok 1: ", item.name)

    def add_item2(self, item):
        self.items.append(item)
        print("Kelompok 2: ", item.name)
        
    def add_item3(self, item):
        self.items.append(item)
        print("Kelompok 3: ", item.name)


    def remove_item(self, item):
        self.items.remove(item)

mahasiswa = Mahasiswa(" ")
kelompok1 = Kelompok_KKM("Gempar Priadi, Adi Sasono, Abdurrohman.")
kelompok2 = Kelompok_KKM("Sahrul, Muhammad Khafid Suryana, Della Nur Fadillah.")
kelompok3 = Kelompok_KKM("Muhammad Ridwan, Tretan Muslim, Coki Pardede.")
print("-"*150)
mahasiswa.anggota.add_item1(kelompok1)
mahasiswa.anggota.add_item2(kelompok2)
mahasiswa.anggota.add_item3(kelompok3)
mahasiswa.anggota.items
print("-"*150)
print(" ")
