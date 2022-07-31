for n in range(1000001,2000000,2):
    counter = 0
    for i in range(2, n//2 + 1):
        if n % i == 0:
            counter += 1
            break
            
    if counter == 0:
        print(n)

