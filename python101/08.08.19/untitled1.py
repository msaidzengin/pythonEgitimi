
metin = input("metin giriniz: ")

rakamlar = ['0','1','2','3','4','5','6','7','8','9']

count = 0
for i in metin:
    if i in rakamlar:
        count += 1
        

if count == len(metin):
    print("digit")
else:
    print("not digit")
    
