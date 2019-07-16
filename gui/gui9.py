from tkinter import *
from tkinter.ttk import *
window = Tk()
window.title("Deneme")
window.geometry('350x200')
chk_state = BooleanVar()
chk_state.set(True) #set check state
chk = Checkbutton(window, text='Seç', var=chk_state)
chk.grid(column=0, row=0)
window.mainloop()

#chk_state = IntVar()
#chk_state.set(0) #uncheck
#chk_state.set(1) #check