#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Searching an element in a list/array in python 
# can be simply done using 'in' operator 
# Example: 
# if x in arr: 
#   print arr.index(x) 
  

# If you want to implement Linear Search in python 
  
# Linearly search x in arr[] 
# If x is present then return its location 
# else return -1 
  
def search(arr, x): 
    for i in range(len(arr)): 
        if arr[i] == x: 
            return i   #index of number
  
    return -1


arr = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
x = 110

print(search(arr,x))

# Output is 6. 
# Index of "110" is 6.

y = 175
print(search(arr,y))


# In[19]:


# Python program for implementation of Insertion Sort 
  
# Function to do insertion sort 
def insertionSort(arr): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key 
  
  
# Driver code to test above 
arr = [12, 11, 13, 5, 6] 
insertionSort(arr) 
for i in range(len(arr)): 
    print ("% d" % arr[i]) 


# In[8]:


for i in range(1,4): 
    for j in range(i):
        print("*",end=" ")
    print()


# In[14]:


#print(*range(1,5))
#liste = list(range(1,5))
liste = [10,2,3,4,5]
for i in liste:
    print(i,end="")


# In[16]:


text = "Burası Btk"
for i in text:
    print(i,end="")


# In[5]:


print("btk","test","abc",sep="-", end =" ")
print("btk","test","abc",sep="-")


# In[3]:


print("btk", "python","sınav", sep ="-")


# In[11]:


liste = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for eleman in liste:
    if((eleman % 3) == 0):
        continue
    elif(eleman == 11):
        break
    else:
        print(eleman)


# In[12]:


def topla(a,b):
    return a+b
print(topla(3,4))


# In[4]:


def faktoriyel(sayi):
    sonuc = 1
    if(sayi < 1):
        sonuc = 1
    else:
        for i in range(1,sayi + 1) :
            sonuc *= i
    
    return sonuc

faktoriyel(5)


# In[18]:


cumle = input("Lütfen cümle giriniz: ")

#(Yöntem 1)
counter = 0
for c in cumle:
    if c == 'a':
        counter += 1
print(counter)

#(Yöntem 2)
toplam = 0
for i in range(len(cumle)):
    if cumle[i] == 'a':
        toplam += 1
print(toplam)


# In[27]:


text = "Merhaba dünya"
print(text[::2])


# In[17]:


dizi = [1,2,3,4,5,6,7,8]
print(dizi[2:5])


# In[6]:


dizi.pop()


# In[7]:


dizi


# In[8]:


dizi.pop(2)


# In[ ]:




