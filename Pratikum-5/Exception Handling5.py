data = {"Ayam": 15, "Singa": 10, "Macan": 23}
try:
    value = data["Kerbau"]
except KeyError:
    print("Key yang dicari tidak ditemukan pada data!")