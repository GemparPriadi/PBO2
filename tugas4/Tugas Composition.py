# Nama  : Gempar Priadi
# Kelas : R1/T21A
# Nim   : 210511036

class Perusahaan:
    def __init__(self, name):
        self.name = name
        self.karyawan = Karyawan()
        print("PT. The Univenus")

class Data:
    def __init__(self, name, sience, placed):
        self.name = name
        self.sience = sience
        self.placed = placed

class Karyawan:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print("Nama: ",item.name,",Sejak", item.sience, "penempatan",item.placed)

    def remove_item(self, item):
        self.items.remove(item)

perusahaan = Perusahaan(" ")
data1 = Data("Gempar Priadi", 2020, "Bekasi")
data2 = Data("Lionel Messi", 2019,"Jakarta Pusat")
data3 = Data("Neymar Jr", 2018, "Bandung")
data4 = Data("Maguire",2022,"Cirebon")
print("-"*150)
perusahaan.karyawan.add_item(data1)
perusahaan.karyawan.add_item(data2)
perusahaan.karyawan.add_item(data3)
perusahaan.karyawan.add_item(data4)
perusahaan.karyawan.items
print("-"*150)
print(" ")
