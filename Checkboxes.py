from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

root=Tk()
root.title("Open Files Dialog Box")
root.iconbitmap("AMADEico.ico")
root.geometry("400x400")

def show():
    myLabel=Label(root, text=var.get()).pack()

var=StringVar()

c=Checkbutton(root, text="Check this box, I dare you!", variable=var, onvalue="Pizza", offvalue="Hamburguer")
c.deselect()
c.pack()

mybutton=Button(root, text="Show Slection", command=show).pack()

root.mainloop()