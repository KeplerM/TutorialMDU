from tkinter import*
root=Tk()
miFrame=Frame(root, width=500, height=400)
miFrame.pack()
#miLabel=Label(miFrame, text="Hola alumnos de Python")   # Create Label
#miLabel.place(x=100, y=200)                             # Location Label [pixeles]
miImagen=PhotoImage(file="amade.png")
Label=Label(miFrame, image=miImagen).place(x=100, y=200) # Abbreviate Label commands 
#Label=Label(miFrame, text="Hola mundo", fg="red", font=("Comic Sans MS", 18)).place(x=100, y=200) # Abbreviate Label commands 






root.mainloop()