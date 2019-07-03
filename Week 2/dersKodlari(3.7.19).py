
cumle = input("Lutfen cumle giriniz: ")
toplam = 0
karakter = 'a'
for c in cumle:
    if c == karakter:
        toplam += 1
print(toplam)



sayi1 = input("ilk sayiyi giriniz: ")
sayi2 = input("ikinci sayiyi giriniz: ")
if sayi1.isdigit() and sayi2.isdigit():
    sayi1 = int(sayi1)
    sayi2 = int(sayi2)
    if sayi1 > sayi2:
        print("Büyük sayý = " + str(sayi1))
    elif sayi1 == sayi2:
        print("Bu sayýlar eþit")
    else:
        print("Büyük sayý = " + str(sayi2))
else:
    print("hatalý input")


dizi = [[1,2,3],[4,5,6,6,2],[7,8,9]]

for i in range(len(dizi)):
    for j in range(len(dizi[i])):
        dizi[i][j] = dizi[i][j] + 2
        print(dizi[i][j], end=" ")
    print()

for i in range(5):
    for j in range(5-i):
        print("*", end=" ")
    print()

for i in range(5):
    print("* " * (5-i))
    



sozluk = {"hello":"merhaba","phone":"telefon"}
print(sozluk["hello"])
print(sozluk.values())
print(sozluk.keys())
print()



def isPrime(x):
    if x < 2:
        return False
    for i in range(2,x-1):
        if x % i == 0:
            return False
    return True
    
def asalSayilar(x,y):
    dizi = []
    for i in range(x,y):
        if isPrime(i):
            dizi.append(i)
    return dizi


dizi = asalSayilar(800,900)
print(dizi)
    



def karakterSayisi(cumle,harf):
    toplam = 0
    for c in cumle:
        if c == harf:
            toplam += 1
    return toplam

cumle = "Burasý BTK Akademi."
harf = 'a'
print(karakterSayisi(cumle,harf))


def values(sozluk):
    dizi = []
    for i in sozluk:
        dizi.append(sozluk[i])
    return dizi

sozluk = {"hello":"merhaba","phone":"telefon"}
print(sozluk.values())
print(values(sozluk))



def minimum(dizi):
    min = 99999
    for i in dizi:
        if i < min:
            min = i
    return min
def maximum(dizi):
    max = -99999
    for i in dizi:
        if i > max:
            max = i
    return max     

dizi = [4,3,2,6,7,0,6,3,5,7,45,-3,7,2467,3]
print(min(dizi))
print(max(dizi))
print(minimum(dizi))
print(maximum(dizi))



i = 1
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)


numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
print(sum(numbers))



# 10 is the total number to print
for num in range(10):
    for i in range(num):
        print (i, end=" ") #print number
    # new line after each row to display pattern correctly
    print("\n")
    


def factoriel(x):
    if x < 1:
        return 1
    else:
        return x * factoriel(x-1)


print(factoriel(5))



cumle = "burasý btk akademi."
kelimeler = cumle.split(" ")
for kelime in kelimeler:
    print(kelime[0].upper() + kelime[1:len(kelime)].lower())



def bol(cumle):
    kelime = ""
    dizi = []
    for c in cumle:
        if c == ' ':
            dizi.append(kelime)
            kelime = ""
        else:
            kelime += c
    if kelime != "":
        dizi.append(kelime)
    return dizi
cumle = "burasý btk akademi."
print(cumle)
dizi = bol(cumle)
print(dizi)


    
   