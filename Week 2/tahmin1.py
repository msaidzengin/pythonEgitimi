import random

randomSayi = random.randint(0,1000)
cevap = -1

tahminSayisi = 0
while cevap != randomSayi:
    tahminSayisi += 1
    cevap = int(input("tahmininin nedir: "))
    if cevap < randomSayi:
        print("çok küçük söyledin")
    elif cevap > randomSayi:
        print("çok büyük")
    
print("Bildin! Random sayı =", randomSayi)
print("Tahmin sayısı:", tahminSayisi)
