import math

n = 0
while n != -1:
    n = int(input("bir rakam giriniz: "))
    if n >= 0 and n <= 9:
        print(n**2)
        print(n*n)
        print(math.pow(n,2))
    elif n == -1:
        break
    else:
        print("hatalı giriş")
    
print("program bitti")

