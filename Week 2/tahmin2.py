import random

counter = 0
tahmin = 0
x = -1
y = 1001
cevap = ""

while cevap != "doğru":
    counter += 1
    tahmin = random.randint(x+1,y-1)
    print(tahmin)
    cevap = input("[küçük - büyük - doğru]: ")
    if cevap == "küçük":
        x = tahmin
    elif cevap == "büyük":
        y = tahmin
        
print("Buldum! Tahmin ettiğin sayı:", tahmin)
print("Tahmin sayısı", counter)
