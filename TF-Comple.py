import random as rnd

class Caja:
    def __init__(self, ancho, largo, alto, ident):
        self.ancho = ancho
        self.largo = largo
        self.alto = alto
        self.ident = ident
        self.x = 0
        self.y = 0
        self.z = 0
        self.ori = 1
        self.C = 0
    
    def Volumen(self):
        return self.ancho * self.largo * self.alto

    def Rotado(self):
        if self.ori == 1:
            return self.largo, self.ancho, self.alto
        elif self.ori == 2:
            return self.ancho, self.largo, self.alto
        elif self.ori == 3:
            return self.largo, self.alto, self.ancho
        elif self.ori == 4:
            return self.alto, self.largo, self.ancho
        elif self.ori == 5:
            return self.ancho, self.alto, self.largo
        elif self.ori == 6:
            return self.alto, self.ancho, self.largo
        else:
            return -1, -1, -1
    
    def Colisiona(self, caja):
        l1,w1,h1 = self.Rotado()
        l2,w2,h2 = caja.Rotado()
        return self.x <= caja.x + l2 and self.x + l1 >= caja.x and self.y <= caja.y + w2 and self.y + w1 >= caja.y and self.z <= caja.z + h2 and self.z + h1 >= caja.z

    # Pos1: x->largo y->ancho z->alto
    # Pos2: x->ancho y->largo z->alto
    # Pos3: x->largo y->alto z->ancho
    # Pos4: x->alto y->largo z->ancho
    # Pos5: x->ancho y->alto z->largo
    # Pos6: x->alto y->ancho z->largo

""" GENERACION AUTOMATICA DE DATOS:

arr = []
An = rnd.randint(1,50)
L = rnd.randint(1,50)
Al = rnd.randint(1,50)
n = rnd.randint(1,10)
for i in range(n):
    ide = chr(i+1+64)
    an = rnd.randint(1, An)
    l = rnd.randint(1, L)
    al = rnd.randint(1, Al)
    n2 = rnd.randint(1, 5)
    for j in range(n2):
        arr.append(caja(an,l,al,ide))
"""


""" ENTRADA MANUAL DE DATOS:

arr = []
An = int(input('Ingresa el ancho del contenedor: '))
L = int(input('Ingresa el largo del contenedor: '))
Al = int(input('Ingresa el alto del contenedor: '))
n = int(input('Ingresa la cantidad de cajas rectangulares: '))

for i in range(n):
    print("Ingresa el id de la caja #", i+1, ": ",end=" ")
    ide = input()
    an = int(input('Ingresa el ancho de la caja: '))
    l = int(input('Ingresa el largo de la caja: '))
    al = int(input('Ingresa el alto de la caja: '))
    n2 = int(input('Cantidad de cajas con este formato: '))
    for j in range(n2):
        arr.append(caja(an,l,al,ide))
"""

#Ingreso de datos por archivo

An, L, Al = 0, 0, 0
arr = []
f = open('In.txt', 'r')
fl = f.readline()
An = int(fl[0])
L = int(fl[2])
Al = int(fl[4])

sl = f.readline()
n = int(sl[0])

for i in range(n):
    cl = f.readline()
    n2 = int(cl[0])
    ide = cl[2]
    an = int(cl[4])
    l = int(cl[6])
    al = int(cl[8])
    for j in range(n2):
        arr.append(Caja(an,l,al,ide))
        
f.close()

#Salida de datos en archivo

f = open('Out.txt','w')
cont = 0
volDis = 0
volOcu = 0
volOcuPor = 100
nC = len(arr)
f.write('Contenedores usados: '+ str(cont) + '\n')
f.write('Volumen disponible: '+ str(volDis) + ' m3\n')
f.write('Volumen ocupado: '+ str(volOcu) + ' m3 (' + str(volOcuPor) + '%)\n')
f.write('Cajas a transportar: '+ str(nC) + '\n')
f.write('Contenedor\tFormato\tCoordenadas\tOrientacion\n')
for i in range(nC):
    cj = arr[i]
    f.write(str(cj.C)+'\t\t'+str(cj.ident)+'\t('
            +str(cj.x)+','+ str(cj.y)+','+ str(cj.z)+')'
            +'\t\t'+str(cj.ori)+'\n')
f.close()