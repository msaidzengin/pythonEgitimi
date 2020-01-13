from tkinter import *
window = Tk()
window.title("Hesap Makinesi")
window.geometry('350x200')
lbl = Label(window, text="Merhaba")
lbl.grid(column=0, row=0)
btn = Button(window, text="Hesapla")
btn.grid(column=0, row=1)
window.mainloop()