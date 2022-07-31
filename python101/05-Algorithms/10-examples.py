girdi = input("(x,y) ikilisi giriniz: ")

sayılar = girdi.split(",")
x = int(sayılar[0])
y = int(sayılar[1])

print("*" * x)
for i in range(y-2):
    print("*" + (x-2) * " " + "*")
print("*" * x)
