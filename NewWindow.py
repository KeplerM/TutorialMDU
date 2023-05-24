from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Lear to code")
root.iconbitmap("AMADEico.ico")


def open():
    global my_img

    top=Toplevel()
    top.title("My second window")
    top.iconbitmap("AMADEico.ico")
    my_img=ImageTk.PhotoImage(Image.open("images/00.png"))
    my_label=Label(top, image=my_img).pack()
    btn2=Button(top, text="close window", command=top.destroy).pack()
    

btn=Button(root, text="open second window", command=open)
btn.pack()

root.mainloop()