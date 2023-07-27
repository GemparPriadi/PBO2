import requests
import json
class Pengembalian:
    def __init__(self):
        self.__id=None
        self.__kode_anggota = None
        self.__tanggal_pengembalian = None
        self.__denda = None
        self.__id_buku = None
        self.__id_anggota = None
        self.__id_admin = None
        self.__url = "http://localhost/perpustakaan/pengembalian_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def kode_anggota(self):
        return self.__kode_anggota
        
    @kode_anggota.setter
    def kode_anggota(self, value):
        self.__kode_anggota = value
    @property
    def tanggal_pengembalian(self):
        return self.__tanggal_pengembalian
        
    @tanggal_pengembalian.setter
    def tanggal_pengembalian(self, value):
        self.__tanggal_pengembalian = value
    @property
    def denda(self):
        return self.__denda
        
    @denda.setter
    def denda(self, value):
        self.__denda = value
    @property
    def id_buku(self):
        return self.__id_buku
        
    @id_buku.setter
    def id_buku(self, value):
        self.__id_buku = value
    @property
    def id_anggota(self):
        return self.__id_anggota
        
    @id_anggota.setter
    def id_anggota(self, value):
        self.__id_anggota = value
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
    def get_by_kode_anggota(self, kode_anggota):
        url = self.__url+"?kode_anggota="+kode_anggota
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['id_pengembalian']
            self.__kode_anggota = item['kode_anggota']
            self.__tanggal_pengembalian = item['tanggal_pengembalian']
            self.__denda = item['denda']
            self.__id_buku = item['id_buku']
            self.__id_anggota = item['id_anggota']
            self.__id_admin = item['id_admin']
        return data
    def simpan(self):
        payload = {
            "kode_anggota":self.__kode_anggota,
            "tanggal_pengembalian":self.__tanggal_pengembalian,
            "denda":self.__denda,
            "id_buku":self.__id_buku,
            "id_anggota":self.__id_anggota,
            "id_admin":self.__id_admin
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_kode_anggota(self, kode_anggota):
        url = self.__url+"?kode_anggota="+kode_anggota
        payload = {
            "kode_anggota":self.__kode_anggota,
            "tanggal_pengembalian":self.__tanggal_pengembalian,
            "denda":self.__denda,
            "id_buku":self.__id_buku,
            "id_anggota":self.__id_anggota,
            "id_admin":self.__id_admin
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_kode_anggota(self,kode_anggota):
        url = self.__url+"?kode_anggota="+kode_anggota
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text
