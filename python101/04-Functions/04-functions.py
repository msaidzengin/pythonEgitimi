sozluk = {"elma": "Apple", "armut": 4, "muz": 7}

sozluk["elma"]

print(sozluk)

sozluk[0]
sozluk.values()
sozluk.keys()
sozluk.items()

for anahtar, deger in sozluk.items():
    print("key", anahtar)
    print("val", deger)


def selamla():
    print("merhaba")


selamla()


def topla(a=1, b=1, c=7):
    return a + b + c


print(topla(c=3))


print("brk", "emre", sep="\n")

bool(0)


def f(x, y):
    return x**2 + 2*y + 9


print(5 + f(4, 3))

# faktoriyel
sayı = int(input('Sayı değerini giriniz:'))


def faktoriyel(x):
    çarp = 1
    for oku in range(x):
        çarp = çarp*(oku+1)
    return çarp


print('Faktöriyel : ', faktoriyel(sayı))

say = int("asd")


try:
    say1 = int(input("say 1 "))
    say2 = int(input("say 2: "))
    say = say1/say2
except ZeroDivisionError:
    print("Sıfıra bölemezsin")
except ValueError:
    print("Lütfen düzgün bir sayı giriniz")
