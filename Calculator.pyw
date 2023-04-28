from tkinter import*

raiz=Tk()

miFrame=Frame(raiz)
miFrame.pack()

#----------Pantalla-----------------------------------------------

pantalla=Entry(miFrame)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")

#----------Fila 1-------------------------------------------------

Boton7=Button(miFrame, text="7", width=3)
Boton7.grid(row=2, column=1)
Boton8=Button(miFrame, text="8", width=3)
Boton8.grid(row=2, column=2)
Boton9=Button(miFrame, text="9", width=3)
Boton9.grid(row=2, column=3)
BotonDiv=Button(miFrame, text="/", width=3)
BotonDiv.grid(row=2, column=4)

#----------Fila 2-------------------------------------------------

Boton4=Button(miFrame, text="4", width=3)
Boton4.grid(row=3, column=1)
Boton5=Button(miFrame, text="5", width=3)
Boton5.grid(row=3, column=2)
Boton6=Button(miFrame, text="6", width=3)
Boton6.grid(row=3, column=3)
BotonMult=Button(miFrame, text="x", width=3)
BotonMult.grid(row=3, column=4)

#----------Fila 3-------------------------------------------------

Boton1=Button(miFrame, text="1", width=3)
Boton1.grid(row=4, column=1)
Boton2=Button(miFrame, text="2", width=3)
Boton2.grid(row=4, column=2)
Boton3=Button(miFrame, text="3", width=3)
Boton3.grid(row=4, column=3)
BotonRest=Button(miFrame, text="-", width=3)
BotonRest.grid(row=4, column=4)

#----------Fila 4-------------------------------------------------

Boton0=Button(miFrame, text="0", width=3)
Boton0.grid(row=5, column=1)
BotonComa=Button(miFrame, text=",", width=3)
BotonComa.grid(row=5, column=2)
BotonIgual=Button(miFrame, text="=", width=3)
BotonIgual.grid(row=5, column=3)
BotonSum=Button(miFrame, text="+", width=3)
BotonSum.grid(row=5, column=4)

mainloop()