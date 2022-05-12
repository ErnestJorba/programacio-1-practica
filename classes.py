class Conjunt:
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

    def disjunts(self, conjunt2):
        return self.__intersecar(conjunt2).cardinal() == 0

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


class Matriu:

    # Classe matriu quadrada.
    # El constructor rep la mida de la matriu i en crea una de buida
    def __init__(self, n):
        self.__matriu = []
        self.__n = n

        for i in range(n):
            fila = [0] * n

            self.__matriu.append(fila)

    def modificar_valor(self, fila, columna, valor):

        if -1 < fila < self.__n and -1 < columna < self.__n:
            self.__matriu[fila][columna] = valor

    def get_valor(self, fila, columna):

        return self.__matriu[fila][columna]

    # Sobreescrivim la funció len de Python, aquest mètode retorna la mida de la matriu.
    def __len__(self):

        return self.__n

    def mostrar_per_pantalla(self):

        n = self.__n

        for i in range(n):
            for j in range(n):
                if self.__matriu[i][j] < 10:
                    print("0", end="")
                print(self.__matriu[i][j], end=" ")

            print("")

    def copia(self):  # Extra
        copia = Matriu(self.__n)
        for i in range(copia.__n):
            for j in range(copia.__n):
                copia.__matriu[i][j] = self.__matriu[i][j]
        return copia

    def fer_identitat(self):  # Extra
        for i in range(len(self.__matriu)):
            for j in range(len(self.__matriu[i])):
                if i != j:
                    self.__matriu[i][j] = 0
                else:
                    self.__matriu[i][j] = 1

    def __mul__(self, other):
        if type(other) == type(self):
            matriu_mult = Matriu(len(self.__matriu))
            for i in range(len(self.__matriu)):
                for j in range(len(self.__matriu)):
                    for k in range(len(self.__matriu)):
                        matriu_mult.__matriu[i][j] += self.__matriu[i][k] * other.__matriu[k][j]
            return matriu_mult

        if type(other) == type(3):
            matriu_mult = self.copia()
            for i in range(matriu_mult.__n):
                for j in range(matriu_mult.__n):
                    matriu_mult.__matriu[i][j] *= other
            return matriu_mult

    def __pow__(self, power, modulo=None):
        m = self.copia()
        if power > 0:
            for i in range(power):
                m * self
        elif power == 0:
            m.fer_identitat()
        return m

    def __add__(self, other):
        matriu_suma = Matriu(len(self.__matriu))
        for i in range(len(self.__matriu)):
            for j in range(len(self.__matriu)):
                matriu_suma.__matriu[i][j] = self.__matriu[i][j] + other.__matriu[i][j]
        return matriu_suma


class Graf:
    def __init__(self, enter):
        self.__vertex = enter
        self.__graf = Matriu(enter)

    def afegir_aresta(self, origen, desti, valor):
        self.__graf.modificar_valor(origen, desti, valor)

    def eliminar_aresta(self, origen, desti):
        self.__graf.modificar_valor(origen, desti, 0)

    def mostrar_graf(self):
        self.__graf.mostrar_per_pantalla()

    def profunditat(self, v0):
        visitats = Conjunt()
        pila = [v0]
        while pila:  # while pila != []:
            v = pila[0]
            pila.pop(0)
            if not visitats.conte(v):
                visitats.afegir(v)
                for i in range(self.__vertex):
                    if self.__graf.get_valor(v, i) != 0 or self.__graf.get_valor(i, v) != 0:
                        if not visitats.conte(i):
                            pila.append(i)
        return visitats

    """ 
    # El problema de fer servir els conjunts predeterminats de python és que, com que són conjunts, l'ordre no 
    # està definit, i per tant quan ens ensenya el conjunt els elements apareixen en ordre ascendent
    
    def profunditat(self, v0):
        visitats = set()
        pila = [v0]
        while pila:  # while pila != []:
            v = pila[0]
            pila.pop(0)
            if v not in visitats:
                visitats.add(v)
                for veinat in range(self.__vertex):
                    if self.__graf.get_valor(v, veinat) != 0 or self.__graf.get_valor(veinat, v) != 0:
                        if veinat not in visitats:
                            pila.append(veinat)
        return visitats
    """

    def warshall(self):
        g = self.__graf
        n_vertex = self.__vertex
        m = Graf(n_vertex)

    def prim(self):
        a = self.__graf
        return a

    def __str__(self):
        return f"{self.__vertex}"


if __name__ == "__main__":
    graf_exemple = Graf(4)
    graf_exemple.mostrar_graf()
    print(graf_exemple)
