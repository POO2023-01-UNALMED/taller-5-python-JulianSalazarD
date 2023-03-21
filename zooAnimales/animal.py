import zooAnimales
class Animal:
    _totalAnimales = 0

    def __init__(self, nombre, edad, habitat, genero):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None
        Animal._totalAnimales += 1

    @classmethod
    def getTotalAnimales(cls):
        return cls._totalAnimales

    @classmethod
    def setTotalAnimales(cls, totalAnimales):
        cls._totalAnimales = totalAnimales

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getEdad(self):
        return self._Edad

    def setEdad(self, Edad):
        self._edad = edad

    def getHabitat(self):
        return self._habitat

    def setHabitat(self, Habitat):
        self._habitat = habitat

    def getGenero(self):
        return self._genero

    def setGenero(self, genero):
        self._genero = genero

    def getZona(self):
        return self._zona

    def setZona(self, zona):
        self._zona = zona

    def movimiento(self):
        return "desplazarse"

    def totalPorTipo(self):
        return "Mamiferos: " + Mamifero.cantidadMamiferos() +\
                "\nAves: " + Ave.cantidadAves() +\
                "\nReptiles: " + Reptil.cantidadReptiles() +\
                "\nPeces: " + Pez.cantidadPeces() +\
                "\nAnfibios: " + Anfibio.cantidadAnfibios()

    def __str__(self):
        info = "Mi nombre es "+nombre+", tengo una edad de "+edad+", habito en "+habitat+\
        " y mi genero es "+genero;
        if (zona != None):
            return info+", la zona en la que me ubico es: "+zona.getNombre()+\
                ", en el "+zona.getZoo().getNombre();

        else: return info






