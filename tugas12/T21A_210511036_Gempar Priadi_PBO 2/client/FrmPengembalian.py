import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Pengembalian import *
class FrmPengembalian:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("750x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        Label(mainFrame, text='Kode_Anggota:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Tanggal_Pengembalian:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Denda:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='ID_Buku:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='ID_Anggota:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='ID_Admin:').grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtKode_anggota = Entry(mainFrame) 
        self.txtKode_anggota.grid(row=0, column=1, padx=5, pady=5)
        self.txtKode_anggota.bind('<Return>', self.onCari)
        # Textbox
        self.txtTanggal_pengembalian = Entry(mainFrame) 
        self.txtTanggal_pengembalian.grid(row=1, column=1, padx=5, pady=5)
        # Textbox
        self.txtDenda = Entry(mainFrame) 
        self.txtDenda.grid(row=2, column=1, padx=5, pady=5)
        # Textbox
        self.txtId_buku = Entry(mainFrame) 
        self.txtId_buku.grid(row=3, column=1, padx=5, pady=5)
        # Textbox
        self.txtId_anggota = Entry(mainFrame) 
        self.txtId_anggota.grid(row=4, column=1, padx=5, pady=5)
        # Textbox
        self.txtId_admin = Entry(mainFrame) 
        self.txtId_admin.grid(row=5, column=1, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('id_pengembalian','kode_anggota','tanggal_pengembalian','denda','id_buku','id_anggota','id_admin')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id_pengembalian', text='ID_Pengembalian')
        self.tree.column('id_pengembalian', width="110")
        self.tree.heading('kode_anggota', text='Kode_Anggota')
        self.tree.column('kode_anggota', width="100")
        self.tree.heading('tanggal_pengembalian', text='Tanggal_Pengembalian')
        self.tree.column('tanggal_pengembalian', width="140")
        self.tree.heading('denda', text='Denda')
        self.tree.column('denda', width="80")
        self.tree.heading('id_buku', text='ID_Buku')
        self.tree.column('id_buku', width="80")
        self.tree.heading('id_anggota', text='ID_Anggota')
        self.tree.column('id_anggota', width="90")
        self.tree.heading('id_admin', text='ID_Admin')
        self.tree.column('id_admin', width="90")
        # set tree position
        self.tree.place(x=0, y=200)
        
    def onClear(self, event=None):
        self.txtKode_anggota.delete(0,END)
        self.txtKode_anggota.insert(END,"")
        self.txtTanggal_pengembalian.delete(0,END)
        self.txtTanggal_pengembalian.insert(END,"")
        self.txtDenda.delete(0,END)
        self.txtDenda.insert(END,"")
        self.txtId_buku.delete(0,END)
        self.txtId_buku.insert(END,"")
        self.txtId_anggota.delete(0,END)
        self.txtId_anggota.insert(END,"")
        self.txtId_admin.delete(0,END)
        self.txtId_admin.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data pengembalian
        obj = Pengembalian()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["id_pengembalian"],d["kode_anggota"],d["tanggal_pengembalian"],d["denda"],d["id_buku"],d["id_anggota"],d["id_admin"]))
    def onCari(self, event=None):
        kode_anggota = self.txtKode_anggota.get()
        obj = Pengembalian()
        a = obj.get_by_kode_anggota(kode_anggota)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        kode_anggota = self.txtKode_anggota.get()
        obj = Pengembalian()
        res = obj.get_by_kode_anggota(kode_anggota)
        self.txtTanggal_pengembalian.delete(0,END)
        self.txtTanggal_pengembalian.insert(END,obj.tanggal_pengembalian)
        self.txtDenda.delete(0,END)
        self.txtDenda.insert(END,obj.denda)
        self.txtId_buku.delete(0,END)
        self.txtId_buku.insert(END,obj.id_buku)
        self.txtId_anggota.delete(0,END)
        self.txtId_anggota.insert(END,obj.id_anggota)
        self.txtId_admin.delete(0,END)
        self.txtId_admin.insert(END,obj.id_admin)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        kode_anggota = self.txtKode_anggota.get()
        tanggal_pengembalian = self.txtTanggal_pengembalian.get()
        denda = self.txtDenda.get()
        id_buku = self.txtId_buku.get()
        id_anggota = self.txtId_anggota.get()
        id_admin = self.txtId_admin.get()
        # create new Object
        obj = Pengembalian()
        obj.kode_anggota = kode_anggota
        obj.tanggal_pengembalian = tanggal_pengembalian
        obj.denda = denda
        obj.id_buku = id_buku
        obj.id_anggota = id_anggota
        obj.id_admin = id_admin
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_kode_anggota(kode_anggota)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        kode_anggota = self.txtKode_anggota.get()
        obj = Pengembalian()
        obj.kode_anggota = kode_anggota
        if(self.ditemukan==True):
            res = obj.delete_by_kode_anggota(kode_anggota)
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
    aplikasi = FrmPengembalian(root2, "Aplikasi Data Pengembalian")
    root2.mainloop()
