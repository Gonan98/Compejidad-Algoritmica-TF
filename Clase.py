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
    
    def setX(self, x):
        self.x = x
        
    def setY(self, y):
        self.y = y
        
    def setZ(self, z):
        self.z = z
        
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
f = open('Pack.txt', 'r')
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