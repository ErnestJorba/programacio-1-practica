import glob
import time

import graphviz

import classes
import subprogrames


def guardar_graf(graf):
    print("Introdueix el nom que li vols posar al teu fitxer (no cal posar l'extensió .txt): ")
    nom_fitxer = input("→ ")

    with open(f"grafs/{nom_fitxer}.txt", "w") as f:
        print(f"{graf}", file=f)
        for fila in range(graf.get_mida()):
            for columna in range(graf.get_mida()):
                if graf.get_graf().get_valor(fila, columna):
                    print(f"{fila} {columna} {graf.get_graf().get_valor(fila, columna)}", file=f)


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
    f = graphviz.Digraph("text", filename="grafs/tmp.gv")
    f.attr(rankdir="LR", size="8,5")
    f.attr("node", shape="circle")

    for fila in range(graf.get_mida()):
        for columna in range(graf.get_mida()):
            if graf.get_graf().get_valor(fila, columna) != 0:
                f.edge(str(fila), str(columna), label=str(graf.get_graf().get_valor(fila, columna)))

    f.view()


def que_fer_amb_el_graf(graf):
    while True:
        print("\nQuè vols fer ara?\n (0) Tornar al menú principal\n (1) Veure la matriu adjacent\n "
              "(2) Veure el teu graf en format PDF\n (3) Veure si és connex\n (4) Aplicar l'algoritme de profunditat\n "
              "(5) Aplicar l'algoritme de Warshall\n (6) Aplicar l'algoritme de Prim")
        eleccio_subprograma = int(input("→ "))

        if eleccio_subprograma == 1:
            graf.mostrar_graf()
            time.sleep(2)

        elif eleccio_subprograma == 2:
            veure_graf(graf)

        elif eleccio_subprograma == 3:
            if subprogrames.es_connex(graf):
                print("Sí que és connex")
                time.sleep(2)

            else:
                print("No és connex")
                time.sleep(2)

        elif eleccio_subprograma == 4:
            print("Introdueix el vèrtex on vols començar:")
            print(graf.algoritme_profunditat(int(input("→ "))))
            time.sleep(2)

        elif eleccio_subprograma == 5:
            print(graf.algoritme_warshall().mostrar_graf())
            time.sleep(2)

        elif eleccio_subprograma == 6:
            print(graf.algoritme_prim())
            time.sleep(2)

        elif eleccio_subprograma == 0:
            print("Vols guardar el graf?\n (0) No\n (1) Sí")
            eleccio_subprograma = int(input("→ "))

            while True:
                if eleccio_subprograma == 0:
                    print("Tornant al menú principal...")
                    time.sleep(0.5)
                    break

                elif eleccio_subprograma == 1:
                    guardar_graf(graf)
                    print("Tornant al menu principal", end="")
                    time.sleep(0.5)
                    break

                else:
                    print("Si us plau, introdueix una opció vàlida")
                    time.sleep(0.5)

            break

        else:
            print("Si us plau, introdueix una opció vàlida")
            time.sleep(0.5)


if __name__ == "__main__":
    while True:
        print("\nQuè vols fer?\n (0) Sortir\n (1) Crear un graf\n (2) Carregar un graf d'un fitxer")
        eleccio = int(input("→ "))

        if eleccio == 1:
            print("Introdueix el nombre de vertexs:")
            graf_creat = classes.Graf(int(input("→ ")))
            print("Quantes arestes vols afegir al graf?")

            for i in range(int(input("→ "))):
                print("Introdueix el vèrtex de sortida:")
                sortida = int(input("→ "))
                print("Introdueix el vèrtex d'entrada:")
                entrada = int(input("→ "))
                print("Introdueix el pes de l'aresta:")
                pes = int(input("→ "))
                graf_creat.afegir_aresta(sortida, entrada, pes)

            que_fer_amb_el_graf(graf_creat)

        elif eleccio == 2:
            fitxers_grafs = glob.glob("grafs/*.txt")
            print("Selecciona el fitxer que vols carregar:")
            for i in range(len(fitxers_grafs)):
                print(f"({i + 1}) {fitxers_grafs[i][6:-4]}")

            graf_llegit = llegir_graf()

            que_fer_amb_el_graf(graf_llegit)

        elif eleccio == 0:
            print("Fins aviat!")
            break

        else:
            print("\nSi us plau, introdueix una opció vàlida")
            time.sleep(0.5)
