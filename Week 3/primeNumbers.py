
# is Prime metodu parametre olarak bir integer alır.
# Eger asal sayı ise true, değilse false return eder.
def isPrime(n):
    for i in range (2,n):
        if n % i == 0:
            return False
    return True



#prime Numbers dizisinin içinde 0,100 arasındaki asal sayılar bulunuyor.
primeNumbers = []
for i in range (100):
    if isPrime(i):
        primeNumbers.append(i)
    

print(primeNumbers)



# Fonksiyona parametre olarak 2 adet sayı verilir.
# Bu iki sayı arasındaki tüm asal sayılar ekrana basılır.
def ikiSayiArasindakiAsalSayilar(a,b):
    for i in range(a,b):
        if isPrime(i):
            print(i, end=", ")


print(ikiSayiArasindakiAsalSayilar (100,200)  )

