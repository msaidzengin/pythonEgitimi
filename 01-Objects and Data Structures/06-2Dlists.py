def printList(liste):
    for i in liste:
        for j in i:
            print(j)


def increaseList(liste):
    for i in range(len(liste)):
        for j in range(len(liste[i])):
            liste[i][j] += 1
    return liste


def reversePrint(liste):
    print([i[::-1] for i in liste[::-1]])


liste = [
    [1, 2, 3, 6, 9],
    [4, 5, 6, 1],
    [7, 8, 9]
]
print(liste)
liste = increaseList(liste)
print(liste)
reversePrint(liste)
