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

    def get_matriu(self):
        return self.__matriu

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

    def maxim(self):
        maxim = 0
        for fila in self.__matriu:
            for numero in fila:
                if numero > maxim:
                    maxim = numero
        return maxim

    def copia(self):
        copia = Matriu(self.__n)

        for i in range(copia.__n):
            for j in range(copia.__n):
                copia.__matriu[i][j] = self.__matriu[i][j]

        return copia

    def fer_identitat(self):
        for i in range(len(self.__matriu)):
            for j in range(len(self.__matriu[i])):
                if i != j:
                    self.__matriu[i][j] = 0
                else:
                    self.__matriu[i][j] = 1

    def __mul__(self, other):
        matriu_mult = Matriu(len(self.__matriu))

        for i in range(len(self.__matriu)):
            for j in range(len(self.__matriu)):
                for k in range(len(self.__matriu)):
                    matriu_mult.__matriu[i][j] += self.__matriu[i][k] * other.__matriu[k][j]

        return matriu_mult

    def __pow__(self, power, modulo=None):
        m = self.copia()

        if power > 0:
            for i in range(power):
                m *= self

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
    def __init__(self, ordre):
        self.__vertex = ordre
        self.__graf = Matriu(ordre)

    def afegir_aresta(self, origen, desti, valor):
        self.__graf.modificar_valor(origen, desti, valor)
        # self.__graf.modificar_valor(desti, origen, valor)

    def eliminar_aresta(self, origen, desti):
        self.__graf.modificar_valor(origen, desti, 0)

    def mostrar_graf(self):
        self.__graf.mostrar_per_pantalla()

    def get_graf(self):
        return self.__graf

    def copia(self):
        graf_copia = Graf(self.__vertex)

        for i in range(len(self.__graf)):
            for j in range(len(self.__graf)):
                pes = self.__graf.get_valor(i, j)
                graf_copia.__graf.modificar_valor(i, j, pes)

        return graf_copia

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

    # def warshall(self):
    #     g = self.__graf
    #     n_vertex = self.__vertex
    #     m = self.copia()

    """
    def prim(self):
        s = Conjunt()
        t = Conjunt()
        v_0 = 0
        s.afegir(v_0)

        for i in range(1, self.__vertex - 1):
            if 0 != self.__graf.get_valor(i, i + 1) < self.__graf.get_valor(i + 1, i) != 0:
                t.afegir((i, i + 1))
                s.afegir(i + 1)
            elif 0 != self.__graf.get_valor(i, i + 1) > self.__graf.get_valor(i + 1, i) != 0:
                t.afegir((i + 1, i))
                s.afegir(i)
    return t
    """

    """
    def prim(self):
        s = set()
        s.add(0)
        t = set()

        for i in range(1, self.__vertex):
            aresta_minima = sys.maxsize
            s_copia = s.copy()
            for vertex in s_copia:
                if i not in s:
                    aresta = self.__graf.get_valor(vertex, i)
                    if 0 < aresta < aresta_minima:
                        aresta_minima = aresta
                        t.add((i, vertex))
                        s.add(i)

        return t
    """

    def prim(self):
        s = [0]
        t = []

        while True:
            s_copia = s.copy()
            v = s_copia[-1]  # aixo no acaba de funcionar
            minim_pes = self.__graf.maxim()

            for i in range(1, self.__vertex):
                if 0 != self.__graf.get_valor(v, i) <= minim_pes and i not in s:
                    minim_pes = self.__graf.get_valor(v, i)
                    vertex_adjacent = i

            s.append(vertex_adjacent)
            t.append((v, vertex_adjacent))

            if len(t) == self.__vertex - 1:  # Tenim que en un arbre T = (V, E) *sempre* es cumpleix que |E| = |V| - 1,
                # amb V el conjunt dels vèrtexs i E el conjunt de les arestes.
                break

        return t

    def __str__(self):
        return f"{self.__vertex}"


if __name__ == "__main__":
    print("Hello world!")
