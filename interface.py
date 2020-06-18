from tkinter import *
#------raiz------
raiz=Tk()
raiz.title("Traducción de ADN")
#raiz.geometry("800x600")
raiz.resizable(0,0)
raiz.config(bg="mint cream")
#-------pantalla-------
pantallauno=Frame(raiz)
pantallauno.config(bg="gold",width="500",height="300")
pantallauno.config(bd=20)
pantallauno.grid(row=3, column=2,pady=5, rowspan=2)

#_____ingreso_____

ingresotexto=Text(raiz, width=50, height=10)
ingresotexto.grid(row=1,column=2,pady=5, rowspan=2)
#_____codigo boton____
def codigoBoton():
    z=ingresotexto.get("1.0","end-1c")
    return z
    

#______botones seleccion izquierda_______
entradalabel=Label(raiz, text="Cadena de entrada",font=(18),bg="mint cream")
entradalabel.grid(row=0,column=1)
opcionizq=IntVar()

def valorizq():
    return None
a=Radiobutton(raiz,text="DNA sense",variable=opcionizq, value=1)
a.grid(row=1, column=1)
a.config(bg="pale turquoise")
b=Radiobutton(raiz,text="DNA antisense",variable=opcionizq, value=2)
b.grid(row=2, column=1)
b.config(bg="pale turquoise")
c=Radiobutton(raiz,text="RNA",variable=opcionizq, value=3)
c.grid(row=3, column=1)
c.config(bg="pale turquoise")
boton=Button(raiz, text="Traducir", command= codigoBoton)
boton.grid(row=4, column=1)


#_______ botones seleccion derecha________
entradalabel=Label(raiz, text="Cadena de salida",font=(18),bg="mint cream")
entradalabel.grid(row=0,column=3)

opcionder=IntVar()

def valorder():
    return None
d=Radiobutton(raiz,text="DNA sense",variable=opcionder, value=1)
d.grid(row=1, column=3)
d.config(bg="pale turquoise")
e=Radiobutton(raiz,text="DNA antisense",variable=opcionder, value=2)
e.grid(row=2, column=3)
e.config(bg="pale turquoise")
f=Radiobutton(raiz,text="RNA",variable=opcionder, value=3)
f.grid(row=3, column=3)
f.config(bg="pale turquoise")
g=Radiobutton(raiz,text="Proteinas",variable=opcionder, value=4)
g.grid(row=4, column=3)
g.config(bg="pale turquoise")
raiz.mainloop()
