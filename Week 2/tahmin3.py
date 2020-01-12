import random

counter = 0
tahmin = 0
x = -1
y = 200
cevap = ""
tutulanSayi = int(input("bir sayi tut: "))

while tahmin != tutulanSayi:
    counter += 1
    tahmin = random.randint(x+1,y-1)
    print(tahmin)
    if tahmin < tutulanSayi:
        x = tahmin
    elif tahmin > tutulanSayi:
        y = tahmin

        
print("Buldum! Tahmin ettigin sayi:", tahmin)
print("Tahmin sayisi", counter)
