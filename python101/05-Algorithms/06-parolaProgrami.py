import random
from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Create Password")
window.geometry('300x300')


def parolaOlustur(isim):
    parola = ""
    for i in range(random.randint(5, 8)):
        b = random.randint(0, 1)
        a = random.randrange(len(isim))
        if b == 0:
            parola += isim[a].lower()
        else:
            parola += isim[a].upper()

    for i in range(10-len(parola)):
        a = random.randint(0, 9)
        parola += str(a)

    return parola


def clicked():
    isim = txt1.get()
    parola = parolaOlustur(isim)
    lbl3 = Label(window, text="Parola: " + parola)
    lbl3.grid(column=0, row=5)


lbl1 = Label(window, text="isim soyisim:")
txt1 = Entry(window, width=30)
lbl2 = Label(window, text="memleket:")
txt2 = Entry(window, width=20)
btn = Button(window, text="parola olustur", command=clicked)

lbl1.grid(column=0, row=0)
txt1.grid(column=0, row=1)
lbl2.grid(column=0, row=2)
txt2.grid(column=0, row=3)
btn.grid(column=0, row=4)

window.mainloop()
