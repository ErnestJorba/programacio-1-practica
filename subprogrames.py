import graphviz
import glob
import classes


def es_connex(graf):
    matriu_graf = graf.get_graf()
    for i in range(len(matriu_graf)):
        matriu_graf += matriu_graf ** (i + 1)

    matriu = matriu_graf.get_matriu()

    for i in range(len(matriu)):
        for j in range(len(matriu)):
            if matriu[i][j] == 0:
                return False

    return True


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
                    guardar_graf(graf)
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
