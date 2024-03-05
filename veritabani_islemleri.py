# MUSTAFA KIRPIK  01.03.2024 - 02.03.2024

import mysql.connector
import json


class VeritabaniIslemleri:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.baglanti = None
        self.cursor = None

    def baglantiyi_ac(self):
        self.baglanti = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
        )
        self.cursor = self.baglanti.cursor()

    def baglantiyi_kapat(self):
        if self.cursor:
            self.cursor.close()
        if self.baglanti:
            self.baglanti.close()

    def tabloyu_olustur(self):
        self.baglantiyi_ac()
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS metinler
                              (id INT AUTO_INCREMENT PRIMARY KEY,
                               metin TEXT,
                               genel_konu TEXT
                               alt_konular TEXT
                               arama_sonuclari  TEXT)"""
        )
        self.baglantiyi_kapat()

    def metni_veritabanina_ekle(self, metin, genel_konu, alt_konular, arama_sonuclari):
        self.baglantiyi_ac()
        alt_konular_str = ", ".join(alt_konular)
        arama_sonuclari_json = json.dumps(
            arama_sonuclari
        )  # Arama sonuçlarını JSON formatına dönüştürür.
        sql = "INSERT INTO metinler (metin, genel_konu, alt_konular,arama_sonuclari) VALUES (%s, %s,%s,%s)"
        values = (metin, genel_konu, alt_konular_str, arama_sonuclari_json)
        self.cursor.execute(sql, values)
        self.baglanti.commit()
        self.baglantiyi_kapat()
