from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Lear to code")
root.iconbitmap("AMADEico.ico")

my_img=ImageTk.PhotoImage(Image.open("AMADEico.png"))
my_label=Label(image=my_img)
my_label.pack()


button_quite=Button(root, text="Exit Program", command=root.quit)
button_quite.pack()

root.mainloop()