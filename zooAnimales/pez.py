from zooAnimales.animal import Animal
class Pez(Animal):
    _listado = []
    salmones = 0
    bacalaos = 0

    def __init__(self,nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Pez._listado.append(self)

    @classmethod
    def getListado(cls):
        return cls._listado

    @classmethod
    def setListado(cls, listado):
        cls._listado = listado

    def getColorEscamas(self):
        return self._colorEscamas

    def setColorEscamas(self, color):
        self._colorEscamas = color

    def getCantidadAletas(self):
        return self._cantidadAletas

    def setCantidadAletas(self, cantidadAletas):
        self._cantidadAletas = cantidadAletas

    @classmethod
    def cantidadPeces(cls):
        return len(cls.__listado)

    def movimiento(self):
        return "nadar"

    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        pez = Pez(nombre, edad, "oceano", genero, "rojo", 6)
        cls.salmones += 1
        return pez

    @classmethod
    def crearBacalao(cls, nombre, edad, genero):
        pez = Pez(nombre, edad, "oceano", genero, "gris", 6)
        cls.bacalaos += 1
        return pez

    def __str__(self):
        super().__str__()