import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

musteriler = []
siparisler = []
enstrumanlar = []
destek_talepleri = []

enstruman_labels = []
siparis_labels = []
destek_labels = []
secilen_enstruman = -1

class Enstruman:
    def __init__(self, ad, stok_miktari):
        self.ad = ad
        self.stok_miktari = stok_miktari
        
    def satis_yap(self, musteri, adet):
        if self.stok_miktari - adet < 0:
            messagebox.showerror("Hata", "Yeterli stok bulunamadı.")
            return
            
        self.stok_miktari = self.stok_miktari - adet
        musteri.siparisler.append(f"{self.ad} ({adet})")
        return Satis(len(siparisler), musteri.tam_isim, f"{self.ad} ({adet})")

class Musteri:
    def __init__(self, tam_isim, adres):
        self.tam_isim = tam_isim
        self.adres = adres
        self.siparisler = []

class Satis:
    def __init__(self, siparis_numarasi, isim, satilan_enstrumanlar):
        self.siparis_numarasi = siparis_numarasi
        self.isim = isim
        self.satilan_enstrumanlar = satilan_enstrumanlar

class Destek:
    def __init__(self, talep_numarasi, enstruman_adi, talep_detaylari):
        self.talep_numarasi = talep_numarasi
        self.enstruman_adi = enstruman_adi
        self.talep_detaylari = talep_detaylari

window = tk.Tk()
window.title("Dükkan")

ust = tk.Frame()

stok_frame = tk.Frame(relief=tk.GROOVE, borderwidth=1)
label = tk.Label(master=stok_frame, text="Stok")
label.pack()
separator = ttk.Separator(master=stok_frame, orient='horizontal')
separator.pack(fill='x', padx=5)
stok_frame.pack(fill=tk.BOTH, side=tk.LEFT, padx=5, pady=5, expand=True)

siparisler_frame = tk.Frame(relief=tk.GROOVE, borderwidth=1)
label = tk.Label(master=siparisler_frame, text="Siparişler")
label.pack()
separator = ttk.Separator(master=siparisler_frame, orient='horizontal')
separator.pack(fill='x', padx=5)
siparisler_frame.pack(fill=tk.BOTH, side=tk.LEFT, padx=5, pady=5, expand=True)

destek_frame = tk.Frame(relief=tk.GROOVE, borderwidth=1)
label = tk.Label(master=destek_frame, text="Destek Talepleri")
label.pack()
separator = ttk.Separator(master=destek_frame, orient='horizontal')
separator.pack(fill='x', padx=5)
destek_frame.pack(fill=tk.BOTH, side=tk.LEFT, padx=5, pady=5, expand=True)

ust.pack(side=tk.TOP, padx=5, pady=5)

def stok_frame_yenile():
    global enstruman_labels
    
    for label in enstruman_labels:
        label.pack_forget()
            
    enstruman_labels = []
    for enstruman in enstrumanlar:
        label = tk.Label(stok_frame, text=f"{enstruman.ad} ({enstruman.stok_miktari})")
        label.pack()
        enstruman_labels.append(label)

def siparisler_frame_yenile():
    global siparis_labels
    
    for label in siparis_labels:
        label.pack_forget()
            
    siparis_labels = []
    for siparis in siparisler:
        label = tk.Label(siparisler_frame, text=f"{siparis.siparis_numarasi}-{siparis.isim}: ({siparis.satilan_enstrumanlar})")
        label.pack()
        siparis_labels.append(label)

def enstruman_ekle_ekrani():
    def ekle():
        enstrumanlar.append(Enstruman(ad.get(), int(stok.get())))
        
        ekran.destroy()
        stok_frame_yenile()
    
    ekran = tk.Toplevel(window)
    ekran.title("Enstrüman Ekle")
    
    label = ttk.Label(ekran, text="Enstrüman adı:")
    label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    ad = ttk.Entry(ekran)
    ad.grid(row=0, column=1, padx=10, pady=5)

    label = ttk.Label(ekran, text="Stok miktarı:")
    label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    stok = ttk.Entry(ekran)
    stok.grid(row=1, column=1, padx=10, pady=5)
    
    buton = ttk.Button(ekran, text="Ekle", command=ekle)
    buton.grid(row=2, columnspan=2, padx=10, pady=10)

def destek_frame_yenile():
    global destek_labels
    
    for label in destek_labels:
        label.pack_forget()
            
    destek_labels = []
    for destek in destek_talepleri:
        label = tk.Label(destek_frame, text=f"{destek.talep_numarasi} - {destek.enstruman_adi}, {destek.talep_detaylari}")
        label.pack()
        destek_labels.append(label)


def destek_ekle_ekrani():
    def ekle():
        destek_talepleri.append(Destek(len(destek_talepleri), enstruman_ad.get(), mesaj.get()))
        
        ekran.destroy()
        destek_frame_yenile()
    
    ekran = tk.Toplevel(window)
    ekran.title("Destek Talepi Oluştur")
    
    label = ttk.Label(ekran, text="Enstrüman adı:")
    label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    enstruman_ad = ttk.Entry(ekran)
    enstruman_ad.grid(row=0, column=1, padx=10, pady=5)

    label = ttk.Label(ekran, text="Mesaj:")
    label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    mesaj = ttk.Entry(ekran)
    mesaj.grid(row=1, column=1, padx=10, pady=5)
    
    buton = ttk.Button(ekran, text="Oluştur", command=ekle)
    buton.grid(row=2, columnspan=2, padx=10, pady=10)
    
def satis_yap_ekrani():
    def sat_buton():
        if secilen_enstruman == -1 or stok.get() == "":
            messagebox.showerror("Hata", "İlk başta enstrüman seçin.")
            return
            
        enstruman = enstrumanlar[secilen_enstruman]
        
        if enstruman == None:
            messagebox.showerror("Hata", "Enstrüman bulunamadı.")
            return
        
        musteri = None
        for mus in musteriler:
            if mus.tam_isim.find(musteri_ad.get()) != -1:
                musteri = mus
                break
        
        if musteri == None:
            musteri = Musteri(musteri_ad.get(), musteri_adres.get())
            musteriler.append(musteri)
        
        satis = enstruman.satis_yap(musteri, int(stok.get()))
        if not satis:
            messagebox.showerror("Hata", "Yeterli stok bulunmuyor.")
            return
        
        siparisler.append(satis)
        ekran.destroy()
        stok_frame_yenile()
        siparisler_frame_yenile()

    ekran = tk.Toplevel(window)
    ekran.title("Satış Yap")
    
    index = 0
    for enstruman in enstrumanlar:
        def satis_enstruman_buton(index):
            def callback():
                global secilen_enstruman
                secilen_enstruman = index
            return callback
        class_name = enstruman.ad
        buton = ttk.Button(ekran, text=f"{enstruman.ad} ({enstruman.stok_miktari})", command=satis_enstruman_buton(index))
        buton.grid(row=index, column=0, columnspan=1, padx=5, pady=5)
        index = index + 1
    
    label = ttk.Label(ekran, text="Stok miktarı:")
    label.grid(row=0, column=1, padx=10, pady=5, sticky="w")
    stok = ttk.Entry(ekran)
    stok.grid(row=0, column=2, padx=10, pady=5)
    
    label = ttk.Label(ekran, text="Müşteri adı:")
    label.grid(row=1, column=1, padx=10, pady=5, sticky="w")
    musteri_ad = ttk.Entry(ekran)
    musteri_ad.grid(row=1, column=2, padx=10, pady=5)
    
    label = ttk.Label(ekran, text="Müşteri adresi:")
    label.grid(row=2, column=1, padx=10, pady=5, sticky="w")
    musteri_adres = ttk.Entry(ekran)
    musteri_adres.grid(row=2, column=2, padx=10, pady=5)
    
    sat = ttk.Button(ekran, text="Sat", command=sat_buton)
    sat.grid(row=0, column=3, padx=10, pady=10)
    
alt = tk.Frame()

enstruman_buton = ttk.Button(alt, text="Enstrüman Ekle", command=enstruman_ekle_ekrani)
enstruman_buton.pack(fill=tk.BOTH, ipadx=2, ipady=2, padx=5, pady=5, expand=True)
satis_buton= ttk.Button(alt, text="Satış Yap", command=satis_yap_ekrani)
satis_buton.pack(fill=tk.BOTH, ipadx=2, ipady=2, padx=5, pady=5, expand=True)
destek_buton = ttk.Button(alt, text="Destek Oluştur", command=destek_ekle_ekrani)
destek_buton.pack(fill=tk.BOTH, ipadx=2, ipady=2, padx=5, pady=5, expand=True)

alt.pack(fill=tk.X, padx=5, pady=5)

window.mainloop()
