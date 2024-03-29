import requests
import json
class Buku:
    def __init__(self):
        self.__id=None
        self.__kode_buku = None
        self.__judul_buku = None
        self.__penulis_buku = None
        self.__penerbit_buku = None
        self.__tahun_penerbit = None
        self.__kategori_buku = None
        self.__url = "http://localhost/perpustakaan/buku_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def kode_buku(self):
        return self.__kode_buku
        
    @kode_buku.setter
    def kode_buku(self, value):
        self.__kode_buku = value
    @property
    def judul_buku(self):
        return self.__judul_buku
        
    @judul_buku.setter
    def judul_buku(self, value):
        self.__judul_buku = value
    @property
    def penulis_buku(self):
        return self.__penulis_buku
        
    @penulis_buku.setter
    def penulis_buku(self, value):
        self.__penulis_buku = value
    @property
    def penerbit_buku(self):
        return self.__penerbit_buku
        
    @penerbit_buku.setter
    def penerbit_buku(self, value):
        self.__penerbit_buku = value
    @property
    def tahun_penerbit(self):
        return self.__tahun_penerbit
        
    @tahun_penerbit.setter
    def tahun_penerbit(self, value):
        self.__tahun_penerbit = value
    @property
    def kategori_buku(self):
        return self.__kategori_buku
        
    @kategori_buku.setter
    def kategori_buku(self, value):
        self.__kategori_buku = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_kode_buku(self, kode_buku):
        url = self.__url+"?kode_buku="+kode_buku
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['id_buku']
            self.__kode_buku = item['kode_buku']
            self.__judul_buku = item['judul_buku']
            self.__penulis_buku = item['penulis_buku']
            self.__penerbit_buku = item['penerbit_buku']
            self.__tahun_penerbit = item['tahun_penerbit']
            self.__kategori_buku = item['kategori_buku']
        return data
    def simpan(self):
        payload = {
            "kode_buku":self.__kode_buku,
            "judul_buku":self.__judul_buku,
            "penulis_buku":self.__penulis_buku,
            "penerbit_buku":self.__penerbit_buku,
            "tahun_penerbit":self.__tahun_penerbit,
            "kategori_buku":self.__kategori_buku
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_kode_buku(self, kode_buku):
        url = self.__url+"?kode_buku="+kode_buku
        payload = {
            "kode_buku":self.__kode_buku,
            "judul_buku":self.__judul_buku,
            "penulis_buku":self.__penulis_buku,
            "penerbit_buku":self.__penerbit_buku,
            "tahun_penerbit":self.__tahun_penerbit,
            "kategori_buku":self.__kategori_buku
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_kode_buku(self,kode_buku):
        url = self.__url+"?kode_buku="+kode_buku
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text
