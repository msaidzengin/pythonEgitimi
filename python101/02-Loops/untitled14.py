import random


sayi = random.randint(0,1000)
cvp = -1
denemeSayisi = 0
while sayi != cvp:
    denemeSayisi += 1
    cvp = int(input("tahmin et: "))
    if cvp < sayi:
        print("çok küçük")
    elif cvp > sayi:
        print("çok dedin")
    
print("bildin!")
print("deneme sayısı:", denemeSayisi)
