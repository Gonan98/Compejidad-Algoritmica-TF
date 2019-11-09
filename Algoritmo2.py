from util import quickSort
from Caja import *
from random import randint

def HaySuperpocicion(cajas, empacado, indice):
    queue = cajas.copy()
    c = queue.pop(indice)
    n = len(queue)
    for i in range(n):
        if empacado[i] and queue[i].C == c.C:
            if c.Superpone(queue[i]):
                return True
    return False

def Cabe(cajaActual, cajaAdy, contenedorW, contenedorH, contenedorL):
    for i in range(6):
        cajaActual.ori = i + 1
        if (cajaAdy.x + cajaAdy.Rotado()[0] + cajaActual.Rotado()[0] <= contenedorL
            and cajaAdy.y + cajaAdy.Rotado()[1] + cajaActual.Rotado()[1] <= contenedorW
            and cajaAdy.z + cajaAdy.Rotado()[2] + cajaActual.Rotado()[2] <= contenedorH):
            return True
    cajaActual.ori = 1
    return False

def Algoritmo2(cajas, contenedorW, contenedorH, contenedorL):
    quickSort(cajas,0,len(cajas)-1)
    n = len(cajas)
    contenedor = 0
    empacado = [False] * n
    # out = []
    volumen = 0

    while False in empacado:
        for actual in range(n):
            if not empacado[actual]:
                contenedor+=1
                cajas[actual].C = contenedor
                empacado[actual] = True
                volumen += cajas[actual].Volumen()
            for i in range(n):
                if empacado[i]: continue
                if Cabe(cajas[i], cajas[actual], contenedorW, contenedorH, contenedorL) and not HaySuperpocicion(cajas, empacado, i):
                    cajas[i].x = cajas[actual].x + cajas[actual].Rotado()[0]
                    cajas[i].y = cajas[actual].y
                    cajas[i].z = cajas[actual].z
                    empacado[i] = True
                    cajas[i].C = contenedor
                    volumen += cajas[i].Volumen()
                    # out.append((cajas[i].ident,cajas[i].x,cajas[i].y,cajas[i].z,cajas[i].ori))
                    break

            for j in range(n):
                if empacado[j]: continue
                if Cabe(cajas[j], cajas[actual], contenedorW, contenedorH, contenedorL) and not HaySuperpocicion(cajas, empacado, j):
                    cajas[j].x = cajas[actual].x
                    cajas[j].y = cajas[actual].y + cajas[actual].Rotado()[1]
                    cajas[j].z = cajas[actual].z
                    empacado[j] = True
                    cajas[j].C = contenedor
                    volumen += cajas[j].Volumen()
                    # out.append((cajas[j].ident,cajas[j].x,cajas[j].y,cajas[j].z,cajas[j].ori))
                    break

            for k in range(n):
                if empacado[k]: continue
                if Cabe(cajas[k], cajas[actual], contenedorW, contenedorH, contenedorL) and not HaySuperpocicion(cajas, empacado, k):
                    cajas[k].x = cajas[actual].x
                    cajas[k].y = cajas[actual].y
                    cajas[k].z = cajas[actual].z + cajas[actual].Rotado()[2]
                    empacado[k] = True
                    cajas[k].C = contenedor
                    volumen += cajas[k].Volumen()
                    # out.append((cajas[k].ident,cajas[k].x,cajas[k].y,cajas[k].z,cajas[k].ori))
                    break

    return cajas, contenedor, volumen


def main():
    cajas = []

    for i in range(10):
        while True:
            w = randint(1,30)
            h = randint(1,30)
            l = randint(1,30)
            if w <= h and h <= l:
                cajas.append(Caja(w,l,h,chr(i+65)))
                break
    
    print(Algoritmo2(cajas,20,25,30))

    # for c in gaa:
    #    print(str(c.ident),end=' ')
    #    print(str(c.x),end=' ')
    #    print(str(c.y),end=' ')
    #    print(str(c.z),end=' ')
    #    print(str(c.ori),end=' ')
    #   print(str(c.C),end='   ')
    #   print(str(c.ancho),end=' ')
    #    print(str(c.alto),end=' ')
    #    print(str(c.largo))

if __name__ == "__main__":
    main()