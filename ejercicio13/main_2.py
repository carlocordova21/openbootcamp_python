from tkinter import *
from tkinter.ttk import Combobox

def sel():
   if combo.get() != "":
      selection = "You selected the option " + str(combo.get())
   else:
      selection = "You must select an option"

   label.config(text = selection)


root = Tk()
root.geometry("200x150")
var = IntVar()

combo = Combobox(state="readonly", values=["Option1", "Option2", "Option3", "Option4"])
combo.pack()

label = Label(root)
label.pack()

B = Button(root, text="Mostrar opcion", command=sel)
B.pack(anchor=W, fill="both")

root.mainloop()