import random

randomSayi = random.randint(0,1000)
cevap = -1

tahminSayisi = 0
while cevap != randomSayi:
    tahminSayisi += 1
    cevap = int(input("tahmininin nedir: "))
    if cevap < randomSayi:
        print("cok kucuk soyledin")
    elif cevap > randomSayi:
        print("cok buyuk")
    
print("Bildin! Random sayi =", randomSayi)
print("Tahmin sayisi:", tahminSayisi)
