from tkinter import *

root = Tk()
root.title("Simple Calculator")

display=Entry(root, width=35, borderwidth=5)
display.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_add(number):
    #display.delete(0, END)
    current=display.get()
    display.delete(0, END)
    display.insert(0, str(current) + str(number))
    return
    
def button_clear():
    display.delete(0, END)

def button_sum():
    first_number=display.get()
    global f_num
    f_num=int(first_number)
    display.delete(0, END)

def button_equal():
    second_number=display.get()
    display.delete(0, END)
    display.insert(0, f_num + int(second_number))
    

button_1=Button(root, text="1", padx=40, pady=20, command=lambda: button_add(1))
button_2=Button(root, text="2", padx=40, pady=20, command=lambda: button_add(2))
button_3=Button(root, text="3", padx=40, pady=20, command=lambda: button_add(3))
button_4=Button(root, text="4", padx=40, pady=20, command=lambda: button_add(4))
button_5=Button(root, text="5", padx=40, pady=20, command=lambda: button_add(5))
button_6=Button(root, text="6", padx=40, pady=20, command=lambda: button_add(6))
button_7=Button(root, text="7", padx=40, pady=20, command=lambda: button_add(7))
button_8=Button(root, text="8", padx=40, pady=20, command=lambda: button_add(8))
button_9=Button(root, text="9", padx=40, pady=20, command=lambda: button_add(9))
button_0=Button(root, text="0", padx=40, pady=20, command=lambda: button_add(0))

button_plus=Button(root, text="+", padx=39, pady=20, command=button_sum)
button_subtract=Button(root, text="-", padx=39, pady=20, command=button_subtract)
button_multiply=Button(root, text="x", padx=39, pady=20, command=button_multiply)
button_divide=Button(root, text="/", padx=39, pady=20, command=button_divide)

button_equal=Button(root, text="=", padx=91, pady=20, command=button_equal)
button_clear=Button(root, text="Clear", padx=79, pady=20, command=button_clear)

# Put the buttons on the screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_plus.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)


root.mainloop()