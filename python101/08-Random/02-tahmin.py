import random

counter = 0
tahmin = 0
x = -1
y = 1001
cevap = ""

while cevap != "do�ru":
    counter += 1
    tahmin = random.randint(x+1,y-1)
    print(tahmin)
    cevap = input("[k���k - b�y�k - do�ru]: ")
    if cevap == "k���k":
        x = tahmin
    elif cevap == "b�y�k":
        y = tahmin
        
print("Buldum! Tahmin etti�in say�:", tahmin)
print("Tahmin say�s�", counter)
