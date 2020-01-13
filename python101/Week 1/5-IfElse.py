sayi = int(input("Bir sayı giriniz: "))
if sayi % 2 == 0:
    print("Bu bir çift sayı.")
else:
    print("Bu bir tek sayı.")




# 7-8-9-10 yaş ilkokul
# 11-12-13-14 yaş ortaokul
# 15-16-17-18 yaş lise
# 19-20-21-22 yaş üniversite
# olarak varsayıyoruz.

yas = int(input("Kaç yaşındasın: "))
if ( yas < 7 ):
    print("Hmm, okuma yazman var mı senin?")
elif ( yas > 6 and yas < 11 ):
    print("İlkokula gidiyor olmalısın.")
elif ( yas > 10 and yas < 15 ):
    print("Oratokula gidiyor olmalısın.")
elif ( yas > 14 and yas < 19 ):
    print("Liseye gidiyor olmalısın.")
elif ( yas > 18 and yas < 23 ):
    print("Üniversite gidiyor olmalısın.")
else:
    print("Okulu bitirmiş olman lazım...")