import requests
import json
class Admin:
    def __init__(self):
        self.__id=None
        self.__kode_admin = None
        self.__nama_admin = None
        self.__no_telp = None
        self.__alamat = None
        self.__url = "http://localhost/perpustakaan/admin_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def kode_admin(self):
        return self.__kode_admin
        
    @kode_admin.setter
    def kode_admin(self, value):
        self.__kode_admin = value
    @property
    def nama_admin(self):
        return self.__nama_admin
        
    @nama_admin.setter
    def nama_admin(self, value):
        self.__nama_admin = value
    @property
    def no_telp(self):
        return self.__no_telp
        
    @no_telp.setter
    def no_telp(self, value):
        self.__no_telp = value
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
    def get_by_kode_admin(self, kode_admin):
        url = self.__url+"?kode_admin="+kode_admin
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['id_admin']
            self.__kode_admin = item['kode_admin']
            self.__nama_admin = item['nama_admin']
            self.__no_telp = item['no_telp']
            self.__alamat = item['alamat']
        return data
    def simpan(self):
        payload = {
            "kode_admin":self.__kode_admin,
            "nama_admin":self.__nama_admin,
            "no_telp":self.__no_telp,
            "alamat":self.__alamat
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_kode_admin(self, kode_admin):
        url = self.__url+"?kode_admin="+kode_admin
        payload = {
            "kode_admin":self.__kode_admin,
            "nama_admin":self.__nama_admin,
            "no_telp":self.__no_telp,
            "alamat":self.__alamat
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_kode_admin(self,kode_admin):
        url = self.__url+"?kode_admin="+kode_admin
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text
