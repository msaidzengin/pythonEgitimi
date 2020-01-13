

print("--Dongu 1--")
s = "ornek dongu"
for index in range(len(s)):
    if s[index] == 'i' or s[index] == 'o':
        print("There is an i or o")

print("--Dongu 2--")
for char in s:
    if char == 'i' or char == 'u':
        print("There is an i or u")