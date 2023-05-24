from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Lear to code")
root.iconbitmap("AMADEico.ico")

frame = LabelFrame(root, text="This is my Frame...", padx=50, pady=50)
frame.pack(padx=100, pady=100)

b=Button(frame, text="Don't click here!!")
b2=Button(frame, text="... or here!!")
b2.grid(row=1, column=1)
b.grid(row=0, column=0)

root.mainloop()