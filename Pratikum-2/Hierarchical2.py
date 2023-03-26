class Siswa:
    def __init__(self, name, nisn, umur):
        self.name = name
        self.nisn = nisn
        self.umur = umur
    def get_name(self):
        return self.name
    def get_nisn(self):
        return self.nisn
    def umur(self):
        return self.umur
    def display_info(self):
        print(f"Name : {self.name}")
        print(f"Nomor Induk Siswa Nasional : {self.nisn}")
        print(f"Umur : {self.umur}")
class Formal(Siswa):
    def __init__(self, name, nisn, umur, sekolah):
        super().__init__(name, nisn, umur)
        self.sekolah = sekolah
    def get_sekolah(self):
        return self.sekolah
class Organisasi(Siswa):
    def __init__(self, name, nisn, umur, sekolah_dasar):
        super().__init__(name, nisn, umur)
        self.sekolah_dasar = sekolah_dasar
    def get_sekolah_dasar(self):
        return self.sekolah_dasar
# Hierarchical Inheritance
class AnggotaPramuka(Organisasi):
    def __init__(self, name, nisn, umur, sekolah_dasar, kelas):
        super().__init__(name, nisn, umur, sekolah_dasar)
        self.kelas = kelas
    def get_kelas(self):
        return self.kelas
    def display_info(self):
        super().display_info()
        print(f"Sekolah Dasar: {self.sekolah_dasar}")
        print(f"Kelas: {self.kelas}")

AnggotaPramukaA = AnggotaPramuka("Rio Febrianto", 2001030738, 9, "SDN 1 Arjawinangun ", 3)
AnggotaPramukaA.display_info()