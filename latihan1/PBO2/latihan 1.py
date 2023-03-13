class Motor:
    def __init__(self, merk, tahun_pembuatan):
        self.merk = merk
        self.tahun_pembuatan = tahun_pembuatan
    def info(self):
        print(f"motor {self.merk} tahun_pembuatan {self.tahun_pembuatan}")

Motor = Motor ("Kawasaki R250", "2022")
Motor.info()
