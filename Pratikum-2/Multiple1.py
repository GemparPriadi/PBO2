class Mahasiswa:

    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def belajar(self):
        print(self.nama, "sedang berolahraga")

class Pekerja:

    def __init__(self, nama, pekerjaan):
        self.nama = nama
        self.pekerjaan = pekerjaan

    def bekerja(self):
        print(self.nama, "sedang bermain basket")

class MahasiswaPekerja(Mahasiswa, Pekerja):
    def __init__(self, nama, nim, pekerjaan):
        Mahasiswa.__init__(self, nama, nim)
        Pekerja.__init__(self, nama, pekerjaan)

    def bersosialisasi(self):
        print(self.nama, "sedang berkendara")

mhs_pekerja = MahasiswaPekerja("Gempar Priadi", "210511036", "Programmer")
mhs_pekerja.belajar()
mhs_pekerja.bekerja()
mhs_pekerja.bersosialisasi()