import random

dizi = [1,2,3,4,5,6,6,6,6,6]
print(random.choice(dizi))


a = random.randint(0,1)
if a == 0:
    print(6)
else:
    print(random.randint(1,5))
    