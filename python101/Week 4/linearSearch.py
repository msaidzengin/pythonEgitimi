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

#Output is -1. Because element x is not present in arr[].