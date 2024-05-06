import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

musteriler = []
musteri_labels = []
satis_labels = []
destek_labels = []

class Musteri:
    def __init__(self, ad, iletisim):
        self.ad = ad
        self.iletisim = iletisim
        self.satislar = []
        self.destek_talepleri = []

    def satis_ekle(self, satis):
        self.satislar.append(satis)

    def destek_talebi_ekle(self, talep):
        self.destek_talepleri.append(talep)

class Satis:
    def __init__(self, siparis_numarasi, urunler):
        self.siparis_numarasi = siparis_numarasi
        self.urunler = urunler

class Destek:
    def __init__(self, talep_numarasi, detaylar):
        self.talep_numarasi = talep_numarasi
        self.detaylar = detaylar

window = tk.Tk()
window.title("Müşteri İlişkileri Yönetimi")

ust = tk.Frame()

musteri_frame = tk.Frame(relief=tk.GROOVE, borderwidth=1)
label = tk.Label(master=musteri_frame, text="Müşteriler")
label.pack()
separator = ttk.Separator(master=musteri_frame, orient='horizontal')
separator.pack(fill='x', padx=5)
musteri_frame.pack(fill=tk.BOTH, side=tk.LEFT, padx=5, pady=5, expand=True)

satis_frame = tk.Frame(relief=tk.GROOVE, borderwidth=1)
label = tk.Label(master=satis_frame, text="Satışlar")
label.pack()
separator = ttk.Separator(master=satis_frame, orient='horizontal')
separator.pack(fill='x', padx=5)
satis_frame.pack(fill=tk.BOTH, side=tk.LEFT, padx=5, pady=5, expand=True)

destek_frame = tk.Frame(relief=tk.GROOVE, borderwidth=1)
label = tk.Label(master=destek_frame, text="Destek Talepleri")
label.pack()
separator = ttk.Separator(master=destek_frame, orient='horizontal')
separator.pack(fill='x', padx=5)
destek_frame.pack(fill=tk.BOTH, side=tk.LEFT, padx=5, pady=5, expand=True)

ust.pack(side=tk.TOP, padx=5, pady=5)

def musteri_frame_yenile():
    global musteri_labels
    
    for label in musteri_labels:
        label.pack_forget()

    for musteri in musteriler:
        label = tk.Label(musteri_frame, text=f"{musteri.ad}, {musteri.iletisim}")
        label.pack()
        musteri_labels.append(label)

def satis_frame_yenile():
    global satis_labels
    
    for label in satis_labels:
        label.pack_forget()

    for musteri in musteriler:
        for satis in musteri.satislar:
            label = tk.Label(satis_frame, text=f"Müşteri: {musteri.ad}, Sipariş Numarası: {satis.siparis_numarasi}, Ürünler: {satis.urunler}")
            label.pack()
            satis_labels.append(label)

def destek_frame_yenile():
    global destek_labels
    
    for label in destek_labels:
        label.pack_forget()

    for musteri in musteriler:
        for talep in musteri.destek_talepleri:
            label = tk.Label(destek_frame, text=f"Müşteri: {musteri.ad}, Talep Numarası: {talep.talep_numarasi}, Detaylar: {talep.detaylar}")
            label.pack()
            destek_labels.append(label)

def musteri_ekle_ekrani():
    def ekle():
        isim = ad.get()
        iletisim = iletisim_entry.get()
        musteri = Musteri(isim, iletisim)
        musteriler.append(musteri)
        musteri_frame_yenile()
        ekran.destroy()

    ekran = tk.Toplevel(window)
    ekran.title("Müşteri Ekle")

    label = ttk.Label(ekran, text="Ad:")
    label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    ad = ttk.Entry(ekran)
    ad.grid(row=0, column=1, padx=10, pady=5)

    label = ttk.Label(ekran, text="İletişim:")
    label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    iletisim_entry = ttk.Entry(ekran)
    iletisim_entry.grid(row=1, column=1, padx=10, pady=5)

    buton = ttk.Button(ekran, text="Ekle", command=ekle)
    buton.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

def satis_ekle_ekrani():
    def ekle():
        musteri_index = combobox.current()
        urunler = urunler_entry.get()
        musteri = musteriler[musteri_index]
        satis = Satis(len(musteri.satislar) + 1, urunler)
        musteri.satis_ekle(satis)
        satis_frame_yenile()
        ekran.destroy()

    ekran = tk.Toplevel(window)
    ekran.title("Satış Ekle")

    label = ttk.Label(ekran, text="Müşteri:")
    label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    musteri_isimler = []
    for musteri in musteriler:
        musteri_isimler.append(musteri.ad)
    combobox = ttk.Combobox(ekran, values=musteri_isimler)
    combobox.grid(row=0, column=1, padx=10, pady=5)

    label = ttk.Label(ekran, text="Ürünler:")
    label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    urunler_entry = ttk.Entry(ekran)
    urunler_entry.grid(row=1, column=1, padx=10, pady=5)

    buton = ttk.Button(ekran, text="Ekle", command=ekle)
    buton.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

def destek_ekle_ekrani():
    def ekle():
        musteri_index = combobox.current()
        detaylar = detaylar_entry.get()
        musteri = musteriler[musteri_index]
        talep = Destek(len(musteri.destek_talepleri) + 1, detaylar)
        musteri.destek_talebi_ekle(talep)
        destek_frame_yenile()
        ekran.destroy()

    ekran = tk.Toplevel(window)
    ekran.title("Destek Talebi Ekle")

    label = ttk.Label(ekran, text="Müşteri:")
    label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    musteri_isimler = []
    for musteri in musteriler:
        musteri_isimler.append(musteri.ad)
    combobox = ttk.Combobox(ekran, values=musteri_isimler)
    combobox.grid(row=0, column=1, padx=10, pady=5)

    label = ttk.Label(ekran, text="Detaylar:")
    label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    detaylar_entry = ttk.Entry(ekran)
    detaylar_entry.grid(row=1, column=1, padx=10, pady=5)

    buton = ttk.Button(ekran, text="Ekle", command=ekle)
    buton.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

alt = tk.Frame()

buton = ttk.Button(alt, text="Müşteri Ekle", command=musteri_ekle_ekrani)
buton.pack(fill=tk.BOTH, ipadx=2, ipady=2, padx=5, pady=5, expand=True)
buton= ttk.Button(alt, text="Satış Ekle", command=satis_ekle_ekrani)
buton.pack(fill=tk.BOTH, ipadx=2, ipady=2, padx=5, pady=5, expand=True)
buton= ttk.Button(alt, text="Destek Talebi Ekle", command=destek_ekle_ekrani)
buton.pack(fill=tk.BOTH, ipadx=2, ipady=2, padx=5, pady=5, expand=True)

alt.pack(fill=tk.X, padx=5, pady=5)

window.mainloop()
