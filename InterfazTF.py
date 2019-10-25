# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 17:00:57 2019

@author: Intel
"""

import tkinter as tk

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


pos = 0

def lecturaArchivo():
       print("a")

def generar():         
    if int(f_cantidad.get()) == 1:
        
        #----1
        datos_caja = tk.Label(ventana, text="Datos del la Caja", bg = "steel blue", fg="black")
        datos_caja.place(x=10, y=240)
        datos_caja.config(font = ("Verdana", 10))
        
        cantidad_caja = tk.Label(ventana, text="Cantidad: ", bg = "steel blue", fg="black")
        cantidad_caja.place(x=10, y=270)
        cantidad_caja.config(font = ("Verdana", 7))
        
        c_caja=tk.Entry(ventana, width=4)
        c_caja.place(x=70, y=270)
        
        nombre_caja = tk.Label(ventana, text="Nombre: ", bg = "steel blue", fg="black")
        nombre_caja.place(x=130, y=270)
        nombre_caja.config(font = ("Verdana", 7))
        
        n_caja=tk.Entry(ventana, width=4)
        n_caja.place(x=190, y=270)
        
        ancho_caja = tk.Label(ventana, text="Anc: ", bg = "steel blue", fg="black")
        ancho_caja.place(x=250, y=270)
        ancho_caja.config(font = ("Verdana", 7))
        
        anc_caja=tk.Entry(ventana, width=4)
        anc_caja.place(x=280, y=270)
        
        alto_caja = tk.Label(ventana, text="Alt: ", bg = "steel blue", fg="black")
        alto_caja.place(x=320, y=270)
        alto_caja.config(font = ("Verdana", 7))
        
        alt_caja=tk.Entry(ventana, width=4)
        alt_caja.place(x=350, y=270)
        
        largo_caja = tk.Label(ventana, text="Lar: ", bg = "steel blue", fg="black")
        largo_caja.place(x=390, y=270)
        largo_caja.config(font = ("Verdana", 7))
        
        lar_caja=tk.Entry(ventana, width=4)
        lar_caja.place(x=420, y=270)
        
    elif int(f_cantidad.get()) == 2:
        #----1
        datos_caja = tk.Label(ventana, text="Datos del la Caja", bg = "steel blue", fg="black")
        datos_caja.place(x=10, y=240)
        datos_caja.config(font = ("Verdana", 10))
        
        cantidad_caja = tk.Label(ventana, text="Cantidad: ", bg = "steel blue", fg="black")
        cantidad_caja.place(x=10, y=270)
        cantidad_caja.config(font = ("Verdana", 7))
        
        c_caja=tk.Entry(ventana, width=4)
        c_caja.place(x=70, y=270)
        
        nombre_caja = tk.Label(ventana, text="Nombre: ", bg = "steel blue", fg="black")
        nombre_caja.place(x=130, y=270)
        nombre_caja.config(font = ("Verdana", 7))
        
        n_caja=tk.Entry(ventana, width=4)
        n_caja.place(x=190, y=270)
        
        ancho_caja = tk.Label(ventana, text="Anc: ", bg = "steel blue", fg="black")
        ancho_caja.place(x=250, y=270)
        ancho_caja.config(font = ("Verdana", 7))
        
        anc_caja=tk.Entry(ventana, width=4)
        anc_caja.place(x=280, y=270)
        
        alto_caja = tk.Label(ventana, text="Alt: ", bg = "steel blue", fg="black")
        alto_caja.place(x=320, y=270)
        alto_caja.config(font = ("Verdana", 7))
        
        alt_caja=tk.Entry(ventana, width=4)
        alt_caja.place(x=350, y=270)
        
        largo_caja = tk.Label(ventana, text="Lar: ", bg = "steel blue", fg="black")
        largo_caja.place(x=390, y=270)
        largo_caja.config(font = ("Verdana", 7))
        
        lar_caja=tk.Entry(ventana, width=4)
        lar_caja.place(x=420, y=270)
        
        
        #----2
        
        cantidad_caja2 = tk.Label(ventana, text="Cantidad: ", bg = "steel blue", fg="black")
        cantidad_caja2.place(x=10, y=300)
        cantidad_caja2.config(font = ("Verdana", 7))
        
        c_caja2=tk.Entry(ventana, width=4)
        c_caja2.place(x=70, y=300)
        
        nombre_caja2 = tk.Label(ventana, text="Nombre: ", bg = "steel blue", fg="black")
        nombre_caja2.place(x=130, y=300)
        nombre_caja2.config(font = ("Verdana", 7))
        
        n_caja2=tk.Entry(ventana, width=4)
        n_caja2.place(x=190, y=300)
        
        ancho_caja2 = tk.Label(ventana, text="Anc: ", bg = "steel blue", fg="black")
        ancho_caja2.place(x=250, y=300)
        ancho_caja2.config(font = ("Verdana", 7))
        
        anc_caja2=tk.Entry(ventana, width=4)
        anc_caja2.place(x=280, y=300)
        
        alto_caja2 = tk.Label(ventana, text="Alt: ", bg = "steel blue", fg="black")
        alto_caja2.place(x=320, y=300)
        alto_caja2.config(font = ("Verdana", 7))
        
        alt_caja2=tk.Entry(ventana, width=4)
        alt_caja2.place(x=350, y=300)
        
        largo_caja2 = tk.Label(ventana, text="Lar: ", bg = "steel blue", fg="black")
        largo_caja2.place(x=390, y=300)
        largo_caja2.config(font = ("Verdana", 7))
        
        lar_caja2=tk.Entry(ventana, width=4)
        lar_caja2.place(x=420, y=300)

    elif int(f_cantidad.get()) == 3:
        #----1
        datos_caja = tk.Label(ventana, text="Datos del la Caja", bg = "steel blue", fg="black")
        datos_caja.place(x=10, y=240)
        datos_caja.config(font = ("Verdana", 10))
        
        cantidad_caja = tk.Label(ventana, text="Cantidad: ", bg = "steel blue", fg="black")
        cantidad_caja.place(x=10, y=270)
        cantidad_caja.config(font = ("Verdana", 7))
        
        c_caja=tk.Entry(ventana, width=4)
        c_caja.place(x=70, y=270)
        
        nombre_caja = tk.Label(ventana, text="Nombre: ", bg = "steel blue", fg="black")
        nombre_caja.place(x=130, y=270)
        nombre_caja.config(font = ("Verdana", 7))
        
        n_caja=tk.Entry(ventana, width=4)
        n_caja.place(x=190, y=270)
        
        ancho_caja = tk.Label(ventana, text="Anc: ", bg = "steel blue", fg="black")
        ancho_caja.place(x=250, y=270)
        ancho_caja.config(font = ("Verdana", 7))
        
        anc_caja=tk.Entry(ventana, width=4)
        anc_caja.place(x=280, y=270)
        
        alto_caja = tk.Label(ventana, text="Alt: ", bg = "steel blue", fg="black")
        alto_caja.place(x=320, y=270)
        alto_caja.config(font = ("Verdana", 7))
        
        alt_caja=tk.Entry(ventana, width=4)
        alt_caja.place(x=350, y=270)
        
        largo_caja = tk.Label(ventana, text="Lar: ", bg = "steel blue", fg="black")
        largo_caja.place(x=390, y=270)
        largo_caja.config(font = ("Verdana", 7))
        
        lar_caja=tk.Entry(ventana, width=4)
        lar_caja.place(x=420, y=270)
        
        
        #----2
        
        cantidad_caja2 = tk.Label(ventana, text="Cantidad: ", bg = "steel blue", fg="black")
        cantidad_caja2.place(x=10, y=300)
        cantidad_caja2.config(font = ("Verdana", 7))
        
        c_caja2=tk.Entry(ventana, width=4)
        c_caja2.place(x=70, y=300)
        
        nombre_caja2 = tk.Label(ventana, text="Nombre: ", bg = "steel blue", fg="black")
        nombre_caja2.place(x=130, y=300)
        nombre_caja2.config(font = ("Verdana", 7))
        
        n_caja2=tk.Entry(ventana, width=4)
        n_caja2.place(x=190, y=300)
        
        ancho_caja2 = tk.Label(ventana, text="Anc: ", bg = "steel blue", fg="black")
        ancho_caja2.place(x=250, y=300)
        ancho_caja2.config(font = ("Verdana", 7))
        
        anc_caja2=tk.Entry(ventana, width=4)
        anc_caja2.place(x=280, y=300)
        
        alto_caja2 = tk.Label(ventana, text="Alt: ", bg = "steel blue", fg="black")
        alto_caja2.place(x=320, y=300)
        alto_caja2.config(font = ("Verdana", 7))
        
        alt_caja2=tk.Entry(ventana, width=4)
        alt_caja2.place(x=350, y=300)
        
        largo_caja2 = tk.Label(ventana, text="Lar: ", bg = "steel blue", fg="black")
        largo_caja2.place(x=390, y=300)
        largo_caja2.config(font = ("Verdana", 7))
        
        lar_caja2=tk.Entry(ventana, width=4)
        lar_caja2.place(x=420, y=300)
        
        
        #----3
        
        cantidad_caja3 = tk.Label(ventana, text="Cantidad: ", bg = "steel blue", fg="black")
        cantidad_caja3.place(x=10, y=330)
        cantidad_caja3.config(font = ("Verdana", 7))
        
        c_caja3=tk.Entry(ventana, width=4)
        c_caja3.place(x=70, y=330)
        
        nombre_caja3 = tk.Label(ventana, text="Nombre: ", bg = "steel blue", fg="black")
        nombre_caja3.place(x=130, y=330)
        nombre_caja3.config(font = ("Verdana", 7))
        
        n_caja3=tk.Entry(ventana, width=4)
        n_caja3.place(x=190, y=330)
        
        ancho_caja3 = tk.Label(ventana, text="Anc: ", bg = "steel blue", fg="black")
        ancho_caja3.place(x=250, y=330)
        ancho_caja3.config(font = ("Verdana", 7))
        
        anc_caja3=tk.Entry(ventana, width=4)
        anc_caja3.place(x=280, y=330)
        
        alto_caja3 = tk.Label(ventana, text="Alt: ", bg = "steel blue", fg="black")
        alto_caja3.place(x=320, y=330)
        alto_caja3.config(font = ("Verdana", 7))
        
        alt_caja3=tk.Entry(ventana, width=4)
        alt_caja3.place(x=350, y=330)
        
        largo_caja3 = tk.Label(ventana, text="Lar: ", bg = "steel blue", fg="black")
        largo_caja3.place(x=390, y=330)
        largo_caja3.config(font = ("Verdana", 7))
        
        lar_caja3=tk.Entry(ventana, width=4)
        lar_caja3.place(x=420, y=330)
        
    elif int(f_cantidad.get()) == 4:
        #----1
        datos_caja = tk.Label(ventana, text="Datos del la Caja", bg = "steel blue", fg="black")
        datos_caja.place(x=10, y=240)
        datos_caja.config(font = ("Verdana", 10))
        
        cantidad_caja = tk.Label(ventana, text="Cantidad: ", bg = "steel blue", fg="black")
        cantidad_caja.place(x=10, y=270)
        cantidad_caja.config(font = ("Verdana", 7))
        
        c_caja=tk.Entry(ventana, width=4)
        c_caja.place(x=70, y=270)
        
        nombre_caja = tk.Label(ventana, text="Nombre: ", bg = "steel blue", fg="black")
        nombre_caja.place(x=130, y=270)
        nombre_caja.config(font = ("Verdana", 7))
        
        n_caja=tk.Entry(ventana, width=4)
        n_caja.place(x=190, y=270)
        
        ancho_caja = tk.Label(ventana, text="Anc: ", bg = "steel blue", fg="black")
        ancho_caja.place(x=250, y=270)
        ancho_caja.config(font = ("Verdana", 7))
        
        anc_caja=tk.Entry(ventana, width=4)
        anc_caja.place(x=280, y=270)
        
        alto_caja = tk.Label(ventana, text="Alt: ", bg = "steel blue", fg="black")
        alto_caja.place(x=320, y=270)
        alto_caja.config(font = ("Verdana", 7))
        
        alt_caja=tk.Entry(ventana, width=4)
        alt_caja.place(x=350, y=270)
        
        largo_caja = tk.Label(ventana, text="Lar: ", bg = "steel blue", fg="black")
        largo_caja.place(x=390, y=270)
        largo_caja.config(font = ("Verdana", 7))
        
        lar_caja=tk.Entry(ventana, width=4)
        lar_caja.place(x=420, y=270)
        
        
        #----2
        
        cantidad_caja2 = tk.Label(ventana, text="Cantidad: ", bg = "steel blue", fg="black")
        cantidad_caja2.place(x=10, y=300)
        cantidad_caja2.config(font = ("Verdana", 7))
        
        c_caja2=tk.Entry(ventana, width=4)
        c_caja2.place(x=70, y=300)
        
        nombre_caja2 = tk.Label(ventana, text="Nombre: ", bg = "steel blue", fg="black")
        nombre_caja2.place(x=130, y=300)
        nombre_caja2.config(font = ("Verdana", 7))
        
        n_caja2=tk.Entry(ventana, width=4)
        n_caja2.place(x=190, y=300)
        
        ancho_caja2 = tk.Label(ventana, text="Anc: ", bg = "steel blue", fg="black")
        ancho_caja2.place(x=250, y=300)
        ancho_caja2.config(font = ("Verdana", 7))
        
        anc_caja2=tk.Entry(ventana, width=4)
        anc_caja2.place(x=280, y=300)
        
        alto_caja2 = tk.Label(ventana, text="Alt: ", bg = "steel blue", fg="black")
        alto_caja2.place(x=320, y=300)
        alto_caja2.config(font = ("Verdana", 7))
        
        alt_caja2=tk.Entry(ventana, width=4)
        alt_caja2.place(x=350, y=300)
        
        largo_caja2 = tk.Label(ventana, text="Lar: ", bg = "steel blue", fg="black")
        largo_caja2.place(x=390, y=300)
        largo_caja2.config(font = ("Verdana", 7))
        
        lar_caja2=tk.Entry(ventana, width=4)
        lar_caja2.place(x=420, y=300)
        
        
        #----3
        
        cantidad_caja3 = tk.Label(ventana, text="Cantidad: ", bg = "steel blue", fg="black")
        cantidad_caja3.place(x=10, y=330)
        cantidad_caja3.config(font = ("Verdana", 7))
        
        c_caja3=tk.Entry(ventana, width=4)
        c_caja3.place(x=70, y=330)
        
        nombre_caja3 = tk.Label(ventana, text="Nombre: ", bg = "steel blue", fg="black")
        nombre_caja3.place(x=130, y=330)
        nombre_caja3.config(font = ("Verdana", 7))
        
        n_caja3=tk.Entry(ventana, width=4)
        n_caja3.place(x=190, y=330)
        
        ancho_caja3 = tk.Label(ventana, text="Anc: ", bg = "steel blue", fg="black")
        ancho_caja3.place(x=250, y=330)
        ancho_caja3.config(font = ("Verdana", 7))
        
        anc_caja3=tk.Entry(ventana, width=4)
        anc_caja3.place(x=280, y=330)
        
        alto_caja3 = tk.Label(ventana, text="Alt: ", bg = "steel blue", fg="black")
        alto_caja3.place(x=320, y=330)
        alto_caja3.config(font = ("Verdana", 7))
        
        alt_caja3=tk.Entry(ventana, width=4)
        alt_caja3.place(x=350, y=330)
        
        largo_caja3 = tk.Label(ventana, text="Lar: ", bg = "steel blue", fg="black")
        largo_caja3.place(x=390, y=330)
        largo_caja3.config(font = ("Verdana", 7))
        
        lar_caja3=tk.Entry(ventana, width=4)
        lar_caja3.place(x=420, y=330)
        
        #----4
        
        cantidad_caja4 = tk.Label(ventana, text="Cantidad: ", bg = "steel blue", fg="black")
        cantidad_caja4.place(x=10, y=360)
        cantidad_caja4.config(font = ("Verdana", 7))
        
        c_caja4=tk.Entry(ventana, width=4)
        c_caja4.place(x=70, y=360)
        
        nombre_caja4 = tk.Label(ventana, text="Nombre: ", bg = "steel blue", fg="black")
        nombre_caja4.place(x=130, y=360)
        nombre_caja4.config(font = ("Verdana", 7))
        
        n_caja4=tk.Entry(ventana, width=4)
        n_caja4.place(x=190, y=360)
        
        ancho_caja4 = tk.Label(ventana, text="Anc: ", bg = "steel blue", fg="black")
        ancho_caja4.place(x=250, y=360)
        ancho_caja4.config(font = ("Verdana", 7))
        
        anc_caja4=tk.Entry(ventana, width=4)
        anc_caja4.place(x=280, y=360)
        
        alto_caja4 = tk.Label(ventana, text="Alt: ", bg = "steel blue", fg="black")
        alto_caja4.place(x=320, y=360)
        alto_caja4.config(font = ("Verdana", 7))
        
        alt_caja4=tk.Entry(ventana, width=4)
        alt_caja4.place(x=350, y=360)
        
        largo_caja4 = tk.Label(ventana, text="Lar: ", bg = "steel blue", fg="black")
        largo_caja4.place(x=390, y=360)
        largo_caja4.config(font = ("Verdana", 7))
        
        lar_caja4=tk.Entry(ventana, width=4)
        lar_caja4.place(x=420, y=360)
        
    elif int(f_cantidad.get()) == 5:
        #----1
        datos_caja = tk.Label(ventana, text="Datos del la Caja", bg = "steel blue", fg="black")
        datos_caja.place(x=10, y=240)
        datos_caja.config(font = ("Verdana", 10))
        
        cantidad_caja = tk.Label(ventana, text="Cantidad: ", bg = "steel blue", fg="black")
        cantidad_caja.place(x=10, y=270)
        cantidad_caja.config(font = ("Verdana", 7))
        
        c_caja=tk.Entry(ventana, width=4)
        c_caja.place(x=70, y=270)
        
        nombre_caja = tk.Label(ventana, text="Nombre: ", bg = "steel blue", fg="black")
        nombre_caja.place(x=130, y=270)
        nombre_caja.config(font = ("Verdana", 7))
        
        n_caja=tk.Entry(ventana, width=4)
        n_caja.place(x=190, y=270)
        
        ancho_caja = tk.Label(ventana, text="Anc: ", bg = "steel blue", fg="black")
        ancho_caja.place(x=250, y=270)
        ancho_caja.config(font = ("Verdana", 7))
        
        anc_caja=tk.Entry(ventana, width=4)
        anc_caja.place(x=280, y=270)
        
        alto_caja = tk.Label(ventana, text="Alt: ", bg = "steel blue", fg="black")
        alto_caja.place(x=320, y=270)
        alto_caja.config(font = ("Verdana", 7))
        
        alt_caja=tk.Entry(ventana, width=4)
        alt_caja.place(x=350, y=270)
        
        largo_caja = tk.Label(ventana, text="Lar: ", bg = "steel blue", fg="black")
        largo_caja.place(x=390, y=270)
        largo_caja.config(font = ("Verdana", 7))
        
        lar_caja=tk.Entry(ventana, width=4)
        lar_caja.place(x=420, y=270)
        
        
        #----2
        
        cantidad_caja2 = tk.Label(ventana, text="Cantidad: ", bg = "steel blue", fg="black")
        cantidad_caja2.place(x=10, y=300)
        cantidad_caja2.config(font = ("Verdana", 7))
        
        c_caja2=tk.Entry(ventana, width=4)
        c_caja2.place(x=70, y=300)
        
        nombre_caja2 = tk.Label(ventana, text="Nombre: ", bg = "steel blue", fg="black")
        nombre_caja2.place(x=130, y=300)
        nombre_caja2.config(font = ("Verdana", 7))
        
        n_caja2=tk.Entry(ventana, width=4)
        n_caja2.place(x=190, y=300)
        
        ancho_caja2 = tk.Label(ventana, text="Anc: ", bg = "steel blue", fg="black")
        ancho_caja2.place(x=250, y=300)
        ancho_caja2.config(font = ("Verdana", 7))
        
        anc_caja2=tk.Entry(ventana, width=4)
        anc_caja2.place(x=280, y=300)
        
        alto_caja2 = tk.Label(ventana, text="Alt: ", bg = "steel blue", fg="black")
        alto_caja2.place(x=320, y=300)
        alto_caja2.config(font = ("Verdana", 7))
        
        alt_caja2=tk.Entry(ventana, width=4)
        alt_caja2.place(x=350, y=300)
        
        largo_caja2 = tk.Label(ventana, text="Lar: ", bg = "steel blue", fg="black")
        largo_caja2.place(x=390, y=300)
        largo_caja2.config(font = ("Verdana", 7))
        
        lar_caja2=tk.Entry(ventana, width=4)
        lar_caja2.place(x=420, y=300)
        
        
        #----3
        
        cantidad_caja3 = tk.Label(ventana, text="Cantidad: ", bg = "steel blue", fg="black")
        cantidad_caja3.place(x=10, y=330)
        cantidad_caja3.config(font = ("Verdana", 7))
        
        c_caja3=tk.Entry(ventana, width=4)
        c_caja3.place(x=70, y=330)
        
        nombre_caja3 = tk.Label(ventana, text="Nombre: ", bg = "steel blue", fg="black")
        nombre_caja3.place(x=130, y=330)
        nombre_caja3.config(font = ("Verdana", 7))
        
        n_caja3=tk.Entry(ventana, width=4)
        n_caja3.place(x=190, y=330)
        
        ancho_caja3 = tk.Label(ventana, text="Anc: ", bg = "steel blue", fg="black")
        ancho_caja3.place(x=250, y=330)
        ancho_caja3.config(font = ("Verdana", 7))
        
        anc_caja3=tk.Entry(ventana, width=4)
        anc_caja3.place(x=280, y=330)
        
        alto_caja3 = tk.Label(ventana, text="Alt: ", bg = "steel blue", fg="black")
        alto_caja3.place(x=320, y=330)
        alto_caja3.config(font = ("Verdana", 7))
        
        alt_caja3=tk.Entry(ventana, width=4)
        alt_caja3.place(x=350, y=330)
        
        largo_caja3 = tk.Label(ventana, text="Lar: ", bg = "steel blue", fg="black")
        largo_caja3.place(x=390, y=330)
        largo_caja3.config(font = ("Verdana", 7))
        
        lar_caja3=tk.Entry(ventana, width=4)
        lar_caja3.place(x=420, y=330)
        
        #----4
        
        cantidad_caja4 = tk.Label(ventana, text="Cantidad: ", bg = "steel blue", fg="black")
        cantidad_caja4.place(x=10, y=360)
        cantidad_caja4.config(font = ("Verdana", 7))
        
        c_caja4=tk.Entry(ventana, width=4)
        c_caja4.place(x=70, y=360)
        
        nombre_caja4 = tk.Label(ventana, text="Nombre: ", bg = "steel blue", fg="black")
        nombre_caja4.place(x=130, y=360)
        nombre_caja4.config(font = ("Verdana", 7))
        
        n_caja4=tk.Entry(ventana, width=4)
        n_caja4.place(x=190, y=360)
        
        ancho_caja4 = tk.Label(ventana, text="Anc: ", bg = "steel blue", fg="black")
        ancho_caja4.place(x=250, y=360)
        ancho_caja4.config(font = ("Verdana", 7))
        
        anc_caja4=tk.Entry(ventana, width=4)
        anc_caja4.place(x=280, y=360)
        
        alto_caja4 = tk.Label(ventana, text="Alt: ", bg = "steel blue", fg="black")
        alto_caja4.place(x=320, y=360)
        alto_caja4.config(font = ("Verdana", 7))
        
        alt_caja4=tk.Entry(ventana, width=4)
        alt_caja4.place(x=350, y=360)
        
        largo_caja4 = tk.Label(ventana, text="Lar: ", bg = "steel blue", fg="black")
        largo_caja4.place(x=390, y=360)
        largo_caja4.config(font = ("Verdana", 7))
        
        lar_caja4=tk.Entry(ventana, width=4)
        lar_caja4.place(x=420, y=360)
        
        #----5
        
        cantidad_caja5 = tk.Label(ventana, text="Cantidad: ", bg = "steel blue", fg="black")
        cantidad_caja5.place(x=10, y=390)
        cantidad_caja5.config(font = ("Verdana", 7))
        
        c_caja5=tk.Entry(ventana, width=4)
        c_caja5.place(x=70, y=390)
        
        nombre_caja5 = tk.Label(ventana, text="Nombre: ", bg = "steel blue", fg="black")
        nombre_caja5.place(x=130, y=390)
        nombre_caja5.config(font = ("Verdana", 7))
        
        n_caja4=tk.Entry(ventana, width=4)
        n_caja4.place(x=190, y=390)
        
        ancho_caja5 = tk.Label(ventana, text="Anc: ", bg = "steel blue", fg="black")
        ancho_caja5.place(x=250, y=390)
        ancho_caja5.config(font = ("Verdana", 7))
        
        anc_caja5=tk.Entry(ventana, width=4)
        anc_caja5.place(x=280, y=390)
        
        alto_caja5 = tk.Label(ventana, text="Alt: ", bg = "steel blue", fg="black")
        alto_caja5.place(x=320, y=390)
        alto_caja5.config(font = ("Verdana", 7))
        
        alt_caja5=tk.Entry(ventana, width=4)
        alt_caja5.place(x=350, y=390)
        
        largo_caja5 = tk.Label(ventana, text="Lar: ", bg = "steel blue", fg="black")
        largo_caja5.place(x=390, y=390)
        largo_caja5.config(font = ("Verdana", 7))
        
        lar_caja5=tk.Entry(ventana, width=4)
        lar_caja5.place(x=420, y=390)
        

def algoritmo1():
    
    class Cubo:
        def __init__(self, x, y, z, ancho, alto, largo):
            self.x = x
            self.y = y
            self.z = z
            self.ancho = ancho
            self.alto = alto
            self.largo = largo
    
    plt.rcParams['toolbar'] = 'None'
    
    x, y, z = np.indices((int(c_largo.get()), int(c_ancho.get()), int(c_alto.get())))
    
    cube1 = (x >= 0) & (x < 2) & (y >= 0) & (y < 1) & (z >= 0) & (z < 5)
    cube2 = (x >= 0) & (x < 2) & (y >= 1) & (y < 1+1) & (z >= 0) & (z < 3)
    cube3 = (x >= 0) & (x < 2) & (y >= 0) & (y < 1) & (z >= 0) & (z < 3)
    cube4 = (x >= 0) & (x < 2) & (y >= 1) & (y < 1+1) & (z >= 0) & (z < 3)
    cube5 = (x >= 2) & (x < 2+1) & (y >= 0) & (y < 1) & (z >= 0) & (z < 2)
    cube6 = (x >= 2) & (x < 2+1) & (y >= 1) & (y < 1+1) & (z >= 0) & (z < 2)
    
    voxels = cube1 | cube2
    voxels2 = cube3 | cube4 | cube5 | cube6
    voxels3 = cube3 | cube4 | cube5 | cube6
    
    
    colors = np.empty(voxels.shape, dtype=object)
    colors2 = np.empty(voxels2.shape, dtype=object)
    
    colors[cube1] = 'blue'
    colors[cube2] = 'green'
    colors2[cube3] = 'yellow'
    colors2[cube4] = 'red'
    colors2[cube5] = 'black'
    colors2[cube6] = 'brown'
    
    
    global pos
    
    def right(event):
        
        global pos
    
        event.canvas.figure.clear()
        
        ax = fig.gca(projection='3d')
        figuras = [voxels, voxels2, voxels3]
        
        if pos == len(figuras) - 1:
            pos = -1
        
        if pos < len(figuras) - 1:
            pos = pos + 1
            
        if pos == 0:
            ax.voxels(figuras[pos], facecolors=colors, edgecolor='k')
        else:
            ax.voxels(figuras[pos], facecolors=colors2, edgecolor='k')
    
        event.canvas.draw()
    
    
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    figuras = [voxels, voxels2, voxels3]
    ax.voxels(figuras[pos], facecolors=colors, edgecolor='k')
    fig.canvas.mpl_connect('key_press_event', right)
    plt.show()





"""
def suma():
    suma=int(entrada.get())+int(entrada.get())
    return var.set(suma)
"""

ventana = tk.Tk()

ventana.title("ALGORITMOS DE EMPAQUETAMIENTO 3D")

ventana.geometry('500x500')

ventana.configure(background='steel blue')

titulo = tk.Label(ventana, text="ALGORITMOS DE EMPAQUETAMIENTO 3D", bg = "steel blue", fg="black")
titulo.pack(fill=tk.X, padx=20, pady=20)
titulo.config(font = ("Verdana", 12))



#-------------- SALIDA DE DATOS -----------------------
var = tk.StringVar()

#res = tk.Label(ventana, bg="plum", textvariable=var, padx=5, pady=5, width=50)
#res.pack()

#------------------------------------------------------


#--------------- ENTRADAA DE DATOS -------------------


contenedor = tk.Label(ventana, text="Datos del Contenedor", bg = "steel blue", fg="black")
contenedor.place(x=10, y=60)
contenedor.config(font = ("Verdana", 10))

contenedor_ancho = tk.Label(ventana, text="Ancho", bg = "steel blue", fg="black")
contenedor_ancho.place(x=10, y=90)
contenedor_ancho.config(font = ("Verdana", 7))

c_ancho=tk.Entry(ventana)
c_ancho.place(x=50, y=90)

contenedor_alto = tk.Label(ventana, text="Alto", bg = "steel blue", fg="black")
contenedor_alto.place(x=10, y=120)
contenedor_alto.config(font = ("Verdana", 7))

c_alto=tk.Entry(ventana)
c_alto.place(x=50, y=120)

contenedor_largo = tk.Label(ventana, text="Largo", bg = "steel blue", fg="black")
contenedor_largo.place(x=10, y=150)
contenedor_largo.config(font = ("Verdana", 7))

c_largo=tk.Entry(ventana)
c_largo.place(x=50, y=150)


formatos = tk.Label(ventana, text="Ingrese la cantidad de formatos de caja", bg = "steel blue", fg="black")
formatos.place(x=10, y=200)
formatos.config(font = ("Verdana", 10))

f_cantidad=tk.Entry(ventana, width=5)
f_cantidad.place(x=300, y=200)

#--------------------- ENTRADA DE FORMATOS DE CAJA -----------------

"""
#----1
datos_caja = tk.Label(ventana, text="Datos del la Caja", bg = "steel blue", fg="black")
datos_caja.place(x=10, y=240)
datos_caja.config(font = ("Verdana", 10))

cantidad_caja = tk.Label(ventana, text="Cantidad: ", bg = "steel blue", fg="black")
cantidad_caja.place(x=10, y=270)
cantidad_caja.config(font = ("Verdana", 7))

c_caja=tk.Entry(ventana, width=4)
c_caja.place(x=70, y=270)

nombre_caja = tk.Label(ventana, text="Nombre: ", bg = "steel blue", fg="black")
nombre_caja.place(x=130, y=270)
nombre_caja.config(font = ("Verdana", 7))

n_caja=tk.Entry(ventana, width=4)
n_caja.place(x=190, y=270)

ancho_caja = tk.Label(ventana, text="Anc: ", bg = "steel blue", fg="black")
ancho_caja.place(x=250, y=270)
ancho_caja.config(font = ("Verdana", 7))

anc_caja=tk.Entry(ventana, width=4)
anc_caja.place(x=280, y=270)

alto_caja = tk.Label(ventana, text="Alt: ", bg = "steel blue", fg="black")
alto_caja.place(x=320, y=270)
alto_caja.config(font = ("Verdana", 7))

alt_caja=tk.Entry(ventana, width=4)
alt_caja.place(x=350, y=270)

largo_caja = tk.Label(ventana, text="Lar: ", bg = "steel blue", fg="black")
largo_caja.place(x=390, y=270)
largo_caja.config(font = ("Verdana", 7))

lar_caja=tk.Entry(ventana, width=4)
lar_caja.place(x=420, y=270)


#----2

cantidad_caja2 = tk.Label(ventana, text="Cantidad: ", bg = "steel blue", fg="black")
cantidad_caja2.place(x=10, y=300)
cantidad_caja2.config(font = ("Verdana", 7))

c_caja2=tk.Entry(ventana, width=4)
c_caja2.place(x=70, y=300)

nombre_caja2 = tk.Label(ventana, text="Nombre: ", bg = "steel blue", fg="black")
nombre_caja2.place(x=130, y=300)
nombre_caja2.config(font = ("Verdana", 7))

n_caja2=tk.Entry(ventana, width=4)
n_caja2.place(x=190, y=300)

ancho_caja2 = tk.Label(ventana, text="Anc: ", bg = "steel blue", fg="black")
ancho_caja2.place(x=250, y=300)
ancho_caja2.config(font = ("Verdana", 7))

anc_caja2=tk.Entry(ventana, width=4)
anc_caja2.place(x=280, y=300)

alto_caja2 = tk.Label(ventana, text="Alt: ", bg = "steel blue", fg="black")
alto_caja2.place(x=320, y=300)
alto_caja2.config(font = ("Verdana", 7))

alt_caja2=tk.Entry(ventana, width=4)
alt_caja2.place(x=350, y=300)

largo_caja2 = tk.Label(ventana, text="Lar: ", bg = "steel blue", fg="black")
largo_caja2.place(x=390, y=300)
largo_caja2.config(font = ("Verdana", 7))

lar_caja2=tk.Entry(ventana, width=4)
lar_caja2.place(x=420, y=300)


#----3

cantidad_caja3 = tk.Label(ventana, text="Cantidad: ", bg = "steel blue", fg="black")
cantidad_caja3.place(x=10, y=330)
cantidad_caja3.config(font = ("Verdana", 7))

c_caja3=tk.Entry(ventana, width=4)
c_caja3.place(x=70, y=330)

nombre_caja3 = tk.Label(ventana, text="Nombre: ", bg = "steel blue", fg="black")
nombre_caja3.place(x=130, y=330)
nombre_caja3.config(font = ("Verdana", 7))

n_caja3=tk.Entry(ventana, width=4)
n_caja3.place(x=190, y=330)

ancho_caja3 = tk.Label(ventana, text="Anc: ", bg = "steel blue", fg="black")
ancho_caja3.place(x=250, y=330)
ancho_caja3.config(font = ("Verdana", 7))

anc_caja3=tk.Entry(ventana, width=4)
anc_caja3.place(x=280, y=330)

alto_caja3 = tk.Label(ventana, text="Alt: ", bg = "steel blue", fg="black")
alto_caja3.place(x=320, y=330)
alto_caja3.config(font = ("Verdana", 7))

alt_caja3=tk.Entry(ventana, width=4)
alt_caja3.place(x=350, y=330)

largo_caja3 = tk.Label(ventana, text="Lar: ", bg = "steel blue", fg="black")
largo_caja3.place(x=390, y=330)
largo_caja3.config(font = ("Verdana", 7))

lar_caja3=tk.Entry(ventana, width=4)
lar_caja3.place(x=420, y=330)

#----4

cantidad_caja4 = tk.Label(ventana, text="Cantidad: ", bg = "steel blue", fg="black")
cantidad_caja4.place(x=10, y=360)
cantidad_caja4.config(font = ("Verdana", 7))

c_caja4=tk.Entry(ventana, width=4)
c_caja4.place(x=70, y=360)

nombre_caja4 = tk.Label(ventana, text="Nombre: ", bg = "steel blue", fg="black")
nombre_caja4.place(x=130, y=360)
nombre_caja4.config(font = ("Verdana", 7))

n_caja4=tk.Entry(ventana, width=4)
n_caja4.place(x=190, y=360)

ancho_caja4 = tk.Label(ventana, text="Anc: ", bg = "steel blue", fg="black")
ancho_caja4.place(x=250, y=360)
ancho_caja4.config(font = ("Verdana", 7))

anc_caja4=tk.Entry(ventana, width=4)
anc_caja4.place(x=280, y=360)

alto_caja4 = tk.Label(ventana, text="Alt: ", bg = "steel blue", fg="black")
alto_caja4.place(x=320, y=360)
alto_caja4.config(font = ("Verdana", 7))

alt_caja4=tk.Entry(ventana, width=4)
alt_caja4.place(x=350, y=360)

largo_caja4 = tk.Label(ventana, text="Lar: ", bg = "steel blue", fg="black")
largo_caja4.place(x=390, y=360)
largo_caja4.config(font = ("Verdana", 7))

lar_caja4=tk.Entry(ventana, width=4)
lar_caja4.place(x=420, y=360)

#----5

cantidad_caja5 = tk.Label(ventana, text="Cantidad: ", bg = "steel blue", fg="black")
cantidad_caja5.place(x=10, y=390)
cantidad_caja5.config(font = ("Verdana", 7))

c_caja5=tk.Entry(ventana, width=4)
c_caja5.place(x=70, y=390)

nombre_caja5 = tk.Label(ventana, text="Nombre: ", bg = "steel blue", fg="black")
nombre_caja5.place(x=130, y=390)
nombre_caja5.config(font = ("Verdana", 7))

n_caja4=tk.Entry(ventana, width=4)
n_caja4.place(x=190, y=390)

ancho_caja5 = tk.Label(ventana, text="Anc: ", bg = "steel blue", fg="black")
ancho_caja5.place(x=250, y=390)
ancho_caja5.config(font = ("Verdana", 7))

anc_caja5=tk.Entry(ventana, width=4)
anc_caja5.place(x=280, y=390)

alto_caja5 = tk.Label(ventana, text="Alt: ", bg = "steel blue", fg="black")
alto_caja5.place(x=320, y=390)
alto_caja5.config(font = ("Verdana", 7))

alt_caja5=tk.Entry(ventana, width=4)
alt_caja5.place(x=350, y=390)

largo_caja5 = tk.Label(ventana, text="Lar: ", bg = "steel blue", fg="black")
largo_caja5.place(x=390, y=390)
largo_caja5.config(font = ("Verdana", 7))

lar_caja5=tk.Entry(ventana, width=4)
lar_caja5.place(x=420, y=390)

"""

#---------------- ENTRADA DE DATOS CON ARCHIVOS 

archivos = tk.Label(ventana, text="Entrada de Datos por Archivo", bg = "steel blue", fg="black")
archivos.place(x=10, y=430)
archivos.config(font = ("Verdana", 10))


#------------------------------------------------------


#--------------- BOTONES --------------

boton1 = tk.Button(ventana, text="Algoritmo1", fg="black", command=algoritmo1, height = 2, width = 30)
boton1.config(font = ("Verdana", 5))
boton1.place(x=300, y=90)

boton2 = tk.Button(ventana, text="Algoritmo2", fg="black", command=algoritmo1, height = 2, width = 30)
boton2.config(font = ("Verdana", 5))
boton2.place(x=300, y=120)

boton3 = tk.Button(ventana, text="Algoritmo3", fg="black", command=lecturaArchivo, height = 2, width = 30)
boton3.config(font = ("Verdana", 5))
boton3.place(x=300, y=150)

boton4 = tk.Button(ventana, text="Generar", fg="black", command=generar, height = 2, width = 15)
boton4.config(font = ("Verdana", 5))
boton4.place(x=360, y=200)

boton5 = tk.Button(ventana, text="Lectura Archivo", fg="black", command=lecturaArchivo, height = 2, width = 15)
boton5.config(font = ("Verdana", 5))
boton5.place(x=230, y=430)


#-----------------------------------------------


ventana.mainloop()
