n = int(input("n giriniz: "))

for i in range(n):
        print("* " * (i+1))


for i in range(n):
    for j in range(i+1):
        print("*",end= " ")
    print()

print("merhaba" * 3)