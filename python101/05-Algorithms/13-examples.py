liste = [45,15,16,17,18,48,49,5,6,7]
yeniListe = []
uzunluk = len(liste)
for i in range(uzunluk):
    minimum = min(liste)
    yeniListe.append(minimum)
    liste.remove(minimum)
    print(yeniListe)    
