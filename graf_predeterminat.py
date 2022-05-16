import classes
import graphviz


def test_funcions():

    graf_test2 = classes.Graf(4)
    graf_test2.afegir_aresta(0, 1, 1)
    graf_test2.afegir_aresta(1, 0, 1)
    graf_test2.afegir_aresta(1, 2, 1)
    graf_test2.afegir_aresta(2, 1, 1)
    graf_test2.afegir_aresta(0, 2, 1)
    graf_test2.afegir_aresta(2, 0, 1)
    graf_test2.afegir_aresta(2, 3, 1)
    graf_test2.afegir_aresta(3, 2, 1)

    # graf_test2.mostrar_graf()
    # print(f"Graf 2: {subprogrames.es_connex(graf_test2)}")
    # print(graf_test2.algoritme_prim())

    graf_test3 = classes.Graf(5)
    graf_test3.afegir_aresta(0, 1, 1)
    # graf_test3.afegir_aresta(1, 0, 1)
    graf_test3.afegir_aresta(0, 2, 3)
    # graf_test3.afegir_aresta(2, 0, 3)
    graf_test3.afegir_aresta(0, 3, 2)
    # graf_test3.afegir_aresta(3, 0, 2)
    graf_test3.afegir_aresta(1, 3, 2)
    # graf_test3.afegir_aresta(3, 1, 2)
    graf_test3.afegir_aresta(3, 2, 1)
    # graf_test3.afegir_aresta(2, 3, 1)
    graf_test3.afegir_aresta(2, 4, 4)
    # graf_test3.afegir_aresta(4, 2, 4)
    graf_test3.afegir_aresta(3, 4, 3)
    # graf_test3.afegir_aresta(4, 3, 3)
    graf_test3.afegir_aresta(4, 1, 4)
    # graf_test3.afegir_aresta(1, 4, 4)

    print(f"Graf 3: {graf_test3.algoritme_prim()}")
    # print(subprogrames.es_connex(graf_test3))

    graf_test4 = classes.Graf(6)
    graf_test4.afegir_aresta(0, 2, 1)
    # graf_test4.afegir_aresta(2, 0, 1)
    graf_test4.afegir_aresta(2, 1, 1)
    # graf_test4.afegir_aresta(1, 2, 1)
    graf_test4.afegir_aresta(2, 3, 4)
    # graf_test4.afegir_aresta(3, 2, 4)
    graf_test4.afegir_aresta(1, 3, 3)
    # graf_test4.afegir_aresta(3, 1, 3)
    graf_test4.afegir_aresta(3, 5, 2)
    # graf_test4.afegir_aresta(5, 3, 2)
    graf_test4.afegir_aresta(3, 4, 5)
    # graf_test4.afegir_aresta(4, 3, 5)
    graf_test4.afegir_aresta(5, 4, 3)
    # graf_test4.afegir_aresta(4, 5, 3)

    print(f"Graf 4: {graf_test4.algoritme_prim()}")
    # graf_test4.mostrar_graf()
    # print(subprogrames.es_connex(graf_test4))

    graf_test4.algoritme_warshall().mostrar_graf()

    matiru = [[1, 2, 3], [3, 5, 6], [7, 8, 9]]


def llegir_fitxers():
    with open("grafs/graf_exemple.txt") as f:
        for line in f:
            fields = line.split()
            if len(fields) == 1:
                graf_fitxer = classes.Graf(int(fields[0]))
            else:
                print(fields)
                graf_fitxer.afegir_aresta(int(fields[0]), int(fields[1]), int(fields[2]))

    graf_fitxer.mostrar_graf()


def guardar_graf(graf):
    print("Introdueix el nom que li vols posar al teu fitxer (no li posis l'extensió .txt): ")
    nom_fitxer = input("    → ")

    with open(f"grafs/{nom_fitxer}.txt", "w") as f:
        print(f"{graf}", file=f)
        for i in range(graf.get_mida()):
            for j in range(graf.get_mida()):
                if graf.get_graf().get_valor(i, j) != 0:
                    print(f"{i} {j} {graf.get_graf().get_valor(i, j)}", file=f)


if __name__ == "__main__":
    graf_test1 = classes.Graf(4)
    graf_test1.afegir_aresta(0, 1, 1)
    graf_test1.afegir_aresta(2, 1, 1)
    graf_test1.afegir_aresta(3, 1, 1)
    graf_test1.afegir_aresta(1, 3, 1)
    graf_test1.afegir_aresta(3, 3, 1)

    # test_funcions()
    # llegir_fitxers()
    # guardar_graf(graf_test1)

    f = graphviz.Digraph("text", filename="grafs/tmp.pdf")
    f.attr(rankdir="LR", size="8,5")
    f.attr("node", shape="circle")

    for i in range(graf_test1.get_mida()):
        for j in range(graf_test1.get_mida()):
            if graf_test1.get_graf().get_valor(i, j) != 0:
                f.edge(str(i), str(j), label=str(graf_test1.get_graf().get_valor(i, j)))

    f.view()



