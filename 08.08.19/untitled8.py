dizi = [5,6,1,7,10,3,14]
yeniDizi = [1,2,3,4,7]

length = len(dizi)
for i in range(length):
    minimum = min(dizi)
    yeniDizi.append(minimum)
    dizi.remove(minimum)z


while len(dizi) != 0:
    minimum = min(dizi)
    yeniDizi.append(minimum)
    dizi.remove(minimum)

print(yeniDizi)