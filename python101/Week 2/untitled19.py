import random

sonuclar = [0] * 11
for i in range(500000):
    sonuc = random.randint(1,6) + random.randint(1,6)
    sonuclar[sonuc - 2] += 1
    
for i in range(len(sonuclar)):
    print(str(i+2) + " gelme olasılığı = " + str(sonuclar[i] / 5000))
