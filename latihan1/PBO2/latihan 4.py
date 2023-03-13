class Buku:
    def __init__(self, Judul, Penulis):
        self.judul = Judul
        self.penulis = Penulis
    def info(self):
        print(f"Judul : {self.judul}\nPenulis : {self.penulis}")

Buku = Buku ("Filosi Teras", "Henry Manampiring")
Buku.info()