from tkinter import *
from tkinter import scrolledtext as st
from tkinter import filedialog as fd
from tkinter import messagebox as mb
#------raiz------
raiz=Tk()
raiz.title("Traducción de ADN")
raiz.resizable(0,0)
raiz.config(bg="mint cream")

#------Lector de archivos

def lector(archivo):
    f=open(archivo,"r", encoding="utf-8", errors="ignore")
    t=f.read()
    f.close()
    t=re.sub('[1()234567890/\.,;*><_,.!?¿#:¡()@]',' ', t)
    t=t.upper()
    t=t.replace("\n", "")
    t=t.replace(" ", "")
    return t


def Guardar():
    nombrearch=fd.asksaveasfilename(initialdir = "/",title = "Guardar como",filetypes = (("txt files","*.txt"),("todos los archivos","*.*")))
    if nombrearch!='':
        archi1=open(nombrearch, "w", encoding="utf-8")
        archi1.write(pantalla.get("1.0", END))
        archi1.close()
        mb.showinfo("Información", "Los datos fueron guardados en el archivo.")

def Abrir():
    nombrearch=fd.askopenfilename(initialdir = "/",title = "Seleccione archivo",filetypes = (("txt files","*.txt"),("todos los archivos","*.*")))
    if nombrearch!='':
        contenido=lector(nombrearch)
        ingresotexto.delete("1.0", END) 
        ingresotexto.insert("1.0", contenido)
        mb.showinfo("Información", "Los datos fueron cargados.")
        
def Nuevo():
    ingresotexto.delete("1.0", END)
    pantalla.get("1.0", END) 
    
def acerca():
    mb.showinfo("ANALIZADOR DEL DOGMA GENETICO", "Es un programa de codigo abierto  y gratuito creado por estudiantes de Fisica de la Universidad de Colombia. \n"
                "\n"
                "El codigo esta escrito en Python 3.7 y la intefaz en Tkinter, con el objetivo de facilitar el analisis de los codigos de la naruraleza para el avance de la Ciencia  \n"
                "\n"
                "Contactenos  \n    "
                " @unal.edu.co\n"
                "bspenad@unal.edu.co"
                "\n \n"
                "2020")
def helps():
    mb.showinfo("¿Cómo usar el traductor?", "El dogma central de la biología dice que la información viaja del ADN al ARN a las proteinas, "
                "este programa permite traducir cadenas de ADN o ARN. \n Para usar el programa simplemente escoja el tipo de cadena que va "
                "a ingresar, el tipo de cadena al que desea convertir y decida si su traducción toma en cuenta el codón de inicio del ADN, "
                "a continuación ingrese su cadena en el recuadro central superior, si esta se encuentra en un archivo de texto .txt puede "
                "abrirla directamente en la opción archivo y abrir, después, haga click en el botón traducir y aparecerá un recuadro confirmando "
                "que la cadena se tradujo exitosamente, si así lo desea puede descargar la cadena traducida en un archivo de texto solo debe "
                "hacer click en la opción archivo y guardar.")

#------Menu------
    
        
menubar=Menu(raiz)
raiz.config(menu=menubar)  

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command=Nuevo)
filemenu.add_command(label="Abrir", command=Abrir)
filemenu.add_command(label="Guardar" , command=Guardar)
#filemenu.add_command(label="Cerrar")
filemenu.add_separator()
filemenu.add_command(label="Salir", command=raiz.destroy)

editmenu = Menu(menubar, tearoff=0)


helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Ayuda", command=helps)
helpmenu.add_separator()
helpmenu.add_command(label="Acerca de...", command=acerca)

menubar.add_cascade(label="Archivo", menu=filemenu)
menubar.add_cascade(label="Ayuda", menu=helpmenu)
#______imagen
imagen=PhotoImage(file="imag013.png")
fondo=Label(raiz,image=imagen).place(x=00,y=00)

#----Titulo-----
etiq = Label(raiz, text=" DOGMA CENTRAL GENÉTICO",bg="beige",font=("Arial Bold", 20))
etiq.grid(row=0,column=2)

#-------pantalla-------
pantallauno=Frame(raiz)
pantallauno.config(bg="gold",width="500",height="300")
pantallauno.config(bd=10)
pantallauno.grid(row=4, column=2,pady=5, rowspan=3)

pantalla=Text(pantallauno, width=50, height=10)
pantalla.config(state=DISABLED)
pantalla.pack()


#_____ingreso_____

ingresotexto=Text(raiz, width=50, height=10)
ingresotexto.grid(row=1,column=2,pady=5, rowspan=3)
#_____codigo boton____
def codigoBoton():
    dna=sort()
    pantalla.config(state=NORMAL)
    pantalla.delete(1.0,END)
    pantalla.insert(END, dna)
    pantalla.config(state=DISABLED)
    mb.showinfo("Hecho","La cadena se tradujo exitosamente")


#______botones seleccion izquierda_______
entradalabel=Label(raiz, text="Cadena de entrada",font=(18),bg="mint cream")
entradalabel.grid(row=1,column=1)
opcionizq=IntVar()
opinicio=IntVar()

def valorizq():
    izquierda=opcionizq.get()
    return izquierda
def valinicio():
    return opinicio.get()
a=Radiobutton(raiz,text="DNA sense",variable=opcionizq, value=1)
a.grid(row=2, column=1)
a.config(bg="pale turquoise")
b=Radiobutton(raiz,text="DNA antisense",variable=opcionizq, value=2)
b.grid(row=3, column=1)
b.config(bg="pale turquoise")
c=Radiobutton(raiz,text="RNA",variable=opcionizq, value=3)
c.grid(row=4, column=1)
c.config(bg="pale turquoise")
inicio=Checkbutton(raiz, text="Codón de inicio",variable=opinicio, onvalue=1, offvalue=0)
inicio.grid(row=5, column=1)
inicio.config(bg="pale turquoise")
boton=Button(raiz, text="Traducir", command= codigoBoton)
boton.grid(row=6, column=1)


#_______ botones seleccion derecha________
entradalabel=Label(raiz, text="Cadena de salida",font=(18),bg="mint cream")
entradalabel.grid(row=1,column=3)

opcionder=IntVar()

def valorder():
    derecha=opcionder.get()
    return derecha
d=Radiobutton(raiz,text="DNA sense",variable=opcionder, value=1)
d.grid(row=2, column=3)
d.config(bg="pale turquoise")
e=Radiobutton(raiz,text="DNA antisense",variable=opcionder, value=2)
e.grid(row=3, column=3)
e.config(bg="pale turquoise")
f=Radiobutton(raiz,text="RNA",variable=opcionder, value=3)
f.grid(row=4, column=3)
f.config(bg="pale turquoise")
g=Radiobutton(raiz,text="Proteinas",variable=opcionder, value=4)
g.grid(row=5, column=3)
g.config(bg="pale turquoise")
h=Radiobutton(raiz,text="ProteinasSimple",variable=opcionder, value=5)
h.grid(row=6, column=3)
h.config(bg="pale turquoise")
#___________-codigo de traduccion-_______________

dic_aminos={'GGG':'Gly','GGA':'Gly','GGU':'Gly','GGC':'Gly','GAG':'Glu','GAA':'Glu','GAU':'Asp','GAC':'Asp','GUG':'Val','GUA':'Val','GUU':'Val','GUC':'Val','GCG':'Ala','GCA':'Ala','GCU':'Ala','GCC':'Ala',
'AGG':'Arg','AGA':'Arg','AGU':'Ser','AGC':'Ser','AAG':'Lys','AAA':'Lys','AAU':'Asn','AAC':'Asn','AUG':'Met','AUA':'Iso','AUU':'Iso','AUC':'Iso','ACG':'Thr','ACA':'Thr','ACU':'Thr','ACC':'Thr',
'UGG':'Try','UGA':'STOP','UGU':'Cys','UGC':'Cys','UAG':'STOP','UAA':'STOP','UAU':'Tyr','UAC':'Tyr','UUG':'Leu','UUA':'Leu','UUU':'Phe','UUC':'Phe','UCG':'Ser','UCA':'Ser','UCU':'Ser','UCC':'Ser',
'CGG':'Arg','CGA':'Arg','CGU':'Arg','CGC':'Arg','CAG':'Gln','CAA':'Gln','CAU':'His','CAC':'His','CUG':'Leu','CUA':'Leu','CUU':'Leu','CUC':'Leu','CCG':'Pro','CCA':'Pro','CCU':'Pro','CCC':'Pro'}

def sort():
    
    dna=ingresotexto.get("1.0","end-1c")
    dna=dna.upper()
    for i in dna:
        if i != "A" and i != "G" and i != "T" and i != "C" and i != "U":
                dna=dna.replace(i,"")
    izquierda=valorizq()
    derecha=valorder()
    inicia=valinicio()
    if izquierda==1 and derecha==2:
        dna=INVERSO(dna)
    elif izquierda==1 and derecha==3:
        dna=RNA(dna)
    elif izquierda==1 and derecha==4:
        dna=RNA(dna)
        dna=Proteinas(dna,inicia)
    elif izquierda==1 and derecha==5:
        dna=Traductor(dna, inicia)    
    elif izquierda==2 and derecha==1:
        dna=INVERSO(dna)
    elif izquierda==2 and derecha==3:
        dna=Transcripcion(dna)
    elif izquierda==2 and derecha==4:
        dna=Transcripcion(dna)
        dna=Proteinas(dna,inicia)
    elif izquierda==2 and derecha==5:
        dna=INVERSO(dna)
        dna=Traductor(dna,inicia)
    elif izquierda==3 and derecha==1:
        dna=invRNA(dna)
    elif izquierda==3 and derecha==2:
        dna=invTranscripcion(dna)
    elif izquierda==3 and derecha==4:
        dna=Proteinas(dna,inicia)
    elif izquierda==3 and derecha==5:
        dna=invRNA(dna)
        dna=Traductor(dna,inicia)        
    else:
        dna=dna
    return dna

 
def RNA (cadena):
    rna=""
    for i in cadena:
        if i=="T":
            rna=cadena.replace("T","U")
    return rna

def invRNA (cadena):
    adn=""
    for i in cadena:
        if i=="U":
            adn=cadena.replace("U","T")
    return adn
   
def INVERSO(cadena):
    adn=""
    for i in cadena:
        if i =="A":
            adn=adn+"T"
        if i=="T":
            adn=adn+"A"
        if i=="C":
            adn=adn+"G"
        if i=="G":
            adn=adn+"C"
    dna=adn
    return dna

def Transcripcion(cadena):
    rna=""
    for i in cadena:
        if i =="A":
            rna=rna+"U"
        if i=="T":
            rna=rna+"A"
        if i=="C":
            rna=rna+"G"
        if i=="G":
            rna=rna+"C"
    return rna

def invTranscripcion(cadena):
    adn=""
    for i in cadena:
        if i =="U":
            adn=adn+"A"
        if i=="A":
            adn=adn+"T"
        if i=="G":
            adn=adn+"C"
        if i=="C":
            adn=adn+"G"
    return adn
    
def Proteinas(cadena,con=0):
    count=0
    amino=""
    proteina=""
    if con==0:
        for i in cadena:
            amino=amino+i
            count=count+1
            if count==3:
                an=dic_aminos[amino]
                count=0
                amino=""
                proteina=proteina+an+", "
    if con==1:
        cuenta=0
        a=0
        for i in cadena:
            amino=amino+i
            count=count+1
            cuenta=cuenta+1
            if count==3:
                if a==1:
                    an=dic_aminos[amino]
                    if an=="STOP":
                        proteina=proteina+an+"\n"
                        a=0
                        amino=""
                        count=0
                    else:
                        proteina=proteina+an+", "
                        count=0
                        amino=""
                if amino=="AUG":
                    a=1
                    amino=""
                    count=0
                else:
                    amino=""
                    count=0
    return proteina

def Traductor(cadena,con=0):
    table = {'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K','AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L','CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V','GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S','TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_', 'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}
    count=0
    amino=""
    proteina=""
    if con==0:
        for i in cadena:
            amino=amino+i
            count=count+1
            if count==3:
                an=table[amino]
                count=0
                amino=""
                proteina=proteina+an
    if con==1:
        cuenta=0
        a=0
        for i in cadena:
            amino=amino+i
            count=count+1
            cuenta=cuenta+1
            if count==3:
                if a==1:
                    an=table[amino]
                    if an=="_":
                        proteina=proteina+an+"\n"
                        a=0
                        amino=""
                        count=0
                    else:
                        proteina=proteina+an
                        count=0
                        amino=""
                if amino=="ATG":
                    a=1
                    amino=""
                    count=0
                else:
                    amino=""
                    count=0
    return proteina


#____________________________________________________________________
raiz.mainloop()
