# Nama  : Gempar Priadi
# Kelas : R1 semester 4
# Nim   : 210511036
# PBO Lanjut


class celcius:
    def __int__(self, C):
        self.celcius = C

    def celcius_to_reamur(c):
        r = (4/5) * c
        return r
    
    def celcius_to_kelvin(c):
        k = c + 273
        return k

    def celcius_to_fahrenheit(c):
        f = (9/5)* c + 32
        return f

C = 60 
R = celcius.celcius_to_reamur(C)
print("Konversi", C,"derajat Celcius adalah:",R,"derajat Reamur")

C = 75 
F = (9/5) * C + 32
print("Konversi", C,"derajat Celcius adalah:",F,"derajat fahrenheit")

C = 90 
K = celcius.celcius_to_kelvin(C)
print("Konversi", C,"derajat Celcius adalah:",K,"derajat Kelvin")