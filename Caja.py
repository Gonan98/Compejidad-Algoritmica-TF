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

    def Coordenadas(self):
        return self.x, self.y, self.z
    
    def Superpone(self, caja):
        l1,w1,h1 = self.Rotado()
        l2,w2,h2 = caja.Rotado()
        return self.x < caja.x + l2 and self.x + l1 > caja.x and self.y < caja.y + w2 and self.y + w1 > caja.y and self.z < caja.z + h2 and self.z + h1 > caja.z
