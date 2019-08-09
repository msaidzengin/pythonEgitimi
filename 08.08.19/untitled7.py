

dizi = [5,6,1,7,10,3,14]
print(dizi)
dizi.append(10)
print(dizi)
dizi.append(5)
print(dizi)
dizi.insert(3,5)
print(dizi)
dizi.insert(len(dizi), 16)
print(dizi)
print(dizi.index(3))

index = 10
count = 0
for i in range(len(dizi)):
    if dizi[i] == index:
        count += 1
        break
if count == 0:
    print("eleman yok")
else:
    print("10un indexi = " + str(i))

dizi.insert(90, 100)
print(dizi)
print(dizi.index(100))
dizi.remove(100)
print(dizi)
print(dizi.pop())
print(dizi)
print(dizi.pop(0))
print(dizi)


dizi = [5,6,1,7,10,3,14]
print(dizi)
dizi.sort()
print(dizi)
dizi.sort(reverse = True)
print(dizi)


