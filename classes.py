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
        self.__arestes = 0

    def afegir_aresta(self, origen, desti, valor):
        self.__graf.modificar_valor(origen, desti, valor)
        self.__arestes += 1

    def eliminar_aresta(self, origen, desti):
        self.__graf.modificar_valor(origen, desti, 0)

    def mostrar_graf(self):
        self.__graf.mostrar_per_pantalla()

    def get_graf(self):
        return self.__graf

    def get_mida(self):
        return self.__vertex

    def get_ordre(self):
        return self.__arestes

    def copia(self):
        graf_copia = Graf(self.__vertex)

        for i in range(len(self.__graf)):
            for j in range(len(self.__graf)):
                pes = self.__graf.get_valor(i, j)
                graf_copia.__graf.modificar_valor(i, j, pes)

        return graf_copia

    def algoritme_profunditat(self, v_0):
        visitats = Conjunt()
        pila = [v_0]

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

    def algoritme_warshall(self):  # no se si funciona be perque no tinc clar que ha de fer exactament
        g = self.__graf
        n_vertex = self.__vertex
        m = self.copia()

        for v_k in range(n_vertex):
            for v_x in range(n_vertex):
                for v_y in range(n_vertex):
                    if g.get_valor(v_x, v_k) != 0 and g.get_valor(v_k, v_y) != 0:
                        m.__graf.modificar_valor(v_x, v_y, 1)

        return m

    def algoritme_prim(self):
        if self.__arestes >= self.__vertex - 1:
            s = set()
            s.add(0)
            t = list()

            while True:
                minim_pes = self.__graf.maxim()
                u = 0
                v = 0

                for v_i in range(self.__vertex):
                    for v_j in range(self.__vertex):
                        if (0 != self.__graf.get_valor(v_i, v_j) <= minim_pes) and (v_i in s) and (v_j not in s):
                            minim_pes = self.__graf.get_valor(v_i, v_j)
                            u = v_i
                            v = v_j

                s.add(v)
                t.append((u, v))

                if len(t) == self.__vertex - 1:  # Tenim que en un arbre T = (V, E) *sempre* es cumpleix que
                    # |E| = |V| - 1, on V és el conjunt dels vèrtexs i E el conjunt de les arestes.
                    break

            return t

        else:
            return "No es pot aplicar l'algoritme de Prim a aquest graf"

    def __str__(self):
        return f"{self.__vertex}"
