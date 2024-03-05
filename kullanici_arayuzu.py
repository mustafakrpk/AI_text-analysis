# MUSTAFA KIRPIK    25.02.2024  - 01.03.2024

import tkinter as tk
from metin_analizi import metni_analiz_et_ve_ara, bul_sohtet_genel_konusu
from veritabani_islemleri import VeritabaniIslemleri


# Veritabanı bağlantısı
host = "localhost"
user = "root"
password = "Uxxxxxxxxxxxxxxxxxxxxx"
database = "yapayzeka"


# Veritabanı işlemleri nesnesi oluşturuldu
veritabani_islemleri = VeritabaniIslemleri(host, user, password, database)


def metin_gonder():
    global tum_metinler
    metin = metin_giris.get("1.0", "end-1c")  # Metin kutusundan metni al
    genel_konu, alt_konular, arama_sonuclari = metni_analiz_et_ve_ara(
        metin
    )  # Metni analiz et ve arama yap
    print("Genel konu:", genel_konu)
    print("Alt konular:", alt_konular)
    print("Arama sonuçları:", arama_sonuclari)
    tum_metinler.append((metin, genel_konu))  # Metni ve genel konuyu sakla
    genel_konusu = bul_sohtet_genel_konusu(tum_metinler)  # sohbet genel konusu
    print("Sohbetin genel konusu:", genel_konusu)

    # Metni veritabanına ekleme işlemi
    veritabani_islemleri.metni_veritabanina_ekle(
        metin, genel_konu, alt_konular, arama_sonuclari
    )


# Tkinter penceresi oluşturma
root = tk.Tk()
root.title("Metin Girişi")

# Metin girişi kutusu
metin_giris = tk.Text(root, height=20, width=50)
metin_giris.pack()

#
gonder_dugmesi = tk.Button(root, text="Gönder", command=metin_gonder)
gonder_dugmesi.pack()

# Tüm metinleri saklamak için boş bir liste oluştur
tum_metinler = []

# Ana döngüyü başlatma
root.mainloop()
