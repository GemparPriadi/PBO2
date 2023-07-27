import requests
import json
class Peminjaman:
    def __init__(self):
        self.__id=None
        self.__kode_peminjaman = None
        self.__tanggal_pinjam = None
        self.__tanggal_kembali = None
        self.__id_anggota = None
        self.__id_buku = None
        self.__id_admin = None
        self.__url = "http://localhost/perpustakaan/peminjaman_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def kode_peminjaman(self):
        return self.__kode_peminjaman
        
    @kode_peminjaman.setter
    def kode_peminjaman(self, value):
        self.__kode_peminjaman = value
    @property
    def tanggal_pinjam(self):
        return self.__tanggal_pinjam
        
    @tanggal_pinjam.setter
    def tanggal_pinjam(self, value):
        self.__tanggal_pinjam = value
    @property
    def tanggal_kembali(self):
        return self.__tanggal_kembali
        
    @tanggal_kembali.setter
    def tanggal_kembali(self, value):
        self.__tanggal_kembali = value
    @property
    def id_anggota(self):
        return self.__id_anggota
        
    @id_anggota.setter
    def id_anggota(self, value):
        self.__id_anggota = value
    @property
    def id_buku(self):
        return self.__id_buku
        
    @id_buku.setter
    def id_buku(self, value):
        self.__id_buku = value
    @property
    def id_admin(self):
        return self.__id_admin
        
    @id_admin.setter
    def id_admin(self, value):
        self.__id_admin = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_kode_peminjaman(self, kode_peminjaman):
        url = self.__url+"?kode_peminjaman="+kode_peminjaman
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['id_peminjaman']
            self.__kode_peminjaman = item['kode_peminjaman']
            self.__tanggal_pinjam = item['tanggal_pinjam']
            self.__tanggal_kembali = item['tanggal_kembali']
            self.__id_anggota = item['id_anggota']
            self.__id_buku = item['id_buku']
            self.__id_admin = item['id_admin']
        return data
    def simpan(self):
        payload = {
            "kode_peminjaman":self.__kode_peminjaman,
            "tanggal_pinjam":self.__tanggal_pinjam,
            "tanggal_kembali":self.__tanggal_kembali,
            "id_anggota":self.__id_anggota,
            "id_buku":self.__id_buku,
            "id_admin":self.__id_admin
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_kode_peminjaman(self, kode_peminjaman):
        url = self.__url+"?kode_peminjaman="+kode_peminjaman
        payload = {
            "kode_peminjaman":self.__kode_peminjaman,
            "tanggal_pinjam":self.__tanggal_pinjam,
            "tanggal_kembali":self.__tanggal_kembali,
            "id_anggota":self.__id_anggota,
            "id_buku":self.__id_buku,
            "id_admin":self.__id_admin
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_kode_peminjaman(self,kode_peminjaman):
        url = self.__url+"?kode_peminjaman="+kode_peminjaman
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text
