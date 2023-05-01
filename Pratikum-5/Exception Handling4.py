list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
try:
    value = list[20]
except IndexError:
    print("Index yang diminta melebihi jumlah elemen dalam list!")