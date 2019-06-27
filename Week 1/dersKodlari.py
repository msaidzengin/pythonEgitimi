for i in range(1,11):
    print(i)
    
for i in range(1,11):
    print("Rakam = " + str(i))

for i in range(11):
    if (i % 2) == 0:
        print(i)
        
for i in range(0,11,2):
    print(i)

fac = 1
for i in range(1,11):
    fac = fac * i
    print(str(i) + "!=" + str(fac))


for i in range(5):
    for j in range(10):
        print("*",end=" ")
    print()
    
print("---------\n")

for i in range(5):
    for j in range(i+1):
        print(j+1,end=" ")
    print()

print("---------\n")


for i in range(1,100000):
    if(i == 5):
        break
    print(i)
    

for i in range(2,101):
    for j in range(2,i-1):
        if i % j == 0:
            break
    else:
        print(i)            



tamBolenSayisi = 0
for i in range(1,101):
    tamBolenSayisi = 0
    for j in range(1,i+1):
        if i % j == 0:
            tamBolenSayisi += 1
    print(str(i) + "'nin tam bölen sayısı " + str(tamBolenSayisi))
        
    


dizi = [1,2,54,4567,563,2,54,7,4,-5,500]
toplam = sum(dizi)
print(toplam)


toplam = 0
for i in range (len(dizi)):
    toplam += dizi[i]
print(toplam)

print("Dizinin ortalaması: " + str(toplam/len(dizi)))

dizi.sort()
print(dizi)
medyan = dizi[len(dizi) // 2]
print("Dizinin medyanı: " + str(medyan))



i = 0
while (i < 100):
    print(i)
    i += 1
    




cumle = "Burası BTK Akademi."
for i in range(len(cumle)):
    if( cumle[i]  == 'a'):
        print("a varmış. index: " + str(i+1))


"""

Ödev: 

soru1: Bir cümlede kaç tane 
'a' harfi geçtiğini bulun.
Ve ekrana bastırın.

soru2: tersten üçgen piramit
ekrana yazın
*****
****
***
**
*



"""



