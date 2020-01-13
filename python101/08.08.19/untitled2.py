dizi = [[0,1,2],[3,4,5,5,5,5,5,5],[6,7]]



print(dizi)
print(dizi[0])
print(dizi[-1])

print(dizi[1][0])
print("--------")

for i in dizi:
    for j in i:
        print(j , end = " ")
    print()
        
        
for i in range(len(dizi)):
    for j in range(len(dizi[i])):
        print(dizi[i][j]  , end = " ")
    print()