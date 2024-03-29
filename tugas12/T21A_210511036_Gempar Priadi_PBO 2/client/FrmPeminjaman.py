import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Peminjaman import *
class FrmPeminjaman:
    
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
        Label(mainFrame, text='Kode_Peminjaman:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Tanggal_Pinjam:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Tanggal_Kembali:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='ID_Anggota:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='ID_Buku:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='ID_Admin:').grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtKode_Peminjaman = Entry(mainFrame) 
        self.txtKode_Peminjaman.grid(row=0, column=1, padx=5, pady=5)
        self.txtKode_Peminjaman.bind('<Return>', self.onCari)
        # Textbox
        self.txtTanggal_pinjam = Entry(mainFrame) 
        self.txtTanggal_pinjam.grid(row=1, column=1, padx=5, pady=5)
        # Textbox
        self.txtTanggal_kembali = Entry(mainFrame) 
        self.txtTanggal_kembali.grid(row=2, column=1, padx=5, pady=5)
        # Textbox
        self.txtId_anggota = Entry(mainFrame) 
        self.txtId_anggota.grid(row=3, column=1, padx=5, pady=5)
        # Textbox
        self.txtId_buku = Entry(mainFrame) 
        self.txtId_buku.grid(row=4, column=1, padx=5, pady=5)
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
        columns = ('id_peminjaman','kode_peminjaman','tanggal_pinjam','tanggal_kembali','id_anggota','id_buku','id_admin')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id_peminjaman', text='ID_Peminjaman')
        self.tree.column('id_peminjaman', width="100")
        self.tree.heading('kode_peminjaman', text='Kode_Peminjaman')
        self.tree.column('kode_peminjaman', width="120")
        self.tree.heading('tanggal_pinjam', text='Tanggal_Pinjam')
        self.tree.column('tanggal_pinjam', width="100")
        self.tree.heading('tanggal_kembali', text='Tanggal_Kembali')
        self.tree.column('tanggal_kembali', width="100")
        self.tree.heading('id_anggota', text='ID_Anggota')
        self.tree.column('id_anggota', width="100")
        self.tree.heading('id_buku', text='ID_Buku')
        self.tree.column('id_buku', width="100")
        self.tree.heading('id_admin', text='ID_Admin')
        self.tree.column('id_admin', width="100")
        # set tree position
        self.tree.place(x=0, y=200)
        
    def onClear(self, event=None):
        self.txtKode_Peminjaman.delete(0,END)
        self.txtKode_Peminjaman.insert(END,"")
        self.txtTanggal_pinjam.delete(0,END)
        self.txtTanggal_pinjam.insert(END,"")
        self.txtTanggal_kembali.delete(0,END)
        self.txtTanggal_kembali.insert(END,"")
        self.txtId_anggota.delete(0,END)
        self.txtId_anggota.insert(END,"")
        self.txtId_buku.delete(0,END)
        self.txtId_buku.insert(END,"")
        self.txtId_admin.delete(0,END)
        self.txtId_admin.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data peminjaman
        obj = Peminjaman()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["id_peminjaman"],d["kode_peminjaman"],d["tanggal_pinjam"],d["tanggal_kembali"],d["id_anggota"],d["id_buku"],d["id_admin"]))
    def onCari(self, event=None):
        kode_peminjaman = self.txtKode_Peminjaman.get()
        obj = Peminjaman()
        a = obj.get_by_kode_peminjaman(kode_peminjaman)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        kode_peminjaman = self.txtKode_Peminjaman.get()
        obj = Peminjaman()
        res = obj.get_by_kode_peminjaman(kode_peminjaman)
        self.txtTanggal_pinjam.delete(0,END)
        self.txtTanggal_pinjam.insert(END,obj.tanggal_pinjam)
        self.txtTanggal_kembali.delete(0,END)
        self.txtTanggal_kembali.insert(END,obj.tanggal_kembali)
        self.txtId_anggota.delete(0,END)
        self.txtId_anggota.insert(END,obj.id_anggota)
        self.txtId_buku.delete(0,END)
        self.txtId_buku.insert(END,obj.id_buku)
        self.txtId_admin.delete(0,END)
        self.txtId_admin.insert(END,obj.id_admin)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        kode_peminjaman = self.txtKode_Peminjaman.get()
        tanggal_pinjam = self.txtTanggal_pinjam.get()
        tanggal_kembali = self.txtTanggal_kembali.get()
        id_anggota = self.txtId_anggota.get()
        id_buku = self.txtId_buku.get()
        id_admin = self.txtId_admin.get()
        # create new Object
        obj = Peminjaman()
        obj.kode_peminjaman = kode_peminjaman
        obj.tanggal_pinjam = tanggal_pinjam
        obj.tanggal_kembali = tanggal_kembali
        obj.id_anggota = id_anggota
        obj.id_buku = id_buku
        obj.id_admin = id_admin
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_kode_peminjaman(kode_peminjaman)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        kode_peminjaman = self.txtKode_Peminjaman.get()
        obj = Peminjaman()
        obj.kode_peminjaman = kode_peminjaman
        if(self.ditemukan==True):
            res = obj.delete_by_kode_peminjaman(kode_peminjaman)
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
    aplikasi = FrmPeminjaman(root2, "Aplikasi Data Peminjaman")
    root2.mainloop()
