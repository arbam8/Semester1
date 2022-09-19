#************************************************** Prueba de GUI - Septiembre 16, 2022 ****************

from tkinter import *

#-------------------------------------------------- Ventana principal

win=Tk()

#-------------------------------------------------- Se importa la imagen central

logo=PhotoImage(file="rrlogo2.png")

#************************************************** En esta sección ************************************
#************************************************** se definen las variables del programa **************

#-------------------------------------------------- Variables para cantidad de postres

choco=StringVar(0)
elote=StringVar(0)
queso=StringVar(0)
limon=StringVar(0)
calab=StringVar(0)

chocoQ=0
eloteQ=0
quesoQ=0
limonQ=0
calabQ=0

subtotal=StringVar(0)
subtotalQ=0
descuento=StringVar(0)
descuentoQ=0
iva=StringVar(0)
ivaQ=0
total=StringVar(0)
totalQ=0

desc=IntVar()
env=IntVar()

#************************************************** En esta sección ************************************
#************************************************** se definen las funciones del programa **************

#-------------------------------------------------- Funciones suma para botones de aumentar

def suma1():
    global chocoQ
    if chocoQ<5:
        chocoQ+=1
        choco.set(chocoQ)
    elif chocoQ==5:
        chocoQ=5
        choco.set(chocoQ)
def suma2():
    global eloteQ
    if eloteQ<5:
        eloteQ+=1
        elote.set(eloteQ)
    elif eloteQ==5:
        eloteQ=5
        elote.set(eloteQ)
def suma3():
    global quesoQ
    if quesoQ<5:
        quesoQ+=1
        queso.set(quesoQ)
    elif quesoQ==5:
        quesoQ=5
        queso.set(quesoQ)
def suma4():
    global limonQ
    if limonQ<5:
        limonQ+=1
        limon.set(limonQ)
    elif limonQ==5:
        limonQ=5
        limon.set(limonQ)
def suma5():
    global calabQ
    if calabQ<5:
        calabQ+=1
        calab.set(calabQ)
    elif calabQ==5:
        calabQ=5
        calab.set(calabQ)
        
#-------------------------------------------------- Funciones resta para botones de disminuir

def resta1():
    global chocoQ
    if chocoQ>0:
        chocoQ-=1
        choco.set(chocoQ)
    elif chocoQ==0:
        chocoQ=0
        choco.set(chocoQ)
def resta2():
    global eloteQ
    if eloteQ>0:
        eloteQ-=1
        elote.set(eloteQ)
    elif eloteQ==0:
        eloteQ=0
        elote.set(eloteQ)
def resta3():
    global quesoQ
    if quesoQ>0:
        quesoQ-=1
        queso.set(quesoQ)
    elif quesoQ==0:
        quesoQ=0
        queso.set(quesoQ)
def resta4():
    global limonQ
    if limonQ>0:
        limonQ-=1
        limon.set(limonQ)
    elif limonQ==0:
        limonQ=0
        limon.set(limonQ)
def resta5():
    global calabQ
    if calabQ>0:
        calabQ-=1
        calab.set(calabQ)
    elif calabQ==0:
        calabQ=0
        calab.set(calabQ)
        
#-------------------------------------------------- Función para subtotal

def result():
    if (env.get())==0:
        subtotalQ=chocoQ*330+eloteQ*280+quesoQ*240+limonQ*220+calabQ*260
        subtotal.set(subtotalQ)
    elif chocoQ==0 and eloteQ==0 and quesoQ==0 and limonQ==0 and calabQ==0:
        subtotalQ=chocoQ*330+eloteQ*280+quesoQ*240+limonQ*220+calabQ*260
        subtotal.set(subtotalQ)
    elif (env.get())==1:
        subtotalQ=chocoQ*330+eloteQ*280+quesoQ*240+limonQ*220+calabQ*260+150
        subtotal.set(subtotalQ)
    if (desc.get())==0:
        descuentoQ=subtotalQ
        descuento.set(descuentoQ)
        ivaQ=round(descuentoQ*.16,2)
        iva.set(ivaQ)
        totalQ=round(descuentoQ*1.16,2)
        total.set(totalQ)
    elif (desc.get())==1:
        descuentoQ=round(subtotalQ*.95,2)
        descuento.set(descuentoQ)
        ivaQ=round(descuentoQ*.16,2)
        iva.set(ivaQ)
        totalQ=round(descuentoQ*1.16,2)
        total.set(totalQ)

#************************************************** En esta sección ************************************
#************************************************** se definen las características de la intefaz *******

#-------------------------------------------------- Se dan características a ventana raíz

win.title("Double R Diner Pies")
win.resizable(0,0)
#win.iconbitmap("nombre_del_favicon.ico")   ------- AGREGAR FAVICON DE PAY
win.geometry("850x700")
win.config(bg="pink")
win.config(padx="20", pady="20")

#-------------------------------------------------- Contenedor con imagen y bienvenida

cont1=Frame(win,width="850")
cont1.pack(anchor=N)
cont1.config(bg="pink")

#-------------------------------------------------- Label con imagen principal

rr=Label(cont1,image=logo,bg="pink")
rr.grid(row=0,column=0,pady="10")

#-------------------------------------------------- Label con bienvenida

bv=Label(cont1,text="¡Le damos la bienvenida a RR Cafe!\nPor favor ingrese los datos de su orden")
bv.config(fg="#973e2c",bg="pink",font=("Arial",14,"bold italic"))
bv.grid(row=1,column=0,pady="10")

#-------------------------------------------------- Contenedores, parte inferior

cont2=Frame(win)
cont2.pack(anchor="w")
cont2.config(bg="pink") #---------------------antes blue

der=Frame(cont2)
der.grid(row=0,column=0,sticky="n",padx=30)
der.config(bg="pink")

dup=Frame(der)
dup.config(bg="pink")
dup.pack()

ddown=Frame(der)
ddown.config(bg="pink")
ddown.pack()

izq=Frame(cont2)
izq.grid(row=0,column=1,sticky="n")
izq.config(bg="pink") #-------------------------antes red

izup=Frame(izq)
izup.config(bg="pink")
izup.pack()

izdn=Frame(izq)
izdn.config(bg="pink")
izdn.pack()

#-------------------------------------------------- Campos de entrada (datos de usuario) - Labels

datlab=Label(dup,text="Sus datos de contacto",bg="pink",fg="#973e2c",font=("Arial",14,"bold"))
datlab.grid(row=0,column=0,padx=5,pady=4,columnspan=2)

namelab=Label(dup,text="                  Su nombre:",bg="pink")
namelab.grid(row=1,column=0,padx=5,pady=2.5,sticky="e")

telab=Label(dup,text="                  Su teléfono:",bg="pink")
telab.grid(row=2,column=0,padx=5,pady=2.5,sticky="e")

emailab=Label(dup,text="                  Su e-mail:",bg="pink")
emailab.grid(row=3,column=0,padx=5,pady=2.5,sticky="e")

ordenlab=Label(dup,text="Su orden",bg="pink",fg="#973e2c",font=("Arial",14,"bold"))
ordenlab.grid(row=4,column=0,padx=5,pady=4,columnspan=2)

#--------------------------------------------------------

pchocolab=Label(ddown,text="Pastel de chocolate ($330):",bg="pink")
pchocolab.grid(row=0,column=0,sticky="e",padx=5,pady=2.5)

pelotelab=Label(ddown,text="Pastel de elote ($280):",bg="pink")
pelotelab.grid(row=1,column=0,sticky="e",padx=5,pady=2.5)

pquesolab=Label(ddown,text="Pay de queso ($240):",bg="pink")
pquesolab.grid(row=2,column=0,sticky="e",padx=5,pady=2.5)

plimonlab=Label(ddown,text="Pay de limón ($220):",bg="pink")
plimonlab.grid(row=3,column=0,sticky="e",padx=5,pady=2.5)

pcalab=Label(ddown,text="Pay de calabaza ($260):",bg="pink")
pcalab.grid(row=4,column=0,sticky="e",padx=5,pady=2.5)

#-------------------------------------------------- Campos de entrada (datos de usuario) - Cuadros

namecuad=Entry(dup)
namecuad.grid(row=1,column=1,sticky="w",padx=5,pady=2.5)

telcuad=Entry(dup)
telcuad.grid(row=2,column=1,sticky="w",padx=5,pady=2.5)

emailcuad=Entry(dup)
emailcuad.grid(row=3,column=1,sticky="w",padx=5,pady=2.5)

#--------------------------------------------------------

pchococuad=Entry(ddown,textvariable=choco,width=5,justify=RIGHT)
pchococuad.grid(row=0,column=1,sticky="w",padx=5,pady=2.5)

pelotecuad=Entry(ddown,textvariable=elote,width=5,justify=RIGHT)
pelotecuad.grid(row=1,column=1,sticky="w",padx=5,pady=2.5)

pquesocuad=Entry(ddown,textvariable=queso,width=5,justify=RIGHT)
pquesocuad.grid(row=2,column=1,sticky="w",padx=5,pady=2.5)

plimoncuad=Entry(ddown,textvariable=limon,width=5,justify=RIGHT)
plimoncuad.grid(row=3,column=1,sticky="w",padx=5,pady=2.5)

pcalcuad=Entry(ddown,textvariable=calab,width=5,justify=RIGHT)
pcalcuad.grid(row=4,column=1,sticky="w",padx=5,pady=2.5)
        
#-------------------------------------------------- Botones (-)

botMenos_choco=Button(ddown,text="-",width=3,command=lambda:[resta1(),result()])
botMenos_choco.grid(row="0",column="2",padx=2.5)

botMenos_elote=Button(ddown,text="-",width=3,command=lambda:[resta2(),result()])
botMenos_elote.grid(row="1",column="2",padx=2.5)

botMenos_queso=Button(ddown,text="-",width=3,command=lambda:[resta3(),result()])
botMenos_queso.grid(row="2",column="2",padx=2.5)

botMenos_limon=Button(ddown,text="-",width=3,command=lambda:[resta4(),result()])
botMenos_limon.grid(row="3",column="2",padx=2.5)

botMenos_calab=Button(ddown,text="-",width=3,command=lambda:[resta5(),result()])
botMenos_calab.grid(row="4",column="2",padx=2.5)

#-------------------------------------------------- Botones (+)

botMas_choco=Button(ddown,text="+",width=3,command=lambda:[suma1(),result()])
botMas_choco.grid(row="0",column="3")

botMas_elote=Button(ddown,text="+",width=3,command=lambda:[suma2(),result()])
botMas_elote.grid(row="1",column="3")

botMas_queso=Button(ddown,text="+",width=3,command=lambda:[suma3(),result()])
botMas_queso.grid(row="2",column="3")

botMas_limon=Button(ddown,text="+",width=3,command=lambda:[suma4(),result()])
botMas_limon.grid(row="3",column="3")

botMas_calab=Button(ddown,text="+",width=3,command=lambda:[suma5(),result()])
botMas_calab.grid(row="4",column="3")

#-------------------------------------------------- Labels cumpleaños y envío

extralab=Label(izup,text="Extras",bg="pink",fg="#973e2c",font=("Arial",14,"bold"))
extralab.grid(row=0,column=0,padx=5,pady=4,columnspan=2)

cumplelab=Label(izup,text="Descuento semana de cumpleaños (5%):\n(Se solicita comprobante)",bg="pink")
cumplelab.grid(row=1,column=0,padx=5,pady=2.5)

envlab=Label(izup,text="Añadir costo de envío ($150):\n(Solo para CDMX)",bg="pink")
envlab.grid(row=2,column=0,padx=5,pady=2.5)

#-------------------------------------------------- Checkbuttons cumpleaños y envío

cumplebut=Checkbutton(izup,variable=desc,command=result,bg="pink")
cumplebut.grid(row=1,column=1,padx=5,pady=2.5,sticky="w")

envbut=Checkbutton(izup,variable=env,command=result,bg="pink")
envbut.grid(row=2,column=1,padx=5,pady=2.5,sticky="w")

#-------------------------------------------------- Labels totales

datlab=Label(izdn,text="Costo:",bg="pink",fg="#973e2c",font=("Arial",14,"bold"))
datlab.grid(row=0,column=0,padx=5,pady=4,columnspan=2)

sublab=Label(izdn,text="Subtotal: $",bg="pink")
sublab.grid(row=1,column=0,padx=5,pady=2.5,sticky="e")

desclab=Label(izdn,text="Con descuento (5%): $",bg="pink")
desclab.grid(row=2,column=0,padx=5,pady=2.5,sticky="e")

ivalab=Label(izdn,text="IVA (16%): $",bg="pink")
ivalab.grid(row=3,column=0,padx=5,pady=2.5,sticky="e")

totalab=Label(izdn,text="Total: $",bg="pink")
totalab.grid(row=4,column=0,padx=5,pady=2.5,sticky="e")

#-------------------------------------------------- Totales - Cuadros

subtotalcuad=Entry(izdn,textvariable=subtotal,width=6)
subtotalcuad.grid(row=1,column=1,sticky="w",padx=5,pady=2.5)

descuad=Entry(izdn,textvariable=descuento,width=6)
descuad.grid(row=2,column=1,sticky="w",padx=5,pady=2.5)

ivacuad=Entry(izdn,textvariable=iva,width=6)
ivacuad.grid(row=3,column=1,sticky="w",padx=5,pady=2.5)

totalcuad=Entry(izdn,textvariable=total,width=6)
totalcuad.grid(row=4,column=1,sticky="w",padx=5,pady=2.5)

#-------------------------------------------------- Botón - "Enviar orden"

botEnviar=Button(izdn,text="Enviar orden",width=13,height=2,fg="#973e2c",font=("Arial",14,"bold"))
botEnviar.grid(row=5,column=0,padx=5,pady=10,columnspan=2)

#-------------------------------------------------- Se ejecuta la ventana raíz

win.mainloop()