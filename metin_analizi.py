# MUSTAFA KIRPIK  25.02.2024  - 01.03.2024
import spacy_stanza
from googlesearch import search


# spaCy'nin Türkçe dil modelini yükleyelim
nlp = spacy_stanza.load_pipeline("tr")


def metni_analiz_et_ve_ara(metin):
    # Metni analiz et
    genel_konu, alt_konular = metin_analizi(metin)

    # İnternette arama yap
    arama_sonuclari = internet_aramasi_yap(genel_konu)

    return genel_konu, alt_konular, arama_sonuclari


def internet_aramasi_yap(konu):
    # Google'da arama yap
    arama_sorgusu = konu
    arama_sonuclari = list(search(arama_sorgusu, sleep_interval=5, num_results=10))

    return arama_sonuclari


def metin_analizi(metin):
    #  Metni Tokenize Etme
    kelimeler = metin.split()

    #  Anahtar Kelimeler
    anahtar_kelimeler = {
        "Edebiyat": ["kitap", "yazar", "şiir", "roman", "edebi eser"],
        "Bilim ve Teknoloji": [
            "bilim",
            "teknoloji",
            "fizik",
            "kimya",
            "kuantum",
            "matematik",
        ],
        "Spor": ["spor", "futbol", "basketbol", "voleybol", "tenis"],
        "Sağlık ve Tıp": ["sağlık", "tıp", "hastalık", "tedavi", "doktor"],
        "Sanat ve Kültür": ["sanat", "müzik", "resim", "tiyatro", "sinema"],
        "Tarih ve Politika": ["tarih", "politika", "savaş", "lider", "devlet"],
        "Doğa ve Çevre": ["doğa", "çevre", "hayvan", "bitki", "ekoloji"],
        "Eğitim": ["eğitim", "okul", "öğrenci", "öğretmen", "ders"],
    }
    genel_konu_ağırlıkları = {konu: 0 for konu in anahtar_kelimeler}

    for kelime in kelimeler:
        for konu, anahtar_kelime_listesi in anahtar_kelimeler.items():
            if kelime.lower() in anahtar_kelime_listesi:
                genel_konu_ağırlıkları[konu] += 1
        genel_konu = "Diğer"

    # En yüksek ağırlığa sahip genel konuyu seçme
    genel_konu = max(genel_konu_ağırlıkları, key=genel_konu_ağırlıkları.get)

    #  Alt Konular
    alt_konular = []
    if genel_konu == "Bilim ve Teknoloji":
        alt_konular = [
            "Fizik",
            "Kimya",
            "Matematik",
            "bilim",
            "teknoloji",
            "fizik",
            "kimya",
        ]
    elif genel_konu == "Spor":
        alt_konular = [
            "Futbol",
            "Basketbol",
            "Voleybol",
            "Tenis",
            "Teknik Direktör",
            "Kulüp Başkanı",
        ]
    elif genel_konu == "Tarih ve Politika":
        alt_konular = [
            "Tarih",
            "Politika",
            "Savaş",
            "tarih",
            "politika",
            "savaş",
            "lider",
            "devlet",
        ]
    elif genel_konu == "Edebiyat":
        alt_konular = ["kitap", "yazar", "şiir", "roman", "edebi eser"]
    elif genel_konu == "Sanat ve Kültür":
        alt_konular = ["sanat", "müzik", "resim", "tiyatro", "sinema"]
    elif genel_konu == "Sağlık ve Tıp":
        alt_konular = ["sağlık", "tıp", "hastalık", "tedavi", "doktor"]
    elif genel_konu == "Doğa ve Çevre":
        alt_konular = ["doğa", "çevre", "hayvan", "bitki", "ekoloji"]
    elif genel_konu == "Eğitim":
        alt_konular = ["eğitim", "okul", "öğrenci", "öğretmen", "ders"]

    return genel_konu, alt_konular


def bul_sohtet_genel_konusu(metinler):
    genel_konu_sayaci = {}

    # Metinlerin genel konularını belirle ve say
    for metin, genel_konu in metinler:
        if genel_konu in genel_konu_sayaci:
            genel_konu_sayaci[genel_konu] += 1
        else:
            genel_konu_sayaci[genel_konu] = 1

    # En çok tekrar eden genel konuyu bul
    en_cok_tekrar = 0
    en_cok_tekrarlanan_konu = None
    for konu, tekrar_sayisi in genel_konu_sayaci.items():
        if tekrar_sayisi > en_cok_tekrar:
            en_cok_tekrar = tekrar_sayisi
            en_cok_tekrarlanan_konu = konu
    return en_cok_tekrarlanan_konu
