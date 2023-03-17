# Nama  : Gempar Priadi
# Kelas : R1 semester 4
# Nim   : 210511036
# PBO Lanjut


class Fahrenheit:
    def __int__(self, F):
        self.Fahrenheit = F

    def fahrenheit_to_reamur(F):
        R = 4/9 * (F - 32) 
        return R
    
    def fahrenheit_to_kelvin(F):
        K = (5/9) * F + 273
        return K

    def fahrenheit_to_celcius(F):
        C = (5/9) * F - 32
        return C

F = 75 
R = Fahrenheit.fahrenheit_to_reamur(F)
print("Konversi", F,"derajat Fahrenheit adalah:",R,"derajat Reamur")

F = 45 
K = Fahrenheit.fahrenheit_to_kelvin(F)
print("Konversi", F,"derajat Fahrenheit adalah:",K,"derajat Kelvin")

F = 55
C = Fahrenheit.fahrenheit_to_celcius(F)
print("Konversi", F,"derajat Fahrenheit adalah:",C,"derajat Celcius")

class Reamur:
    def __int__(self, R):
        self.Reamur = R

    def reamur_to_fahrenheit(R):
        F = (R * 2.25) + 32
        return F

    def reamur_to_kelvin(R):
        K = ( R ) + 273.15
        return K

    def reamur_to_celcius(R):
        C = R / 0.8
        return C
    
print("-" * 150)  
R = 24 
F = Reamur.reamur_to_fahrenheit(R)
print("Konversi", R,"derajat Reamur adalah:",F,"derajat Fahrenheit")

R = 55
K = Reamur.reamur_to_kelvin(R)
print("Konversi", R,"derajat Reamur adalah:",F,"derajat Kelvin")

R = 77 
F = Reamur.reamur_to_celcius(R)
print("Konversi", R,"derajat Reamur adalah:",F,"derajat Fahrenheit")


class Kelvin:
    def __int__(self, K):
        self.Kelvin = K

    def kelvin_to_fahrenheit(K):
        F = (K * 9/5) - 459.67
        return F

    def kelvin_to_reamur(K):
        R = 4/5 * (K -  273)
        return R

    def kelvin_to_celcius(K):
        C = K - 273.15
        return C

print("-" * 150)
  
K = 40 
F = Kelvin.kelvin_to_fahrenheit(K)
print("Konversi", K,"derajat Kelvin adalah:",F,"derajat Fahrenheit")

K = 80 
R = Kelvin.kelvin_to_reamur(K)
print("Konversi", K,"derajat Kelvin adalah:",F,"derajat Reamur")

K = 20 
F = Kelvin.kelvin_to_celcius(K)
print("Konversi", K,"derajat Kelvin adalah:",F,"derajat Celcius")

print("-"*150)