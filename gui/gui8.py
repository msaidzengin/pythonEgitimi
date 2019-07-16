from tkinter import *
from tkinter.ttk import *
window = Tk()
window.title("Deneme")
window.geometry('350x200')
combo = Combobox(window)
combo['values']= (1, 2, 3, 4, 5, "Seç")
combo.current(5) #set the selected item
combo.grid(column=0, row=0)
window.mainloop()