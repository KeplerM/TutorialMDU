from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Lear to code")
root.iconbitmap("AMADEico.ico")

r=IntVar()
r.set("2")

TOPPINGS=[
    ("Pepperoni","Pepperoni"),
    ("Cheese","Cheese"),
    ("Mushroom","Mushroom"),
    ("Onion","Onion"),
]

pizza=StringVar()
pizza.set("Pepperoni")

for text, topping in TOPPINGS:
    Radiobutton(root, text=text, variable=pizza, value=topping).pack(anchor=W)


def clicked(value):
    mylabel=Label(root, text=value)
    mylabel.pack()

#Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda:clicked(r.get())).pack()
#Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda:clicked(r.get())).pack()
#Radiobutton(root, text="Option 3", variable=r, value=3, command=lambda:clicked(r.get())).pack()

#mylabel=Label(root, text=pizza.get())
#mylabel.pack()

mybutton=Button(root, text="Click me!", command=lambda:clicked(pizza.get()))
mybutton.pack()

root.mainloop()