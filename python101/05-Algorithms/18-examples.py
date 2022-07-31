import random

tutulanSayi = int(input("bir sayı tut: "))
denemeSayisi = []
for i in range(10000):
    x = 0
    y = 1000
    sayac = 0
    tahmin = -1
    while tahmin != tutulanSayi:
        sayac += 1
        tahmin = random.randint(x,y)
        if tahmin < tutulanSayi:
            x = tahmin + 1
        elif tahmin > tutulanSayi:
            y = tahmin - 1
    
    denemeSayisi.append(sayac)
    
print(sum(denemeSayisi) / len(denemeSayisi))
