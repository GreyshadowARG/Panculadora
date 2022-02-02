from tkinter import *
import tkinter as tk
import math

#hola

class Panculadora():
    def __init__(self):
        # Definimos variables que albergaran y mostraran los datos
        self.cantidad = StringVar()
        self.sin_semi = StringVar()
        self.resultado = StringVar()
        self.cantidadTotal = StringVar()
        self.res_sinSemi = StringVar()
        self.res_HarinaEsponja = StringVar()
        self.res_agua = StringVar() 
        self.res_levadura = StringVar() 
        self.res_Harina = StringVar()
        self.res_pure_papa = StringVar() 
        self.res_azucar = StringVar() 
        self.res_leche_polvo = StringVar()
        self.res_sal = StringVar()
        self.res_manteca = StringVar()
        self.res_agua_extra = StringVar()
        self.res_anti_moho = StringVar()

    # Variables receta x 1 bolsa
    #esponja
    harina000_esponja = float(83.33333333333334)
    agua = float(83.33333333333334)
    levadura = float(4.166666666666667)

    harina = 125
    pure_papa = float(62.50000000000001)
    azucar = float(12.5)
    leche_polvo = float(12.5)
    sal = float(4.166666666666667)
    manteca = float(20.83333333333338)
    agua_extra = float(16.66666666666667)
    anti_moho = float(0.3125)

    # FUNCION CALCULO RECETA
    def get_cantidadTotal(self):
        self.cantidadTotal.set(str(self.cantidad.get()))

    def get_cantidad_SinSemi(self):
        self.res_sinSemi.set(str(self.sin_semi.get()))

    def get_harinaEsponja(self):
        op_harina_esponja = (float(self.harina000_esponja) * float(self.cantidad.get()))
        self.res_HarinaEsponja.set(math.trunc(op_harina_esponja))

    def get_agua(self):
        op_agua = (self.agua * float(self.cantidad.get()))
        self.res_agua.set(math.trunc(op_agua))

    def get_levadura(self):
        op_levadura = (self.levadura * float(self.cantidad.get()))
        self.res_levadura.set(math.trunc(op_levadura))

    def get_harina(self):
        op_harina = (self.harina * float(self.cantidad.get()))
        self.res_Harina.set(math.trunc(op_harina))

    def get_pure_papa(self):
        op_pure_papa = (self.pure_papa * float(self.cantidad.get()))
        self.res_pure_papa.set(math.trunc(op_pure_papa))

    def get_azucar(self):
        op_azucar = (self.azucar * float(self.cantidad.get()))
        self.res_azucar.set(math.trunc(op_azucar))

    def get_leche_polvo(self):
        op_leche_polvo = (self.leche_polvo * float(self.cantidad.get()))
        self.res_leche_polvo.set(math.trunc(op_leche_polvo))

    def get_sal(self):
        op_sal = (self.sal * float(self.cantidad.get()))
        self.res_sal.set(math.trunc(op_sal))

    def get_manteca(self):
        op_manteca = (self.manteca * float(self.cantidad.get()))
        self.res_manteca.set(math.trunc(op_manteca))

    def get_agua_extra(self):
        op_agua_extra = (self.agua_extra * float(self.cantidad.get()))
        self.res_agua_extra.set(math.trunc(op_agua_extra))

    def get_anti_moho(self):
        op_anti_moho = (self.anti_moho * float(self.cantidad.get()))
        self.res_anti_moho.set(math.trunc(op_anti_moho))

    def ejecutarTodo(self):
        self.get_cantidadTotal()
        self.get_cantidad_SinSemi()
        self.get_harinaEsponja()
        self.get_agua()
        self.get_levadura()
        self.get_harina()
        self.get_pure_papa()
        self.get_azucar()
        self.get_leche_polvo()
        self.get_sal()
        self.get_manteca()
        self.get_agua_extra()
        self.get_anti_moho()

ventana = Tk()
ventana.geometry("362x530")
ventana.config(bg="#1E1E1E")
ventana.title("Panqladora vbeta 0.2")
ventana.iconbitmap('./pancufav.ico')
ventana.resizable(False, False)

panculadora = Panculadora ()

# Frame que contiene el programa
frame = Frame(ventana, width=338, height=500)
frame.config (bg="#1E1E1E")
frame.grid (row=0, column=0, padx=15, pady=15)

# TEXTO ENCABEZADO
encabezado = Label (frame, text="RECETA PARA PAN DE PAPA")
encabezado.config(
    bg="#3C3C3C",
    fg="white",
    font=("Consolas", 10),
    padx=85,
    pady=10,
)
encabezado.grid(row=1, column=0, columnspan=4, sticky=W)

# Label para el campo (cantidad bolsas)
label_cantBolsas = Label(frame, text="¿Cuántas bolsas necesitas?")
label_cantBolsas.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Entry (cantidad bolsas)
campo_cantBolsa = Entry(frame, textvariable=panculadora.cantidad)
campo_cantBolsa.grid(row=2, column=1, sticky= W, padx=5, pady=5)

# Label para el campo (cantidad sin semillas)
label_sin_semi = Label(frame, text="¿Cuántas bolsas NO llevan semillas?")
label_sin_semi.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Entry (cantidad sin semillas)
campo_sin_semi = Entry(frame, textvariable=panculadora.sin_semi)
campo_sin_semi.grid(row=3, column=1, sticky= W, padx=5, pady=5)

# Boton
boton = Button(frame, text="Calcular receta", command=panculadora.ejecutarTodo)
boton.grid(row=5, column=1)
boton.config(padx=3, pady=4, bg="#913B24", fg="white")

espacio = Label(frame, text="")
espacio.config (bg="#1E1E1E", font=("Consolas", 4))
espacio.grid(row=6, column=0, sticky=W)

# RESULTADO
label_titulo = Label(frame, text="### RECETA PAN DE PAPA ###")
label_titulo.config (bg="#1E1E1E", fg="white", font=("Consolas", 10))
label_titulo.grid(row=7, column=0, sticky=W)

label_cantidades = Label(frame, text="Cantidad de bolsas: ")
label_cantidades.config (bg="#1E1E1E", fg="white", font=("Consolas", 10))
label_cantidades.grid(row=8, column=0, sticky=W)

resultado_cantidades = Label(frame, textvariable=panculadora.cantidadTotal)
resultado_cantidades.config (bg="#1E1E1E", fg="white", font=("Consolas", 10))
resultado_cantidades.grid(row=8, column=1, sticky=W)

label_cantidades_sinSemi = Label(frame, text="Cantidad sin semillas: ")
label_cantidades_sinSemi.config (bg="#1E1E1E", fg="white", font=("Consolas", 10))
label_cantidades_sinSemi.grid(row=9, column=0, sticky=W)

resultado_cantidades_sinSemi = Label(frame, textvariable=panculadora.res_sinSemi)
resultado_cantidades_sinSemi.config (bg="#1E1E1E", fg="white", font=("Consolas", 10))
resultado_cantidades_sinSemi.grid(row=9, column=1, sticky=W)

espacio = Label(frame, text="")
espacio.config (bg="#1E1E1E", font=("Consolas", 4))
espacio.grid(row=10, column=0, sticky=W)

label_esponja = Label(frame, text="# ESPONJA #")
label_esponja.config (bg="#1E1E1E", fg="white", font=("Consolas", 10))
label_esponja.grid(row=11, column=0, sticky=W)

resultadoReceta = Label(frame, text="Harina 000: ")
resultadoReceta.config (bg="#1E1E1E", fg="white", font=("Consolas", 8))
resultadoReceta.grid(row=12, column=0, sticky=W)

harina_num = Label(frame, textvariable=panculadora.res_HarinaEsponja)
harina_num.config (bg="#1E1E1E", fg="white", font=("Consolas", 10))
harina_num.grid(row=12, column=1, sticky=W)

label_agua = Label(frame, text="Agua: ")
label_agua.config (bg="#1E1E1E", fg="white", font=("Consolas", 8))
label_agua.grid(row=13, column=0, sticky=W)

agua_num = Label(frame, textvariable=panculadora.res_agua)
agua_num.config (bg="#1E1E1E", fg="white", font=("Consolas", 10))
agua_num.grid(row=13, column=1, sticky=W)

label_levadura = Label(frame, text="Levadura: ")
label_levadura.config (bg="#1E1E1E", fg="white", font=("Consolas", 8))
label_levadura.grid(row=14, column=0, sticky=W)

levadura_num = Label(frame, textvariable=panculadora.res_levadura)
levadura_num.config (bg="#1E1E1E", fg="white", font=("Consolas", 10))
levadura_num.grid(row=14, column=1, sticky=W)

espacio = Label(frame, text="")
espacio.config (bg="#1E1E1E", font=("Consolas", 4))
espacio.grid(row=15, column=0, sticky=W)

label_harina000 = Label(frame, text="Harina: ")
label_harina000.config (bg="#1E1E1E", fg="white", font=("Consolas", 8))
label_harina000.grid(row=16, column=0, sticky=W)

harina000_num = Label(frame, textvariable=panculadora.res_Harina)
harina000_num.config (bg="#1E1E1E", fg="white", font=("Consolas", 10))
harina000_num.grid(row=16, column=1, sticky=W)

label_pure_papa = Label(frame, text="Pure de papa: ")
label_pure_papa.config (bg="#1E1E1E", fg="white", font=("Consolas", 8))
label_pure_papa.grid(row=17, column=0, sticky=W)

pure_papa_num = Label(frame, textvariable=panculadora.res_pure_papa)
pure_papa_num.config (bg="#1E1E1E", fg="white", font=("Consolas", 10))
pure_papa_num.grid(row=17, column=1, sticky=W)

label_azucar = Label(frame, text="Azucar: ")
label_azucar.config (bg="#1E1E1E", fg="white", font=("Consolas", 8))
label_azucar.grid(row=18, column=0, sticky=W)

azucar_num = Label(frame, textvariable=panculadora.res_azucar)
azucar_num.config (bg="#1E1E1E", fg="white", font=("Consolas", 10))
azucar_num.grid(row=18, column=1, sticky=W)

label_leche_polvo = Label(frame, text="Leche en polvo: ")
label_leche_polvo.config (bg="#1E1E1E", fg="white", font=("Consolas", 8))
label_leche_polvo.grid(row=19, column=0, sticky=W)

leche_polvo_num = Label(frame, textvariable=panculadora.res_leche_polvo)
leche_polvo_num.config (bg="#1E1E1E", fg="white", font=("Consolas", 10))
leche_polvo_num.grid(row=19, column=1, sticky=W)
    
label_sal = Label(frame, text="Sal: ")
label_sal.config (bg="#1E1E1E", fg="white", font=("Consolas", 8))
label_sal.grid(row=20, column=0, sticky=W)

sal_num = Label(frame, textvariable=panculadora.res_sal)
sal_num.config (bg="#1E1E1E", fg="white", font=("Consolas", 10))
sal_num.grid(row=20, column=1, sticky=W)

label_manteca = Label(frame, text="Manteca: ")
label_manteca.config (bg="#1E1E1E", fg="white", font=("Consolas", 8))
label_manteca.grid(row=21, column=0, sticky=W)

manteca_num = Label(frame, textvariable=panculadora.res_manteca)
manteca_num.config (bg="#1E1E1E", fg="white", font=("Consolas", 10))
manteca_num.grid(row=21, column=1, sticky=W)

espacio = Label(frame, text="")
espacio.config (bg="#1E1E1E", font=("Consolas", 4))
espacio.grid(row=22, column=0, sticky=W)

label_agua_extra = Label(frame, text="Agua Extra: ")
label_agua_extra.config (bg="#1E1E1E", fg="white", font=("Consolas", 8))
label_agua_extra.grid(row=23, column=0, sticky=W)

agua_extra_num = Label(frame, textvariable=panculadora.res_agua_extra)
agua_extra_num.config (bg="#1E1E1E", fg="white", font=("Consolas", 10))
agua_extra_num.grid(row=23, column=1, sticky=W)

label_anti_moho = Label(frame, text="Anti moho: ")
label_anti_moho.config (bg="#1E1E1E", fg="white", font=("Consolas", 8))
label_anti_moho.grid(row=24, column=0, sticky=W)

anti_moho_num = Label(frame, textvariable=panculadora.res_anti_moho)
anti_moho_num.config (bg="#1E1E1E", fg="white", font=("Consolas", 10))
anti_moho_num.grid(row=24, column=1, sticky=W)

ventana.mainloop()