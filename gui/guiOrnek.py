from tkinter import *

def clicked():
    islem = selected.get()
    a = int(txt1.get())
    b = int(txt2.get())
    if(islem == 1):
        cvp = a + b
    elif islem == 2:
        cvp = a-b
    else:
        cvp = a/b
    lbl = Label(window, text="" + str(cvp))
    lbl.grid(column=1, row=3)


window = Tk()
window.title("Hesap Makinesi")
window.geometry('500x500')


txt1 = Entry(window,width=20)
txt1.grid(column=0, row=0)

txt2 = Entry(window,width=20)
txt2.grid(column=2, row=0)

selected = IntVar()
rad1 = Radiobutton(window,text='+', value=1, variable=selected)
rad2 = Radiobutton(window,text='-', value=2, variable=selected)
rad3 = Radiobutton(window,text='/', value=3, variable=selected)
rad1.grid(column=0, row=1)
rad2.grid(column=1, row=1)
rad3.grid(column=2, row=1)

btn = Button(window, text="Hesapla", command=clicked)
btn.grid(column=1, row=2)



window.mainloop()