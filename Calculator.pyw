from tkinter import*

raiz=Tk()

miFrame=Frame(raiz)
miFrame.pack()

operacion=""

reset_pantalla=False

resultado=0
#----------Pantalla-----------------------------------------------

numeroPantalla=StringVar()

pantalla=Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")

#----------Pulsaciones Teclado----------------------------------

def numeroPulsado(num):

    global operacion

    global reset_pantalla

    #if operacion!="":
    #    numeroPantalla.set(num)
    #    operacion=""
    #else:
    #    numeroPantalla.set(numeroPantalla.get() + num)

    if reset_pantalla!=False:

        numeroPantalla.set(num)

        reset_pantalla=False

    else:
        numeroPantalla.set(numeroPantalla.get()+num)

#----------Funcion suma------------------------------------------

def suma(num):

    global operacion 

    global resultado

    global reset_pantalla

    resultado+=float(num)

    operacion="suma"

    reset_pantalla=True

    numeroPantalla.set(resultado)

#-----------Funcion resta------------------------------------------
num1=0

contador_resta=0

def resta(num):

    global operacion

    global resultado

    global num1

    global contador_resta

    global reset_pantalla

    if contador_resta==0:

        num1=float(num)

        resultado=num1

    else:

        if contador_resta==1:

            resultado=num1-float(num)
            
        else:

            resultado=float(resultado)-float(num)

        numeroPantalla.set(resultado)

        resultado=numeroPantalla.get()

    contador_resta=contador_resta+1

    operacion="resta"

    reset_pantalla=True

#----------Funcion multiplicacion------------------------------------

contador_multi=0

def multiplica(num):

    global operacion

    global resultado

    global num1

    global contador_multi

    global reset_pantalla

    if contador_multi==0:

        num1=float(num)

        resultado=num1

    else:

        if contador_multi==1:

            resultado=num1*float(num)

        else:

            resultado=float(resultado)*float(num)

        numeroPantalla.set(resultado)

        resultado=numeroPantalla.get()

    contador_multi=contador_multi+1

    operacion="multiplicacion"

    reset_pantalla=True

#----------Funcion division------------------------------------------

contador_divi=0

def divide(num):

    global operacion

    global resultado

    global num1

    global contador_divi

    global reset_pantalla

    if contador_divi==0:

        num1=float(num)

        resultado=num1

    else:

        if contador_divi==1:

            resultado=num1/float(num)

        else:

            resultado=float(resultado)/float(num)

        numeroPantalla.set(resultado)

        resultado=numeroPantalla.get()

    contador_divi=contador_divi+1

    operacion="division"

    reset_pantalla=True

#----------Funcion el_resultado--------------------------------------

def el_resultado():

    global resultado

    global operacion

    global contador_resta

    if operacion=="suma":

        numeroPantalla.set(resultado+float(numeroPantalla.get()))

        resultado=0

    elif operacion=="resta":

        numeroPantalla.set(float(resultado)-float(numeroPantalla.get()))

        resultado=0

        contador_resta=0

    elif operacion=="multiplicacion":

        numeroPantalla.set(float(resultado)*float(numeroPantalla.get()))

        resultado=0

        contador_multi=0

    elif operacion=="division":

        numeroPantalla.set(float(resultado)/float(numeroPantalla.get()))

        resultado=0

        contador_divi=0

#----------Fila 1-------------------------------------------------

Boton7=Button(miFrame, text="7", width=3, command=lambda:numeroPulsado("7"))
Boton7.grid(row=2, column=1)
Boton8=Button(miFrame, text="8", width=3, command=lambda:numeroPulsado("8"))
Boton8.grid(row=2, column=2)
Boton9=Button(miFrame, text="9", width=3, command=lambda:numeroPulsado("9"))
Boton9.grid(row=2, column=3)
BotonDiv=Button(miFrame, text="/", width=3, command=lambda:divide(numeroPantalla.get()))
BotonDiv.grid(row=2, column=4)

#----------Fila 2-------------------------------------------------

Boton4=Button(miFrame, text="4", width=3, command=lambda:numeroPulsado("4"))
Boton4.grid(row=3, column=1)
Boton5=Button(miFrame, text="5", width=3, command=lambda:numeroPulsado("5"))
Boton5.grid(row=3, column=2)
Boton6=Button(miFrame, text="6", width=3, command=lambda:numeroPulsado("6"))
Boton6.grid(row=3, column=3)
BotonMult=Button(miFrame, text="x", width=3, command=lambda:multiplica(numeroPantalla.get()))
BotonMult.grid(row=3, column=4)

#----------Fila 3-------------------------------------------------

Boton1=Button(miFrame, text="1", width=3, command=lambda:numeroPulsado("1"))
Boton1.grid(row=4, column=1)
Boton2=Button(miFrame, text="2", width=3, command=lambda:numeroPulsado("2"))
Boton2.grid(row=4, column=2)
Boton3=Button(miFrame, text="3", width=3, command=lambda:numeroPulsado("3"))
Boton3.grid(row=4, column=3)
BotonRest=Button(miFrame, text="-", width=3, command=lambda:resta(numeroPantalla.get()))
BotonRest.grid(row=4, column=4)

#----------Fila 4-------------------------------------------------

Boton0=Button(miFrame, text="0", width=3, command=lambda:numeroPulsado("0"))
Boton0.grid(row=5, column=1)
BotonComa=Button(miFrame, text=",", width=3, command=lambda:numeroPulsado("."))
BotonComa.grid(row=5, column=2)
BotonIgual=Button(miFrame, text="=", width=3, command=lambda:el_resultado())
BotonIgual.grid(row=5, column=3)
BotonSum=Button(miFrame, text="+", width=3, command=lambda:suma(numeroPantalla.get()))
BotonSum.grid(row=5, column=4)

mainloop()