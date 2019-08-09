import random

isim = ""
while isim != "quit":
    isim = input("isminiz nedir: ")
    parola = ""
    for i in range(6):
        a = random.choice(isim)
        b = random.randint(0,1)
        if b == 0:
            parola += a.lower()
        else:
            parola += a.upper()
        

    for i in range(4):
        parola += str(random.randint(0,9))
    print(parola)

print("a".upper())
print("b".lower())
