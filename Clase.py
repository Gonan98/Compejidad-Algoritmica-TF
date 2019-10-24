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
    
    def setX(self, x):
        self.x = x
        
    def setY(self, y):
        self.y = y
        
    def setZ(self, z):
        self.z = z
        
    def setC(self, C):
        self.C = C
        
    def getC(self):
        return self.C
        
    def getX(self):
        return self.x
        
    def getY(self):
        return self.y
        
    def getZ(self):
        return self.z
    
    def getAncho(self):
        return self.ancho
        
    def getLargo(self):
        return self.largo
        
    def getAlto(self):
        return self.alto
    
    def getVolumen(self):
        return self.alto
    
    def getIdent(self):
        return self.ident
    
    def getOri(self):
        return self.ori


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
    for i in range(n2):
        arr.append(caja(an,l,al,ide))
        
f.close()

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
    f.write(str(cj.getC())+'\t\t'+str(cj.getIdent())+'\t('
            +str(cj.getX())+','+ str(cj.getY())+','+ str(cj.getZ())+')'
            +'\t\t'+str(cj.getOri())+'\n')
f.close()