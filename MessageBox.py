from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Lear to code")
root.iconbitmap("AMADEico.ico")

#showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    response = messagebox.askquestion("This is my Popup!", "Hello world")
    Label(root, text=response).pack()
    if response == "yes":
        Label(root, text="You clicked: Yes!").pack()
    else:
        Label(root, text="You clicked: No!!").pack()

Button(root, text="Popup", command=popup).pack()

root.mainloop()