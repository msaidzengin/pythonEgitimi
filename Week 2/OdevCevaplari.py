#Soru 1:

a = int(input("Lütfen ilk sayıyı giriniz: "))
b = int(input("Lütfen ikinci sayıyı giriniz: "))

if a > b:
    print("Büyük sayı = " + str(a) + " ve küçük sayı = " + str(b))
elif a < b:
    print("Büyük sayı = " + str(b) + " ve küçük sayı = " + str(a))
else:
    print("İki sayı eşit ve değerleri = " + str(a))



#Soru 2: 
cumle = input("Lütfen cümle giriniz")

#(Yöntem 1)
counter = 0
for c in cumle:
    if c == 'a':
        counter += 1
print(counter)

#(Yöntem 2)
toplam = 0
for i in range(len(cumle)):
    if cumle[i] == 'a':
        toplam += 1
print(toplam)