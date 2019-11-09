import tkinter as tk

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

import tkinter.filedialog

pos = 0

arr = []
Largo = 0
Ancho = 0
Alto = 0


TipoEntrada = 0

def LecturaArchivo():
    archivo = tkinter.filedialog.askopenfilename()
    global Largo, Ancho, Alto
    global arr
    global TipoEntrada
    
    TipoEntrada = 1
    
    f = open(archivo, 'r')
    fl = f.readline()
    Largo = int(fl[0])
    Ancho = int(fl[2])
    Alto = int(fl[4])    
    sl = f.readline()
    n = int(sl[0])
    
    for i in range(n):
        cl = f.readline()
        n2 = int(cl[0])
        ide = cl[2]
        l = int(cl[4])
        an = int(cl[6])
        al = int(cl[8])
        for j in range(n2):
            arr.append(caja(an,l,al,ide))
    
    
    f.close()
    
def SalidaArchivo(arr, cont, volOcu):
    f = open('Out.txt','w')
    volDis = 0
    volOcu = 0
    volOcuPor = 100
    f.write('Contenedores usados: '+ str(cont) + '\n')
    f.write('Volumen disponible: '+ str(volDis) + ' m3\n')
    f.write('Volumen ocupado: '+ str(volOcu) + ' m3 (' + str(volOcuPor) + '%)\n')
    f.write('Cajas a transportar: '+ str(cont) + '\n')
    f.write('Contenedor\tFormato\t\tCoordenadas\tOrientacion\tlargo\tancho\talto\n')
    for i in range(len(arr)):
        cj = arr[i]
        f.write(str(cj.C)+'\t\t'+str(cj.ident)+'\t\t('
                +str(cj.x)+','+ str(cj.y)+','+ str(cj.z)+')'
                +'\t\t'+str(cj.ori)+'\t\t'+ str(cj.largo)+'\t'+str(cj.ancho)+'\t'+str(cj.alto)+'\n')
    f.close()

class caja:
    def __init__(self, ancho, largo, alto, ident):
        self.ancho = ancho
        self.largo = largo
        self.alto = alto
        self.volumen = ancho*largo*alto
        self.ident = ident
        self.x = 0
        self.y = 0
        self.z = 0
        self.ori = 1
        self.C = 0
        
    def Volumen(self):
        return self.ancho * self.largo * self.alto
        

def merge1(i, d):
    li = len(i)
    ld = len(d)
    l = li + ld
    ci, cd = 0, 0
    r = []
    while len(r) != l: 
        if cd == ld:
            r.append(i[ci])
            ci += 1
        elif ci == li:
            r.append(d[cd])
            cd += 1
        elif i[ci].alto > d[cd].alto:
            r.append(i[ci])
            ci += 1
        else:  
            r.append(d[cd])
            cd += 1
    return r
    
def Sort1(V): 
    n = len(V)
    if n == 1:
        return V
    else:
        m = n // 2
    return merge1(Sort1(V[ :m]), Sort1(V[m: ]))

def NFDH(arr, an, al, la):
    nC = 1
    volumen = arr[0].Volumen()
    arr[0].C = nC
    xmax = arr[0].largo
    xant = 0
    zn = arr[0].alto
    zant = 0
    for i in range(1, len(arr)):
        volumen += arr[i].ancho * arr[i].alto * arr[0].largo 
        w = arr[i-1].y + arr[i-1].ancho + arr[i].ancho
        if xant + arr[i].largo <= la:
            if w <= an:
                if xmax < xant + arr[i].largo: xmax = xant + arr[i].largo
                arr[i].x = xant
                arr[i].y = arr[i-1].y + arr[i-1].ancho
                arr[i].z = zant
                arr[i].C = nC
            elif arr[i].largo+xmax <= la:
                arr[i].x = xmax
                xant = xmax
                arr[i].y = 0
                arr[i].z = zant
                arr[i].C = nC
                xmax = xmax + arr[i].largo
            elif arr[i].alto + zn <= al:
                xant = 0
                xmax = arr[i].largo
                arr[i].x = 0
                arr[i].y = 0
                zant = zn
                arr[i].z = zn
                zn = arr[i].alto + zn
                arr[i].C = nC
            else:
                nC += 1
                arr[i].C = nC
                xmax = arr[i].largo
                xant = 0
                zn = arr[i].alto
                zant = 0
        elif arr[i].alto + zn <= al:
            xant = 0
            xmax = arr[i].largo
            arr[i].x = 0
            arr[i].y = 0
            zant = zn
            arr[i].z = zn
            zn = arr[i].alto + zn
            arr[i].C = nC
        else:
            nC += 1
            arr[i].C = nC
            xmax = arr[i].largo
            xant = 0
            zn = arr[i].alto
            zant = 0
            
    return arr, nC, volumen


def merge3(i, d):
    li = len(i)
    ld = len(d)
    l = li + ld
    ci, cd = 0, 0
    r = []
    while len(r) != l: 
        if cd == ld:
            r.append(i[ci])
            ci += 1
        elif ci == li:
            r.append(d[cd])
            cd += 1
        elif i[ci].volumen > d[cd].volumen:
            r.append(i[ci])
            ci += 1
        else:  
            r.append(d[cd])
            cd += 1
    return r
    
def Sort3(V): 
    n = len(V)
    if n == 1:
        return V
    else:
        m = n // 2
    return merge3(Sort3(V[ :m]), Sort3(V[m: ]))

def Algoritmo3(arr, an, al, la):
    nC = 1
    volumen = arr[0].ancho * arr[0].alto * arr[0].largo 
    arr[0].C = nC
    
    xmax = arr[0].largo
    
    ymax = arr[0].ancho

    for i in range(1, len(arr)):
        
        volumen += arr[i].ancho * arr[i].alto * arr[i].largo 
        
        if arr[i-1].x + arr[i].largo <= la:
            if  arr[i].ancho + arr[i-1].y <= an:
                if arr[i].alto + arr[i-1].z +arr[i-1].alto <= al:
                    arr[i].C = nC
                    if xmax < arr[i-1].x + arr[i].largo: xmax = arr[i-1].x + arr[i].largo
                    if ymax < arr[i-1].y + arr[i].ancho: ymax = arr[i-1].y + arr[i].ancho
                    arr[i].x = arr[i-1].x
                    arr[i].y = arr[i-1].y
                    arr[i].z = arr[i-1].z + arr[i-1].alto
                else:
                    if  arr[i].ancho + ymax <= an:  
                        arr[i].C = nC
                        arr[i].x = arr[i-1].x
                        arr[i].y = ymax
                        arr[i].z = 0 
                        ymax = arr[i].y + arr[i].ancho
                        if xmax < arr[i-1].x + arr[i].largo: xmax = arr[i-1].x + arr[i].largo
                        
                    else:
                        if xmax + arr[i].largo <= la:
                            arr[i].C = nC
                            arr[i].x = xmax
                            arr[i].y = 0
                            arr[i].z = 0
                            xmax = xmax + arr[i].largo
                            ymax = arr[i].ancho
                        else:
                            xmax = arr[i].largo
                            ymax = arr[i].ancho
                            nC += 1
                            arr[i].C = nC
                        
            else:
                if xmax + arr[i].largo <= la:
                    arr[i].C = nC
                    arr[i].x = xmax
                    arr[i].y = 0
                    arr[i].z = 0
                    xmax = xmax + arr[i].largo
                    ymax = arr[i].ancho
                else:
                    xmax = arr[i].largo
                    ymax = arr[i].ancho
                    nC += 1
                    arr[i].C = nC
        else:
            nC += 1
            arr[i].C = nC
            
    return arr, nC, volumen


def AgregarCaja():
    global arr
    for j in range(int(c_caja.get())):
        arr.append(caja(int(anc_caja.get()), int(lar_caja.get()) , int(alt_caja.get()), int(n_caja.get())))

algoritmo = 1

def BotonAlgoritmo1():
    global algoritmo
    global arr
    global Ancho, Alto, Largo
    global TipoEntrada
    arrAux = arr
    algoritmo = 1
    if TipoEntrada == 0:
        Ancho = int(c_ancho.get())
        Alto = int(c_alto.get())
        Largo = int(c_largo.get())
        MostrarAlgoritmo(algoritmo, arrAux, Ancho, Largo, Alto)
        arr = []
    else:
         MostrarAlgoritmo(algoritmo, arrAux, Ancho, Largo, Alto)
         arr = []
         TipoEntrada = 0
         
         
def BotonAlgoritmo2():
    global algoritmo
    global arr
    global Ancho, Alto, Largo
    global TipoEntrada
    arrAux = arr
    algoritmo = 2
    if TipoEntrada == 0:
        Ancho = int(c_ancho.get())
        Alto = int(c_alto.get())
        Largo = int(c_largo.get())
        MostrarAlgoritmo(algoritmo, arrAux, Ancho, Largo, Alto)
        arr = []
    else:
         MostrarAlgoritmo(algoritmo, arrAux, Ancho, Largo, Alto)
         arr = []
         TipoEntrada = 0

def BotonAlgoritmo3():
    global algoritmo
    global arr
    global Ancho, Alto, Largo
    global TipoEntrada
    arrAux = arr
    algoritmo = 3
    if TipoEntrada == 0:
        Ancho = int(c_ancho.get())
        Alto = int(c_alto.get())
        Largo = int(c_largo.get())
        MostrarAlgoritmo(algoritmo, arrAux, Ancho, Largo, Alto)
        arr = []
    else:
         MostrarAlgoritmo(algoritmo, arrAux, Ancho, Largo, Alto)
         arr = []
         TipoEntrada = 0

def MostrarAlgoritmo(algoritmo, arr, Ancho, Largo, Alto):
    
    if algoritmo == 1:
        arr = Sort1(arr)
        arr, cont, volOcu = NFDH(arr, Ancho, Alto, Largo)
    elif algoritmo == 2:
        arr = Sort3(arr)
        arr, cont, volOcu = Algoritmo3(arr, Ancho, Alto, Largo)
    else:
        arr = Sort3(arr)
        arr, cont, volOcu = Algoritmo3(arr, Ancho, Alto, Largo)
     
    
    SalidaArchivo(arr, cont, volOcu)
    
    plt.rcParams['toolbar'] = 'None'
    
    x, y, z = np.indices((Largo, Ancho, Alto))
    
    arrCubos = []
    voxels = [arrCubos]*cont
    
    for j in range(cont):
        k = 0
        for i in range(len(arr)):
            if arr[i].C == j + 1:
                k += 1
        voxels[j] = [0] * k
    
    for j in range(cont):
        k = 0
        for i in range(len(arr)):
            if arr[i].C == j + 1:
                cubo = (x >= arr[i].x) & (x < arr[i].x + arr[i].largo) & (y >= arr[i].y) & (y < arr[i].y + arr[i].ancho) & (z >= arr[i].z) & (z < arr[i].z + arr[i].alto)
                voxels[j][k]=cubo
                k += 1
    
    global pos
    
    def right(event):
        
        global pos
    
        event.canvas.figure.clear()
        
        ax = fig.gca(projection='3d')
        
        ax.set_xlabel('( X ) Largo')
        ax.set_ylabel('( Y ) Ancho')
        ax.set_zlabel('( Z ) Alto')
        
        
        if pos == len(voxels)-1:
            pos = -1
        
        if pos < len(voxels)-1:
            pos = pos + 1
        
        ax.set_title('Contenedor Número ' + str(pos))
        
        
        for j in range(len(voxels)):
                for i in range(len(voxels[pos])):
                    if i==0:
                        ax.voxels(voxels[pos][i], facecolors='blue', edgecolor='k')
                    elif i%2 == 0:
                        ax.voxels(voxels[pos][i], facecolors='red', edgecolor='k')
                    elif i%3 == 0:
                        ax.voxels(voxels[pos][i], facecolors='brown', edgecolor='k')
                    elif i%5 == 0:
                        ax.voxels(voxels[pos][i], facecolors='green', edgecolor='k')
                    else:
                        ax.voxels(voxels[pos][i], facecolors='yellow', edgecolor='k')
    
        event.canvas.draw()
    
    
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    
    for i in range(len(voxels[0])):
        if i==0:
            ax.voxels(voxels[0][i], facecolors='blue', edgecolor='k')
        elif i%2 == 0:
            ax.voxels(voxels[0][i], facecolors='red', edgecolor='k')
        elif i%3 == 0:
            ax.voxels(voxels[0][i], facecolors='brown', edgecolor='k')
        elif i%5 == 0:
            ax.voxels(voxels[0][i], facecolors='green', edgecolor='k')
        else:
            ax.voxels(voxels[0][i], facecolors='yellow', edgecolor='k')
            
    fig.canvas.mpl_connect('key_press_event', right)
    ax.set_title('Contenedor Número 0')
    ax.set_xlabel('( X ) Largo')
    ax.set_ylabel('( Y ) Ancho')
    ax.set_zlabel('( Z ) Alto')
    plt.show()

ventana = tk.Tk()

ventana.title("ALGORITMOS DE EMPAQUETAMIENTO 3D")

ventana.geometry('500x500')

ventana.configure(background='steel blue')

titulo = tk.Label(ventana, text="ALGORITMOS DE EMPAQUETAMIENTO 3D", bg = "steel blue", fg="black")
titulo.pack(fill=tk.X, padx=20, pady=20)
titulo.config(font = ("Verdana", 12))

#-------------- SALIDA DE DATOS -----------------------
#var = tk.StringVar()
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

#--------------------- ENTRADA DE FORMATOS DE CAJA -----------------

#----1
datos_caja = tk.Label(ventana, text="Datos del la Caja", bg = "steel blue", fg="black")
datos_caja.place(x=10, y=210)
datos_caja.config(font = ("Verdana", 10))
cantidad_caja = tk.Label(ventana, text="Cantidad: ", bg = "steel blue", fg="black")
cantidad_caja.place(x=10, y=250)
cantidad_caja.config(font = ("Verdana", 7))
c_caja=tk.Entry(ventana, width=4)
c_caja.place(x=70, y=250)
nombre_caja = tk.Label(ventana, text="Nombre: ", bg = "steel blue", fg="black")
nombre_caja.place(x=130, y=250)
nombre_caja.config(font = ("Verdana", 7))
n_caja=tk.Entry(ventana, width=4)
n_caja.place(x=190, y=250)
ancho_caja = tk.Label(ventana, text="Anc: ", bg = "steel blue", fg="black")
ancho_caja.place(x=250, y=250)
ancho_caja.config(font = ("Verdana", 7))
anc_caja=tk.Entry(ventana, width=4)
anc_caja.place(x=280, y=250)
alto_caja = tk.Label(ventana, text="Alt: ", bg = "steel blue", fg="black")
alto_caja.place(x=320, y=250)
alto_caja.config(font = ("Verdana", 7))
alt_caja=tk.Entry(ventana, width=4)
alt_caja.place(x=350, y=250)
largo_caja = tk.Label(ventana, text="Lar: ", bg = "steel blue", fg="black")
largo_caja.place(x=390, y=250)
largo_caja.config(font = ("Verdana", 7))
lar_caja=tk.Entry(ventana, width=4)
lar_caja.place(x=420, y=250)

#---------------- ENTRADA DE DATOS CON ARCHIVOS 

archivos = tk.Label(ventana, text="Entrada de Datos por Archivo", bg = "steel blue", fg="black")
archivos.place(x=10, y=320)
archivos.config(font = ("Verdana", 10))

#------------------------------------------------------

#--------------- BOTONES --------------

boton1 = tk.Button(ventana, text="Algoritmo1", fg="black", command=BotonAlgoritmo1, height = 2, width = 30)
boton1.config(font = ("Verdana", 5))
boton1.place(x=320, y=90)

boton2 = tk.Button(ventana, text="Algoritmo2", fg="black", command=BotonAlgoritmo2, height = 2, width = 30)
boton2.config(font = ("Verdana", 5))
boton2.place(x=320, y=120)

boton3 = tk.Button(ventana, text="Algoritmo3", fg="black", command=BotonAlgoritmo3, height = 2, width = 30)
boton3.config(font = ("Verdana", 5))
boton3.place(x=320, y=150)

boton4 = tk.Button(ventana, text="Agregar Caja", fg="black", command=AgregarCaja, height = 2, width = 15)
boton4.config(font = ("Verdana", 5))
boton4.place(x=380, y=215)

boton5 = tk.Button(ventana, text="Lectura Archivo", fg="black", command=LecturaArchivo, height = 2, width = 15)
boton5.config(font = ("Verdana", 5))
boton5.place(x=230, y=320)

#-----------------------------------------------

ventana.mainloop()