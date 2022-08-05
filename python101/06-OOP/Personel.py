convertWeekDays = {
    1: "Pazartesi",
    2: "Salı",
    3: "Çarşamba",
    4: "Perşembe",
    5: "Cuma",
    6: "Cumartesi",
    7: "Pazar"
}


class Personel():
    def __init__(self, isim, soyisim, yas, cinsiyet, maas, kimlik, calisma_gunleri):
        self.isim = isim
        self.soyisim = soyisim
        self.yas = yas
        self.cinsiyet = cinsiyet
        self.maas = maas
        self.kimlik = kimlik
        self.calisma_gunleri = calisma_gunleri

    def printInfo(self):
        print("---------------------")
        print(self.isim, self.soyisim, self.yas, "yaşındadır.")
        print(self.cinsiyet, "cinsiyetindedir.")
        print("Maaşı", self.maas, "TL'dir.")
        print("Kimlik numarası:", self.kimlik)
        gunler = [convertWeekDays[i] for i in self.calisma_gunleri]
        print("Çalışma günleri:", ' / '.join(gunler))

    def maas_guncelle(self, yeni_maas):
        self.maas = yeni_maas

    def calisma_gunu_ekle(self, gun):
        self.calisma_gunleri.append(gun)


per1 = Personel("Ahmet", "Yıldız", 32, "M", 2000, "12345678901", [1, 3, 5])
per2 = Personel("Ayşe", "Yılmaz", 25, "F", 3000, "18956278950", [2, 3, 4, 5])
per3 = Personel("Mehmet", "Yılmaz", 28, "M", 2500, "11122255570", [1, 2, 3, 4])

per1.printInfo()
per1.maas_guncelle(50000)
per1.printInfo()
