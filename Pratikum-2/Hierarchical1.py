class Makhluk_Hidup:
    def __init__(self, nama, habitat):
        self.nama = nama
        self.habitat = habitat
    def get_nama(self):
        return self.nama
    def get_habitat(self):
        return self.habitat
    def display_info(self):
        print(f"nama : {self.nama}")
        print(f"habitat : {self.habitat}")
class Karnivora(Makhluk_Hidup):
    def __init__(self, nama, habitat, daging):
        super().__init__(nama, habitat)
        self.daging = daging
    def get_daging(self):
        return self.daging
class Herbivora(Makhluk_Hidup):
    def __init__(self, nama, habitat, tumbuhan):
        super().__init__(nama, habitat)
        self.tumbuhan = tumbuhan
    def get_tumbuhan(self):
        return self.tumbuhan
class Omnivora (Makhluk_Hidup):
    def __init__(self, nama, habitat, daging_tumbuhan):
        super().__init__(nama, habitat)
        self.daging_tumbuhan = daging_tumbuhan
    def get_daing_tumbuhan(self):
        return self.daging_tumbuhan
# Hierarchical Inheritance
class Harimau(Karnivora):
    def __init__(self, nama, habitat, daging, Berat):
        super().__init__(nama, habitat, daging)
        self.Berat = Berat
    def get_Berat(self):
        return self.Berat
    def display_info(self):
        super().display_info()
        print(f"Nama: {self.nama}")
        print(f"Habitat: {self.habitat}")
        print(f"Daging: {self.daging}")
        print(f"Berat: {self.Berat}")
       
HarimauA = Harimau ("Harimau Jawa", "Jawa", "Rusa", "135 KG")
HarimauA.display_info()