def yontem1():
    # kullanicidan input olarak liste alma, yontem 1:
    liste = []
    while True:
        sayi = input("Sayi giriniz: ")
        if sayi == "":
            break
        liste.append(int(sayi))

    print(liste)


def yontem2():
    # kullanicidan input olarak liste alma, yontem 2:
    liste = []
    uzunluk = int(input("Liste uzunlugu: "))
    for i in range(uzunluk):
        sayi = int(input("Sayi giriniz: "))
        liste.append(sayi)
    print(liste)


def yontem3():
    # kullanicidan input olarak liste alma, yontem 3:
    str_list = input("Liste giriniz: ")
    liste = str_list.split(" ")
    liste = [int(i) for i in liste]
    print(liste)


def listeOrtalama(liste):
    return sum(liste) / len(liste)


def question3():
    for i in range(2, 101):
        liste = list(range(1, i+1))
        print(listeOrtalama(liste))


def factorial(n):
    cevap = 1
    for i in range(1, n+1):
        cevap *= i
    print(cevap)


def maksimum1(liste):
    return max(liste)


def maksimum2(liste):
    enbuyuk = liste[0]
    for i in liste:
        if i > enbuyuk:
            enbuyuk = i
        # print(enbuyuk)

    return enbuyuk


def minimum(liste):
    enkucuk = liste[0]
    for i in liste:
        if i < enkucuk:
            enkucuk = i

    return enkucuk


def q8():
    paragraf = input("Metin giriniz:")
    print("---------------------------")
    kelimeler = paragraf.split()
    for kelime in kelimeler:
        yenikelime = kelime[0].upper() + kelime[1:].lower()
        print(yenikelime, end=" ")
    print()
    print("---------------------------")


def sezarSifrele(text, number):
    newText = ""
    for i in text:
        newText += (chr(ord(i) + number))
    return newText


# Parametre olarak, bir liste ve bir sayı alan bir fonksiyon yazınız.
# Bu fonksiyon, liste içerisinde sayıların kaç kere geçtiğini bulup return etsin.

def search(liste, sayi):
    counter = 0
    for i in liste:
        if i == sayi:
            counter += 1
    return counter

# Parametre olarak bir liste alan ve bu listeyi sıralayıp return eden bir fonksiyon yazınız.


def sort(liste):
    yeniliste = []
    while len(liste) > 0:
        enbuyuk = max(liste)
        yeniliste.append(enbuyuk)
        liste.remove(enbuyuk)
        print(yeniliste)
    return yeniliste


def exampleRecursion(n):
    if n == 0:
        return
    print(n)
    exampleRecursion(n-1)
    print(n)


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)


def joinExample():
    liste = ["a", "b", "c", "d", "e"]
    print(" / ".join(liste))
