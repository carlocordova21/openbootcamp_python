from tkinter import *

def sel():
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)

root = Tk()
root.geometry("200x150")
var = IntVar()
R1 = Radiobutton(root, text="Option 1", variable=var, value=1, command=sel)
R1.pack(anchor=W, fill="both")
R2 = Radiobutton(root, text="Option 2", variable=var, value=2, command=sel)
R2.pack(anchor=W, fill="both")
R3 = Radiobutton(root, text="Option 3", variable=var, value=3, command=sel)
R3.pack(anchor=W, fill="both")

label = Label(root)
label.pack()

def reset():
   var.set(None)         
   label.config(text='')   

B = Button(root, text="Reiniciar", command=reset)
B.pack(anchor=W, fill="both")

root.mainloop()