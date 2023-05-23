from tkinter import *

root=Tk()

def myClick():
    myLabel3=Label(root, text="Look! I clicked a Button!!")
    myLabel3.pack()

# Creating a Label Widget
#myLabel1=Label(root, text="Hello World!").grid(row=0, column=0)
#myLabel2=Label(root, text="My name is Diego Martinez")
#myButton=Button(root, text="Click Me!")
#myButton=Button(root, text="Click Me!", state=DISABLED)
#myButton=Button(root, text="Click Me!", padx=50, pady=10)
myButton=Button(root, text="Click Me!", command=myClick, fg="blue", bg="green")


# Showing it onto the screen

#myLabel2.grid(row=1, column=2)
#myButton.grid(row=1, column=3)
myButton.pack()

root.mainloop()