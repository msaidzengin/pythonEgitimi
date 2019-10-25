import random
cvp = ""
x = 0
y = 1000
sayac = 0
while cvp != "doğru":
    sayac += 1
    tahmin = random.randint(x,y)
    print("tahminim:", tahmin)
    cvp = input("(küçük-büyük-doğru)?: ")
    if cvp == "küçük":
        x = tahmin + 1
    elif cvp == "büyük":
        y = tahmin - 1

print("buldum! teşekkürler")
print("deneme sayısı", sayac)
