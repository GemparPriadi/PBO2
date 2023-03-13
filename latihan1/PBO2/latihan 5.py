class PesawatTerbang:
    def __init__(self, Maskapai, Tujuan):
        self.maskapai = Maskapai
        self.tujuan = Tujuan
    def info(self):
        print(f"Maskapai : {self.maskapai}\nTujuan : {self.tujuan}")

PesawatTerbang = PesawatTerbang ("Lion Air", "Bali - Jakarta")
PesawatTerbang.info()
