from tkinter import Tk, Button, Entry

# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0,0)
root.geometry("290x250")

op_anterior="+"
num_anterior=3.0
pimp=False

def numero1():
    global pimp
    if(pimp):
        pantalla.delete(0,len(pantalla.get()))
        pimp=False
    pantalla.insert(len(pantalla.get()), "1")
def numero2():
    global pimp
    if(pimp):
        pantalla.delete(0,len(pantalla.get()))
        pimp=False
    pantalla.insert(len(pantalla.get()), "2")
def numero3():
    global pimp
    if(pimp):
        pantalla.delete(0,len(pantalla.get()))
        pimp=False
    pantalla.insert(len(pantalla.get()), "3")
def numero4():
    global pimp
    if(pimp):
        pantalla.delete(0,len(pantalla.get()))
        pimp=False
    pantalla.insert(len(pantalla.get()), "4")
def numero5():
    global pimp
    if(pimp):
        pantalla.delete(0,len(pantalla.get()))
        pimp=False
    pantalla.insert(len(pantalla.get()), "5")
def numero6():
    global pimp
    if(pimp):
        pantalla.delete(0,len(pantalla.get()))
        pimp=False
    pantalla.insert(len(pantalla.get()), "6")
def numero7():
    global pimp
    if(pimp):
        pantalla.delete(0,len(pantalla.get()))
        pimp=False
    pantalla.insert(len(pantalla.get()), "7")
def numero8():
    global pimp
    if(pimp):
        pantalla.delete(0,len(pantalla.get()))
        pimp=False
    pantalla.insert(len(pantalla.get()), "8")
def numero9():
    global pimp
    if(pimp):
        pantalla.delete(0,len(pantalla.get()))
        pimp=False
    pantalla.insert(len(pantalla.get()), "9")
def numerop():
    global pimp
    if(pimp):
        pantalla.delete(0,len(pantalla.get()))
        pimp=False
    pantalla.insert(len(pantalla.get()), ".")
def mul():
    global op_anterior
    global num_anterior
    op_anterior="*"
    num_anterior=float(pantalla.get())
    pantalla.delete(0, len(pantalla.get()))
def sum():
    global op_anterior
    global num_anterior
    op_anterior="+"
    num_anterior=float(pantalla.get())
    pantalla.delete(0, len(pantalla.get()))
def res():
    global op_anterior
    global num_anterior
    op_anterior="-"
    num_anterior=float(pantalla.get())
    pantalla.delete(0, len(pantalla.get()))
def div():
    global op_anterior
    global num_anterior
    op_anterior="/"
    num_anterior=float(pantalla.get())
    pantalla.delete(0, len(pantalla.get()))
    
def igual():
    numero=float(pantalla.get())
    if(op_anterior=="+"):
        resultado=numero+num_anterior
    if(op_anterior=="*"):
        resultado=numero*num_anterior
    if(op_anterior=="-"):
        resultado=num_anterior-numero
    if(op_anterior=="/"):
        resultado=num_anterior/numero
    pantalla.delete(0, len(pantalla.get()))
    pantalla.insert(0,str(resultado))
    global pimp
    pimp=True

# Configuración pantalla de salida 
pantalla = Entry(root, width=22, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=4, padx=1, pady=1)

# Configuración botones
boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=numero1).grid(row=1, column=0, padx=1, pady=1)
boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=numero2).grid(row=1, column=1, padx=1, pady=1)
boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=numero3).grid(row=1, column=2, padx=1, pady=1)
boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=numero4).grid(row=2, column=0, padx=1, pady=1)
boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=numero5).grid(row=2, column=1, padx=1, pady=1)
boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=numero6).grid(row=2, column=2, padx=1, pady=1)
boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=numero7).grid(row=3, column=0, padx=1, pady=1)
boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=numero8).grid(row=3, column=1, padx=1, pady=1)
boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=numero9).grid(row=3, column=2, padx=1, pady=1)
boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2", command=igual).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0, command=numerop).grid(row=4, column=2, padx=1, pady=1)
boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=sum).grid(row=1, column=3, padx=1, pady=1)
boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=res).grid(row=2, column=3, padx=1, pady=1)
boton_multiplicacion = Button(root, text="*",  width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=mul).grid(row=3, column=3, padx=1, pady=1)
boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=div).grid(row=4, column=3, padx=1, pady=1)

root.mainloop()