from gestion.zona import Zona
class Zoologico:

    def __init__(self,nombre,ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zona = []

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getUbicacion(self):
        return self._Ubicacion

    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion

    def getZona(self):
        return self._zona

    def setZona(self,zona):
        self._zona = zona

    def agregarZonas(self, zona):
        self._zona.append(zona)

    def cantidadTotalAnimales(self):
        total = 0
        for zona in self._zona:
            total += zona.cantidadTotalAnimales()
        return total