# Recursive examples

#yontem 1
def factorial( n ):
   if n < 1:    #base case
       return 1
   else:
       returnNumber = n * factorial( n - 1 )  # recursive call
       print(str(n) + '! = ' + str(returnNumber))
       return returnNumber



#yontem 2
def fac(n):
    return 1 if (n < 1) else n * fac(n-1)

fac(4)
