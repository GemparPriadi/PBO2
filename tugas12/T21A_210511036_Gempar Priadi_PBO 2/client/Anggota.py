import requests
import json
class Anggota:
    def __init__(self):
        self.__id=None
        self.__kode_anggota = None
        self.__nama_anggota = None
        self.__jenis_kelamin = None
        self.__prodi = None
        self.__no_tlp = None
        self.__alamat = None
        self.__url = "http://localhost/perpustakaan/anggota_api.php"
                    
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
    def nama_anggota(self):
        return self.__nama_anggota
        
    @nama_anggota.setter
    def nama_anggota(self, value):
        self.__nama_anggota = value
    @property
    def jenis_kelamin(self):
        return self.__jenis_kelamin
        
    @jenis_kelamin.setter
    def jenis_kelamin(self, value):
        self.__jenis_kelamin = value
    @property
    def prodi(self):
        return self.__prodi
        
    @prodi.setter
    def prodi(self, value):
        self.__prodi = value
    @property
    def no_tlp(self):
        return self.__no_tlp
        
    @no_tlp.setter
    def no_tlp(self, value):
        self.__no_tlp = value
    @property
    def alamat(self):
        return self.__alamat
        
    @alamat.setter
    def alamat(self, value):
        self.__alamat = value
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
            self.__id = item['id_anggota']
            self.__kode_anggota = item['kode_anggota']
            self.__nama_anggota = item['nama_anggota']
            self.__jenis_kelamin = item['jenis_kelamin']
            self.__prodi = item['prodi']
            self.__no_tlp = item['no_tlp']
            self.__alamat = item['alamat']
        return data
    def simpan(self):
        payload = {
            "kode_anggota":self.__kode_anggota,
            "nama_anggota":self.__nama_anggota,
            "jenis_kelamin":self.__jenis_kelamin,
            "prodi":self.__prodi,
            "no_tlp":self.__no_tlp,
            "alamat":self.__alamat
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_kode_anggota(self, kode_anggota):
        url = self.__url+"?kode_anggota="+kode_anggota
        payload = {
            "kode_anggota":self.__kode_anggota,
            "nama_anggota":self.__nama_anggota,
            "jenis_kelamin":self.__jenis_kelamin,
            "prodi":self.__prodi,
            "no_tlp":self.__no_tlp,
            "alamat":self.__alamat
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
