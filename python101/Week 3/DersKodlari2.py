#!/usr/bin/env python
# coding: utf-8

# In[3]:


sozluk ={"elma":"Apple","armut":4,"muz":7}

sozluk["elma"]


# In[4]:


def


# In[6]:


print(sozluk)


# In[7]:


sozluk[0]


# In[8]:


sozluk.values()


# In[9]:


sozluk.keys()


# In[10]:


sozluk.items()


# In[12]:


for anahtar, deger in sozluk.items():
    print("key", anahtar)
    print("val", deger)
    


# In[13]:


def selamla():
    print("merhaba")

selamla()


# In[24]:


def topla(a=1,b=1,c = 7):
    return a + b + c

print(topla(c=3))


# In[26]:


print("brk", "emre", sep="\n")


# In[29]:


bool(0)


# In[32]:


def f(x,y):
    return x**2 + 2*y + 9

print(5 + f(4,3))


# In[38]:


#faktöriyel
sayı = int(input('Sayı değerini giriniz:'))
def faktoriyel(x):
    çarp = 1
    for oku in range(x):
        çarp = çarp*(oku+1)
    return çarp

print('Faktöriyel : ',faktoriyel(sayı))    


# In[42]:


say = int("asd")


# In[44]:


try:
    say1 = int(input("say 1 "))
    say2 = int(input("say 2: "))
    say = say1/say2
except ZeroDivisionError:
    print("Sıfıra bölemezsin")
except ValueError:
    print("Lütfen düzgün bir sayı giriniz")


# In[ ]:




