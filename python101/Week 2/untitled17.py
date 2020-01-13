import random
x = 0
y = 1000
sayac = 0
tahmin = -1
tutulanSayi = int(input("bir sayı tut: "))
while tahmin != tutulanSayi:
    sayac += 1
    tahmin = random.randint(x,y)
    print("tahminim:", tahmin)
    if tahmin < tutulanSayi:
        x = tahmin + 1
    elif tahmin > tutulanSayi:
        y = tahmin - 1

print("buldum! teşekkürler")
print("deneme sayısı", sayac)
