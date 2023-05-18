from tkinter import *

root=Tk()

root.title("Ejemplo")

playa=IntVar()
montana=IntVar()
desierto=IntVar()

def opcionesViaje():

    opcionEscogida=""
    if(playa.get()==1):
        opcionEscogida+=" playa"

    if(montana.get()==1):
        opcionEscogida+=" montaña"

    if(desierto.get()==1):
        opcionEscogida+=" desierto"

    textofinal.config(text=opcionEscogida)

foto=PhotoImage(file="avion.png")
Label(root, image=foto, width=100, height=100).pack()

frame=Frame(root)
frame.pack()

Label(frame, text="Elige destinos", width=50).pack()

Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Montaña", variable=montana, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Desierto", variable=desierto, onvalue=1, offvalue=0, command=opcionesViaje).pack()

textofinal=Label(frame)
textofinal.pack()

root.mainloop()