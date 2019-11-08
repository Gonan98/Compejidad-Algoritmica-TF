from util import quickSort
from Caja import *
from random import randint

def HaySuperpocicion(cajaActual, cajas, empacado):
    n = len(cajas)
    for i in range(n):
        if empacado[i]:
            if cajas[i].Superpone(cajaActual):
                return True
    return False

def Cabe(cajaActual, cajaAdyacente, contenedorW, contenedorH, contenedorL):
    for i in range(6):
        cajaActual.ori = i + 1
        if (cajaAdyacente.x + cajaAdyacente.Rotado()[0] + cajaActual.Rotado()[0] <= contenedorL
        and cajaAdyacente.y + cajaAdyacente.Rotado()[1] + cajaActual.Rotado()[1] <= contenedorW
        and cajaAdyacente.y + cajaAdyacente.Rotado()[2] + cajaActual.Rotado()[2] <= contenedorH):
            return True
    cajaActual.ori = 1
    return False

def Algoritmo2(cajas, contenedorW, contenedorH, contenedorL):
    quickSort(cajas,0,len(cajas)-1)
    n = len(cajas)
    contenedor = 1
    # print(cajas[0].Volumen())
    # print(cajas[n-1].Volumen())
    empacado = [False] * n
    empacado[0] = True
    tree = [[] for _ in range(n)]
    cont = 1
    cajas[0].C = contenedor
    coords = [(cajas[0].ident,cajas[0].x,cajas[0].y,cajas[0].z,cajas[0].ori)]

    while False in empacado:
        for i in range(cont,n):
            if empacado[i]: continue
            if Cabe(cajas[i], cajas[cont-1], contenedorW, contenedorH, contenedorL):
                cajas[i].x = cajas[cont-1].x + cajas[cont-1].Rotado()[0]
                cajas[i].y = cajas[cont-1].y
                cajas[i].z = cajas[cont-1].z
                empacado[i] = True
                coords.append((cajas[i].ident,cajas[i].x,cajas[i].y,cajas[i].z,cajas[i].ori))
                tree[cont-1].append(i+1)
                break

        for j in range(cont,n):
            if empacado[j]: continue
            if Cabe(cajas[j], cajas[cont-1], contenedorW, contenedorH, contenedorL):
                cajas[j].x = cajas[cont-1].x
                cajas[j].y = cajas[cont-1].y + cajas[cont-1].Rotado()[1]
                cajas[j].z = cajas[cont-1].z
                empacado[j] = True
                coords.append((cajas[j].ident,cajas[j].x,cajas[j].y,cajas[j].z,cajas[j].ori))
                tree[cont-1].append(j+1)
                break

        cont += 1
    return coords


def main():
    c1 = Caja(10,10,10,'A')
    c2 = Caja(5,5,5,'B')
    c3 = Caja(3,9,8,'C')
    c4 = Caja(4,7,6,'D')
    c5 = Caja(10,13,11,'E')
    cajas = []

    for i in range(10):
        while True:
            w = randint(1,15)
            h = randint(1,15)
            l = randint(1,15)
            if w <= h and h <= l:
                cajas.append(Caja(w,l,h,chr(i+65)))
                break
    
    # print(cajas)

    """
    if c1.Superpone(c2):
        print('hay superposicion')
    else:
        print('no hay superposicion')
    """
    print(Algoritmo2(cajas,20,30,40))

if __name__ == "__main__":
    main()