#!/usr/bin/env python
# coding: utf-8

# In[2]:


def selamla():
    print("Merhaba")
    
selamla()


# In[3]:


def selamla(isim):
    print("Merhaba", isim)
    
selamla("İsmail")


# In[4]:


print(selamla(isim))#fonksiyonumuz geriye değer dönmediği için hata aldık


# In[ ]:


def selamla(isim):
    return isim

print("Merhaba", selamla("BTK"))


# In[6]:


def faktoriyel(sayi):
    sonuc = 1
    if(sayi == 0 or sayi == 1):
        sonuc = 1
    else:
        for i in range(1,sayi + 1) :
            sonuc *= i
    
    return sonuc

faktoriyel(6)


# In[7]:


def ciftSayiMi(sayi):
    if((sayi % 2) == 0):
        return True
    else:
        return False

liste = []
for i in range(1,101):
    if(ciftSayiMi(i)):
        liste.append(i)

print(liste)
    


# In[25]:


# is Prime metodu parametre olarak bir integer alır.
# Eger asal sayı ise true, değilse false return eder.
def isPrime(n):
    if(n<2):
        return False
    for i in range (2,n):
        if n % i == 0:
            return False
    return True



#prime Numbers dizisinin içinde 0,100 arasındaki asal sayılar bulunuyor.
primeNumbers = []
for i in range (100):
    if isPrime(i):
        primeNumbers.append(i)
    
print(primeNumbers)
print("\n")


# Fonksiyona parametre olarak 2 adet sayı verilir.
# Bu iki sayı arasındaki tüm asal sayılar ekrana basılır.
def ikiSayiArasindakiAsalSayilar(a,b):
    for i in range(a,b):
        if isPrime(i):
            print(i, end=", ")
    
print(ikiSayiArasindakiAsalSayilar (100,200))


# In[23]:


liste = list(range(1,101))
ciftSayilar = [i for i in liste if((i % 2) == 0)]
print(ciftSayilar)


# In[24]:


ciftMi = lambda x : ((x % 2) == 0)

print(ciftMi(2))
print(ciftMi(3))


# In[ ]:




def toplam(*sayilar):
    toplam = 0
    for i in sayilar:
        toplam += i
    return toplam

print ( toplam(1,2,4,5,7) )