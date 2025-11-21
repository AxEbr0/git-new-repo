class UnaPython:
    longitud = int
    nombre = str
    cofre

    def __init__(self, nombre, longitud, cofre):
        self.nombre = nombre
        self.longitud = longitud
        self.cofre = cofre

    def __init__(self, nombre, longitud):
        self.nombre = nombre
        self.longitud = longitud
    
    def getNombre(self):
        return self.nombre
    def getLongitud(self):
        return self.longitud
    def getCofre(self):
        return self.cofre
    def setCofre(self, cofre):
        self.cofre = cofre;
