import graphviz
import glob
import numpy as np

import classes


def es_connex_no_funciona(graf):
    a = graf.get_graf()
    matriu_graf = a.copy()
    for i in range(len(matriu_graf)):
        # matriu_graf += matriu_graf ** (i + 1)
        matriu_graf += np.linalg.matrix_power(matriu_graf, i + 1)

    # matriu = matriu_graf.get_matriu()

    for i in range(len(matriu_graf)):
        for j in range(len(matriu_graf)):
            if matriu_graf[i][j] == 0:
                return False

    return True

    # Una altra manera de veure si és connex o no seria mirant la matriu resultant de l'algoritme de
    # Warshall i veure si hi ha algun zero. Si és que sí, el graf no és connex. Altrament sí que ho és.


def es_connex(graf):
    matriu_warshall = graf.algoritme_warshall().get_graf()

    for i in range(len(matriu_warshall)):
        for j in range(len(matriu_warshall)):
            if matriu_warshall[i][j] == 0:
                return False

    return True


def guardar_graf(graf, nom_fitxer):

    with open(f"grafs/{nom_fitxer}.txt", "w") as f:
        print(f"{graf}", file=f)

        # for fila in range(graf.get_mida()):
        for fila in range(len(graf.get_graf())):
            # for columna in range(graf.get_mida()):
            for columna in range(len(graf.get_graf())):
                # if graf.get_graf().get_valor(fila, columna):
                if graf[fila][columna]:  # if graf[fila][columna] != 0:
                    # print(f"{fila} {columna} {graf.get_graf().get_valor(fila, columna)}", file=f)
                    print(f"{fila} {columna} {graf[fila][columna]}", file=f)


def llegir_graf():
    fitxers = glob.glob("grafs/*.txt")

    with open(fitxers[int(input("→ ")) - 1]) as f:
        for line in f:
            fields = line.split()
            if len(fields) == 1:
                graf_fitxer = classes.Graf(int(fields[0]))
            elif len(fields) == 3:
                graf_fitxer.afegir_aresta(int(fields[0]), int(fields[1]), int(fields[2]))
            else:
                print("Hi ha hagut un error llegint el fitxer. Si us plau, mireu que tot sigui correcte")
                quit()

    return graf_fitxer


def veure_graf(graf):
    g = graphviz.Digraph("text", filename="grafs/tmp.gv")
    g.attr("node", shape="circle")
    g.attr(rankdir="LR", size="8,5")

    for fila in range(graf.get_mida()):
        for columna in range(graf.get_mida()):
            # if graf.get_graf().get_valor(fila, columna) != 0:
            if graf.get_graf()[fila][columna] != 0:
                # g.edge(str(fila), str(columna), label=str(graf.get_graf().get_valor(fila, columna)))
                g.edge(str(fila), str(columna), label=str(int(graf.get_graf()[fila][columna])))

    g.view()


def que_fer_amb_el_graf(graf):
    while True:
        print("\nQuè vols fer ara?\n (0) Tornar al menú principal\n (1) Veure la matriu adjacent\n "
              "(2) Veure el teu graf en format PDF\n (3) Veure si és connex\n (4) Aplicar l'algoritme de profunditat\n "
              "(5) Aplicar l'algoritme de Warshall\n (6) Aplicar l'algoritme de Prim")
        eleccio = int(input("→ "))

        if eleccio == 1:
            graf.mostrar_graf()
            # time.sleep(2)

        elif eleccio == 2:
            veure_graf(graf)

        elif eleccio == 3:
            if es_connex(graf):
                print("Sí que és connex")
                # time.sleep(2)

            else:
                print("No és connex")
                # time.sleep(2)

        elif eleccio == 4:
            print("Introdueix el vèrtex on vols començar:")
            print(graf.algoritme_profunditat(int(input("→ "))))
            # time.sleep(2)

        elif eleccio == 5:
            graf.algoritme_warshall().mostrar_graf()
            # time.sleep(2)

        elif eleccio == 6:
            print(graf.algoritme_prim())
            # time.sleep(2)

        elif eleccio == 0:
            print("Vols guardar el graf?\n (0) No\n (1) Sí")
            eleccio = int(input("→ "))

            while True:
                if eleccio == 0:
                    print("Tornant al menú principal...")
                    # time.sleep(0.5)
                    break

                elif eleccio == 1:
                    print("Introdueix el nom que li vols posar al fitxer (sense extensió):")
                    nom = input("→ ")
                    guardar_graf(graf, nom)
                    print("Tornant al menu principal", end="")
                    # time.sleep(0.5)
                    break

                else:
                    print("Si us plau, introdueix una opció vàlida")
                    # time.sleep(0.5)

            break

        else:
            print("Si us plau, introdueix una opció vàlida")
            # time.sleep(0.5)
