class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
    def info(self):
        print(f"Nama : {self.nama}\nNim  : {self.nim}")

Mahasiswa = Mahasiswa ("Gempar Priadi", "210511036")
Mahasiswa.info()