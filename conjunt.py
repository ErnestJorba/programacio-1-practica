class Conjunt:  # No la faig servir perquè he substituït aquesta classe pels sets de python
    def __init__(self):
        self.__elements = []

    def afegir(self, e):
        if e not in self.__elements:
            self.__elements.append(e)

    def eliminar(self, e):
        if e in self.__elements:
            self.__elements.remove(e)

    def cardinal(self):
        return len(self.__elements)

    @staticmethod
    def unio(other1, other2):
        conjunt_unio = Conjunt()

        for element in other1.__elements:
            conjunt_unio.afegir(element)

        for element in other2.__elements:
            conjunt_unio.afegir(element)

    def __intersecar(self, conjunt2):
        interseccio = Conjunt()

        for element in self.__elements:
            if element in conjunt2.__elements:
                interseccio.afegir(element)

        return interseccio

    @staticmethod
    def interseccio(other1, other2):
        return other1.__intersecar(other2)

    @staticmethod
    def disjunts(other1, other2):
        return other1.__intersecar(other2).cardinal() == 0

    def conte(self, e):
        return e in self.__elements

    def es_subconjunt(self, conjunt2):
        for element in self.__elements:
            if not conjunt2.conte(element):
                return False
        return True

    def copia(self):
        c = Conjunt()
        for element in self.__elements:
            c.afegir(element)
        return c

    def __str__(self):
        seq = ""
        for element in self.__elements:
            seq += str(element) + ", "
        return "{" + seq[0:-2] + "}"
