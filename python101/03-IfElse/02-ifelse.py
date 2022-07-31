# i > j
# i >= j
# i < j
# i <= j
# i == j  equality test, True if i is the same as j
# i != j  inequality test, True if i not the same as j

a = 5
b = 3

if a == 5 and b == 3:
    print("ikisi de dogruymus")

if a == 5 and b == 4:
    print("b = 4 olmadigi icin bu print ekrana basilmayacak.")

if a == 5 or b == 34567:
    print("bir tanesi dogruymus.")

if a == 3 or b == 2:
    print("ikisi de yanlis oldugu icin bu ekrana basilmayacak")