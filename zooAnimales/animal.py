import zooAnimales as zoo
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
        return self._edad

    def setEdad(self, edad):
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

    @staticmethod
    def totalPorTipo():
        return "Mamiferos : " + str(zoo.mamifero.Mamifero.cantidadMamiferos()) +\
                "\nAves : " + str(zoo.ave.Ave.cantidadAves()) +\
                "\nReptiles : " + str(zoo.reptil.Reptil.cantidadReptiles()) +\
                "\nPeces : " + str(zoo.pez.Pez.cantidadPeces()) +\
                "\nAnfibios : " + str(zoo.anfibio.Anfibio.cantidadAnfibios())

    def toString(self):
        info = "Mi nombre es "+self._nombre+", tengo una edad de "+str(self._edad)+", habito en "+self._habitat+\
        " y mi genero es "+genero;
        if (self._zona != None):
            return info+", la zona en la que me ubico es: "+self._zona.getNombre()+\
                ", en el "+self._zona.getZoo().getNombre();

        else: return info






