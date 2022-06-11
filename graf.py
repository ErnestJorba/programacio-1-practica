import numpy as np
import graphviz


class Graf:
    def __init__(self, ordre):
        self.__vertex = ordre
        # self.__graf = Matriu(ordre)
        self.__graf = np.zeros(shape=(ordre, ordre),
                               dtype=np.uint8)  # Primer cal generar una matriu de zeros (ho he fet amb numpy)

    def afegir_aresta(self, origen, desti, valor):
        # self.__graf.modificar_valor(origen, desti, valor)
        self.__graf[origen][desti] = valor

    def eliminar_aresta(self, origen, desti):
        # self.__graf.modificar_valor(origen, desti, 0)
        self.__graf[origen][desti] = 0

    def mostrar_graf(self):
        # self.__graf.mostrar_per_pantalla()

        for fila in range(len(self.__graf)):
            for columna in range(len(self.__graf)):
                print(str(int(self.__graf[fila][columna])), end="  ")

            print("")

    def get_matriu_graf(self):
        return self.__graf

    def get_ordre(self):
        return self.__vertex

    def copia(self):
        graf_copia = Graf(self.__vertex)

        for i in range(len(self.__graf)):
            for j in range(len(self.__graf)):
                # pes = self.__graf.get_valor(i, j)
                pes = self.__graf[i][j]
                # graf_copia.__graf.modificar_valor(i, j, pes)
                graf_copia.__graf[i][j] = pes

        return graf_copia

    def algoritme_profunditat(self, v0):  # Considero que no cal explicar l'algoritme, ja que és pràcticament idèntic
        # al pseudocodi
        visitats = set()
        pila = [v0]
        while pila:  # while pila != []:
            v = pila[0]
            pila.pop(0)

            if v not in visitats:
                visitats.add(v)
                for veinat in range(self.__vertex):
                    # if self.__graf.get_valor(v, veinat) != 0 or self.__graf.get_valor(veinat, v) != 0:
                    # if self.__graf[v][veinat] != 0 or self.__graf[veinat][v] != 0:
                    if self.__graf[v][veinat] or self.__graf[veinat][v]:
                        if veinat not in visitats:
                            pila.append(veinat)
        return visitats

    def algoritme_warshall(self):
        g = self.__graf
        n_vertex = self.__vertex
        m = Graf(n_vertex)

        for v_i in range(n_vertex):  # Aquesta és la part d'actualitzar els vèrtexs de g cap a m
            for v_j in range(n_vertex):
                # if g.get_valor(v_i, v_j) != 0:
                if g[v_i][v_j] != 0:
                    # m.__graf.modificar_valor(v_i, v_j, 1)
                    m.__graf[v_i][v_j] = 1

        for v_k in range(n_vertex):
            for v_x in range(n_vertex):
                for v_y in range(n_vertex):
                    # if m.__graf.get_valor(v_x, v_k) != 0 and m.__graf.get_valor(v_k, v_y) != 0:
                    # if m.__graf[v_x][v_k] != 0 and m.__graf[v_k][v_y] != 0:
                    if m.__graf[v_x][v_k] and m.__graf[v_k][v_y]:
                        # m.__graf.modificar_valor(v_x, v_y, 1)
                        m.__graf[v_x][v_y] = 1

        return m

    def algoritme_prim(self):
        s = set()
        s.add(0)
        t = set()

        for i in range(self.__vertex - 1):  # Tenim que en un arbre T = (V, E), *sempre* es compleix que
            # |E| = |V| - 1, on V és el conjunt dels vèrtexs i E el conjunt de les arestes. Com que amb l'algoritme
            # de Prim estem buscant l'arbre minimal d'un graf determinal, quan acabi aquest bucle ja l'haurem trobat.
            # minim_pes = self.__graf.maxim()
            minim_pes = np.amax(self.get_matriu_graf())
            u = 0  # Assigno valors 0 per evitar que PyCharm es queixi, però no caldria
            v = 0
            for v_i in range(self.__vertex):
                for v_j in range(self.__vertex):
                    # if (0 != self.__graf.get_valor(v_i, v_j) <= minim_pes) and (v_i in s) and (v_j not in s):
                    if (0 != self.__graf[v_i][v_j] <= minim_pes) and (v_i in s) and (v_j not in s):
                        # minim_pes = self.__graf.get_valor(v_i, v_j)
                        minim_pes = self.__graf[v_i][v_j]
                        u = v_i
                        v = v_j

            if u != v:
                s.add(v)
                t.add((u, v))

            else:
                return "No es pot aplicar l'algoritme de Prim a aquest graf"

        return t

    def veure_arbre_minimal(self):
        arbre = Graf(self.__vertex)
        llista_arestes = self.algoritme_prim()

        if llista_arestes != "No es pot aplicar l'algoritme de Prim a aquest graf":
            for aresta in llista_arestes:
                # arbre.afegir_aresta(aresta[0], aresta[1], self.__graf.get_valor(aresta[0], aresta[1]))
                arbre.__graf[aresta[0]][aresta[1]] = self.__graf[aresta[0]][aresta[1]]

            arbre.veure_graf()

        else:
            print(llista_arestes)

    def es_connex(self):
        matriu_warshall = self.algoritme_warshall().get_matriu_graf()

        for i in range(len(matriu_warshall)):
            for j in range(len(matriu_warshall)):
                if matriu_warshall[i][j] == 0:
                    return False

        return True

    def veure_graf(self):
        g = graphviz.Digraph("text", filename="grafs/tmp.gv")
        g.attr("node", shape="circle")
        g.attr(rankdir="LR", size="8,5")

        for i in range(len(self.__graf)):
            g.node(str(i))  # Per evitar no representar vèrtexs amb grau d'entrada i de sortida zero

        for fila in range(len(self.__graf)):
            for columna in range(len(self.__graf)):
                # if self.__graf.get_graf().get_valor(fila, columna) != 0:
                if self.__graf[fila][columna]:
                    # g.edge(str(fila), str(columna), label=str(graf.get_graf().get_valor(fila, columna)))
                    g.edge(str(fila), str(columna), label=str(int(self.__graf[fila][columna])))

        g.view()

    def guardar_graf(self, nom_fitxer):

        with open(f"grafs/{nom_fitxer}.txt", "w") as f:
            print(f"{self.get_ordre()}", file=f)

            # for fila in range(graf.get_ordre()):
            for fila in range(len(self.__graf)):
                # for columna in range(graf.get_ordre()):
                for columna in range(len(self.__graf)):
                    # if graf.get_graf().get_valor(fila, columna):
                    if self.__graf[fila][columna]:  # if graf[fila][columna] != 0:
                        # print(f"{fila} {columna} {graf.get_graf().get_valor(fila, columna)}", file=f)
                        print(f"{fila} {columna} {int(self.__graf[fila][columna])}", file=f)

    def __str__(self):
        return f"{self.__vertex}"
