import random
import math
import kutuphane as k
"""
cumle = "burası btk."
yeni = ""
for i in range(len(cumle)):
    a = random.randint(0,1)
    if a == 0:
        yeni += (cumle[i].lower())
    else:
        yeni += (cumle[i].upper())

print(yeni)

cumle = "burası btk."
for i in range(5):
    a = random.randrange(len(cumle))
    print(cumle[a])

for i in range(4):
    print(random.randint(0,9))

isim = input("İsminizi giriniz: ")
parola = ""
for i in range(random.randint(5,8)):
    b = random.randint(0,1)
    a = random.randrange(len(isim))
    if b == 0:
        parola += isim[a].lower()
    else:
        parola += isim[a].upper()


for i in range(10-len(parola)):
    a = random.randint(0,9)
    parola += str(a)


print(parola)

math.pow(4,1/2)


def isPolindrom(sayi):
    return str(sayi) == k.reverse(str(sayi))


print(isPolindrom(12343321))

#lambda function
#for loop


ciftmi = lambda say : (say % 2) == 0
topla = lambda a,b,c : a+b+c
ortalama = lambda a,b,c : (a+b+c) / 3

karesiniAl = lambda *sayilar : [i**2 for i in sayilar]

print(karesiniAl(1,2,3,4,5,6))


ciftlerinKaresiniAl = lambda *sayilar : [i**2 for i in sayilar if(i%2==0)]

print(ciftlerinKaresiniAl(1,2,3,4,5,6,7,8,9,10))






def minn(dizi):
    minimum = 99999999
    for i in dizi:
        if i < minimum:
            minimum = i
    return minimum


liste = [9,5,3,15,45,756,4,6]
sıralıListe = []
count = len(liste)
for i in range(count):
    minimum = minn(liste)
    sıralıListe.append(minimum)
    liste.remove(minimum)

print(sıralıListe)

"""



















