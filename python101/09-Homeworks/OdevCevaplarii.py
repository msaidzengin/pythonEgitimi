""""
Soru 1: Parametre olarak 2 sayı alan ve ortalamasını return eden bir fonksiyon yazınız.
Fonksiyonu test etmek için 3 defa çağırıp doğruluğunu deneyiniz.
"""

def ortalama(a,b):
    return (a+b) / 2

print( ortalama(2,3) )
print( ortalama(10,30) ) 
print( ortalama(3,14) )


"""
Soru 2: Parametre olarak bir sayı listesi alan ve listenin ortalamasını return eden bir fonksiyon yazınız.
Fonksiyonu test etmek için 3 farklı liste ile deneyiniz.
"""

def listeOrtalamasi(liste):
    return sum(liste) / len(liste)

liste1 = [1,2,3,4]
liste2 = [10,20,30]
liste3 = [2,3]

print(listeOrtalamasi(liste1))
print(listeOrtalamasi(liste2))
cevap = listeOrtalamasi(liste3)
print(cevap)

# ortalama metodunu sum kullanmadan şu şekilde yazabiliriz:
def ort(liste):
    toplam = 0
    for i in liste:
        toplam += i
    return toplam / len(liste)


"""
Soru 3: İkinci soruda yazdığınız metodu kullanarak 1 ile 100 arasındaki aralıkların ortalamasını ekrana basın.
Örnek olarak, 
1-2 aralığının ortalaması
1-3 aralığının ortalaması
1-4 aralığının ortalaması
1-5 aralığının ortalaması
...
...
1-100 aralığının ortalaması
"""

for i in range(2,100):
    liste = range(1,i)
    print ( ort(liste) )
    #print(listeOrtalamasi(liste))


"""
Soru 4: Parametre olarak bir sayı alan ve faktöriyelini print eden bir fonksiyon yazınız.
Daha sonra metodu 5 sayısı ile çağırınız.
"""

def factorial(num):
    fac = 1
    for i in range(1,num):
        fac *= i
    return fac
print( factorial(5) )


"""
Soru 5: Dördüncü soruda yazdığınız fonksiyonu kullanarak 1-20 arasındaki tüm sayıların faktöriyelini ekrana basın.
"""

for i in range(1,20):
    print(factorial(i))


"""
Soru 6: Parametre olarak bir dizi alan fonksiyon yazın ve maximum sayıyı return ediniz.
"""
#normalde pythonda max metodu var onu kullanarak şöyle yapılır.
def maxBul(liste):
    return max(liste)

#fakat max sayıyı kendimiz şu algoritma ile bulabiliriz

def maxx(liste):
    buyukSayi = 0     #burada listede negatif sayı olmadığını varsayalım
    for i in liste:
        if buyukSayi > i:
            buyukSayi = i
    return buyukSayi

# eger negatif sayılar olan bi listede max value bulacaksak
# buyukSayi = MIN VALUE yapmamız gerekiyor. yani en küçük sayıdan başlarsak sorun kalmaz
# sys kütüphanesi kullanarak yapabiliriz.

"""
Soru 7: Parametre olarak bir dizi alan fonksiyon yazın ve minimum sayıyı return ediniz.
"""
def minBul(dizi):
    return min(dizi)

def minn(dizi):
    kucukSayi = sys.maxsize
    for i in dizi:
        if kucukSayi < i:
            kucukSayi = i
    return kucukSayi



"""
Soru 8: 
Derste preudo code(sudo kod)'unu yazdığımız metodu python dili ile yazınız.
Soru şöyleydi: İnput olarak bir paragraf alın. 
Paragraftaki tüm kelimeleri baş harfi büyük olacak şekilde ekrana yazın.
Sudo kod: 
paragraf = input al.
dizi = paragraf.split(" ")
for kelime in dizi
    kelime[0].upper
    print kelime
"""

paragraf = input("Lütfen paragraf giriniz: ")
kelimeler = paragraf.split(" ")
for kelime in kelimeler:
    print(kelime[0].upper() + kelime[1:len(kelime)])



"""
Soru 9:
Buradaki split metodu pythonda var. Fakat isteyenler split metodunu da kendi yazabilir.
Split metodu için sudokod:
def split(paragraf, karakter)
    dizi = []
    kelime = ""
    for c in paragraf:
        if c != karakter:
            kelime += c
        else:
            dizi.add (kelime)
            kelime = ""
Bu sudokodunu yazdığımız split metodunu split(paragraf, ' ') şeklinde çağırabilirsiniz.
"""

#split metodunun yeni ismi ayir olsun
#paragrafı her zaman boşluklardan ayıralım.
def ayir(paragraf):
    kelimeler = []
    kelime = ""
    for harf in paragraf:
        if harf != " ":
            kelime += harf
        else:
            kelimeler.append(kelime)
            kelime = ""
    kelimeler.append(kelime) # bu satırı paragraf sonunda boşluk olmadığı için yazdık
    return kelimeler

# ayirma metodunu split'teki gibi istediğimiz bir karakterden ayırmak istersek;
# parametre olarak x alıp, if'in içinde x ile karşılaştırma yapıyoruz
def ayir2(paragraf, x):
    kelimeler = []
    kelime = ""
    for harf in paragraf:
        if harf != x:
            kelime += harf
        else:
            kelimeler.append(kelime)
            kelime = ""
    kelimeler.append(kelime) # bu satırı paragraf sonunda boşluk olmadığı için yazdık
    return kelimeler

"""
soru 10:  (ekstra)
8. soruda kelimeleri split ile ayırıp ekrana basarken,
nokta virgül gibi karakterleri kelimelerden silebiliriz.
"""

paragraf = input("Lütfen paragraf giriniz: ")
kelimeler = paragraf.split(" ")
for kelime in kelimeler:
    kelime.replace(",","")
    kelime.replace(".","")
    print(kelime[0].upper() + kelime[1:len(kelime)])

#burada nokta ve virgül olan yerleri boş string ile değiştirdik.
#split ederken bu karakterleri hiç görmeyerek de yapabilirdik.
#birsürü farklı yöntemle yapabiliriz.