from tkinter import *

def clicked():
    txt = Entry(window,width=10)
    txt.grid(column=1, row=2)



window = Tk()
window.title("Hesap Makinesi")
window.geometry('350x200')
lbl = Label(window, text="Merhaba")
lbl2 = Label(window, text="")
lbl.grid(column=1, row=0)
btn = Button(window, text="Tıkla", command=clicked)
btn.grid(column=1, row=1)

#txt = Entry(window,width=10)
txt = Entry(window,width=10, state='disabled')
txt.grid(column=1, row=2)

window.mainloop()