from tkinter import*
raiz=Tk()
miFrame=Frame(raiz, width=1200,heigh=600)
miFrame.pack()

#_____Nombre______

minombre=StringVar()                                            # Associate function
cuadroNombre=Entry(miFrame, textvariable=minombre)              # Create Entry, textvariable: write the variable
#cuadroTexto.pack()                                             # Pack Entry
#cuadroTexto.place(x=100, y=100)                                # Location Entry
cuadroNombre.grid(row=0, column=1, padx=5, pady=10)             # Location Entry
cuadroNombre.config(fg="red", justify="right")                  # Config Entry

NombreLabel=Label(miFrame, text="Nombre:")                      # Create Text
#NombreLabel.place(x=100, y=100)                                # It's not advisable
NombreLabel.grid(row=0, column=0, sticky="w", padx=5, pady=10)            # Location Label

#_____Apellido______

cuadroApellido=Entry(miFrame)                  # Create Entry
cuadroApellido.grid(row=1, column=1, padx=5, pady=10)          # Location Entry

ApellidoLabel=Label(miFrame, text="Apellido:")  # Create Text
ApellidoLabel.grid(row=1, column=0, sticky="w", padx=5, pady=10)           # Location Label

#_____Dirección______

cuadroUbicacion=Entry(miFrame)                  # Create Entry
cuadroUbicacion.grid(row=2, column=1, padx=5, pady=10)           # Location Entry

UbicacionLabel=Label(miFrame, text="Dirección:")  # Create Text
UbicacionLabel.grid(row=2, column=0, sticky="w", padx=5, pady=10)           # Location Label, padx and pady add pixels to separate from other widget

#_____Password______

cuadroPass=Entry(miFrame)                  # Create Entry
cuadroPass.grid(row=3, column=1, padx=5, pady=10)           # Location Entry
cuadroPass.config(show="*")

PassLabel=Label(miFrame, text="Password:")  # Create Text
PassLabel.grid(row=3, column=0, sticky="w", padx=5, pady=10)           # Location Label, padx and pady add pixels to separate from other widget

#_____Text______

textoComentario=Text(miFrame, width=16, height=10)                  # Create Text
textoComentario.grid(row=4, column=1, padx=5, pady=10)           # Location Entry


ComentariosLabel=Label(miFrame, text="Comentarios:")  # Create Text
ComentariosLabel.grid(row=4, column=0, sticky="w", padx=5, pady=10)           # Location Label, padx and pady add pixels to separate from other widget

scrollVert=Scrollbar(miFrame, command=textoComentario.yview)        # Create a scrollbar
scrollVert.grid(row=4, column=2, sticky="nsew")                     # Location scroll 

textoComentario.config(yscrollcommand=scrollVert.set)               # Location scrollbar according to text

#__________Button_________

def codigoBoton():                                                  # Creat function to Button
    minombre.set("Diego")                                           # Write name

BotonEnvio=Button(raiz, text="Enviar", command=codigoBoton)         # Creat Button
BotonEnvio.pack()                                                   # Pack Button

raiz.mainloop()