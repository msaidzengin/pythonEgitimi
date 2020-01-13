import random

metin = "merhaba dünya"
liste = [1,2,3,4,5]

print(random.choice(metin))
print(random.choice(liste))
print(random.randrange(5)) #0,1,2,3,4
print(random.randint(3,5)) #3,4,5

# hileli zar atımı
ihtimaller = [1,2,3,4,5,6,6,6,6,6]
print(random.choice(ihtimaller))

a = random.randrange(2)
if a == 0:
    print(random.randint(1,5))
else:
    print(6)
