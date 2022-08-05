import random


def createPassword(length):
    password = ""
    for i in range(length):
        password += random.choice("abcdefghijklmnopqrstuvwxyz0123456789")
    return password


passwords = [createPassword(random.randrange(5, 15)) for i in range(100000)]

with open('passwords.txt', 'w', encoding='utf-8') as f:
    for password in passwords:
        f.write(password + "\n")


with open('passwords.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]


print(lines[0])
print(lines[1])
