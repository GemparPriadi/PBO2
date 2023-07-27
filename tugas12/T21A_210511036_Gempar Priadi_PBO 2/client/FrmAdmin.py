import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Admin import *
class FrmAdmin:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("450x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        Label(mainFrame, text='Kode_Admin:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Nama_Admin:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='No_Telp:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Alamat:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtKode_admin = Entry(mainFrame) 
        self.txtKode_admin.grid(row=0, column=1, padx=5, pady=5)
        self.txtKode_admin.bind('<Return>',self.onCari)
        # Textbox
        self.txtNama_admin = Entry(mainFrame) 
        self.txtNama_admin.grid(row=1, column=1, padx=5, pady=5)
        # Textbox
        self.txtNo_telp = Entry(mainFrame) 
        self.txtNo_telp.grid(row=2, column=1, padx=5, pady=5)
        # Textbox
        self.txtAlamat = Entry(mainFrame) 
        self.txtAlamat.grid(row=3, column=1, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('id_admin','kode_admin','nama_admin','no_telp','alamat')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id_admin', text='ID_Admin')
        self.tree.column('id_admin', width="70")
        self.tree.heading('kode_admin', text='Kode_Admin')
        self.tree.column('kode_admin', width="80")
        self.tree.heading('nama_admin', text='Nama_Admin')
        self.tree.column('nama_admin', width="100")
        self.tree.heading('no_telp', text='No_Telp')
        self.tree.column('no_telp', width="100")
        self.tree.heading('alamat', text='Alamat')
        self.tree.column('alamat', width="70")
        # set tree position
        self.tree.place(x=0, y=200)
        
    def onClear(self, event=None):
        self.txtKode_admin.delete(0,END)
        self.txtKode_admin.insert(END,"")
        self.txtNama_admin.delete(0,END)
        self.txtNama_admin.insert(END,"")
        self.txtNo_telp.delete(0,END)
        self.txtNo_telp.insert(END,"")
        self.txtAlamat.delete(0,END)
        self.txtAlamat.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data admin
        obj = Admin()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["id_admin"],d["kode_admin"],d["nama_admin"],d["no_telp"],d["alamat"]))
    def onCari(self, event=None):
        kode_admin = self.txtKode_admin.get()
        obj = Admin()
        a = obj.get_by_kode_admin(kode_admin)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        kode_admin = self.txtKode_admin.get()
        obj = Admin()
        res = obj.get_by_kode_admin(kode_admin)
        self.txtNama_admin.delete(0,END)
        self.txtNama_admin.insert(END,obj.nama_admin)
        self.txtNo_telp.delete(0,END)
        self.txtNo_telp.insert(END,obj.no_telp)
        self.txtAlamat.delete(0,END)
        self.txtAlamat.insert(END,obj.alamat)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        kode_admin = self.txtKode_admin.get()
        nama_admin = self.txtNama_admin.get()
        no_telp = self.txtNo_telp.get()
        alamat = self.txtAlamat.get()
        # create new Object
        obj = Admin()
        obj.kode_admin = kode_admin
        obj.nama_admin = nama_admin
        obj.no_telp = no_telp
        obj.alamat = alamat
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_kode_admin(kode_admin)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        kode_admin = self.txtKode_admin.get()
        obj = Admin()
        obj.kode_admin = kode_admin
        if(self.ditemukan==True):
            res = obj.delete_by_kode_admin(kode_admin)
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        
        self.onClear()
            
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
if __name__ == '__main__':
    root2 = tk.Tk()
    aplikasi = FrmAdmin(root2, "Aplikasi Data Admin")
    root2.mainloop()
