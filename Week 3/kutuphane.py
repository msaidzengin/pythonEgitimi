def ort(a,b):
    return (a+b) / 2

def ort2(a,b):
    cevap = (a+b) / 2
    print(cevap)

def reverse(kelime):
    return kelime[::-1]

def reverse2(kelime):
    yeni = ""
    for i in range(len(kelime)-1,-1,-1):
        yeni += kelime[i]
    return yeni

def fibo(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
    
def fibo2(n):
    liste = []
    liste.append(1)
    liste.append(1)
    for i in range(2,n):
        liste.append(liste[i-1] + liste[i-2])


def diziOrtalamasi(dizi):
    return sum(dizi) / len(dizi)































