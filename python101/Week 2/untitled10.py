liste = [45,15,16,17,18,48,49,5,6,7]

minimum = liste[0]
for i in liste:
    if i < minimum:
        minimum = i
        
print("min:", minimum)

maximum = liste[0]
for i in liste:
    if i > maximum:
        maximum = i
        
print("max:", maximum)

