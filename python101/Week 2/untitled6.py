n = int(input("bir rakam giriniz: "))

fact = 1
for i in range(1, n+1):
    fact *= i
    print(str(i) + "! = " + str(fact))
