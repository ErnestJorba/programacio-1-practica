import glob
import time
import graf


def llegir_graf():
    fitxers = glob.glob("grafs/*.txt")

    with open(fitxers[int(input("→ ")) - 1]) as f:
        for line in f:
            fields = line.split()
            if len(fields) == 1:
                graf_fitxer = graf.Graf(int(fields[0]))
            elif len(fields) == 3:  # Com que la primera línia de tots els fitxers sempre és la de longitud 1, mai ens
                # trobarem en el cas on intentem afegir una aresta a un graf inexistent
                graf_fitxer.afegir_aresta(int(fields[0]), int(fields[1]), int(fields[2]))
            else:
                print("Hi ha hagut un error llegint el fitxer. Si us plau, mireu que tot sigui correcte")
                quit()

    return graf_fitxer


def que_fer_amb_el_graf(graf_escollit):
    while True:
        print("\nQuè vols fer ara?\n (0) Tornar al menú principal\n (1) Veure la matriu adjacent\n "
              "(2) Veure el teu graf en format PDF\n (3) Veure si és connex\n (4) Aplicar l'algoritme de profunditat\n "
              "(5) Aplicar l'algoritme de Warshall\n (6) Aplicar l'algoritme de Prim")
        eleccio = int(input("→ "))

        if eleccio == 1:
            graf_escollit.mostrar_graf()
            time.sleep(2)

        elif eleccio == 2:
            graf_escollit.veure_graf()

        elif eleccio == 3:
            if graf_escollit.es_connex():
                print("Sí que és connex")
                time.sleep(2)

            else:
                print("No és connex")
                time.sleep(2)

        elif eleccio == 4:
            print("Introdueix el vèrtex on vols començar:")
            print(graf_escollit.algoritme_profunditat(int(input("→ "))))
            time.sleep(2)

        elif eleccio == 5:
            graf_escollit.algoritme_warshall().mostrar_graf()
            time.sleep(2)

        elif eleccio == 6:
            print(graf_escollit.algoritme_prim())
            time.sleep(2)

        elif eleccio == 0:
            print("Vols guardar el graf?\n (0) No\n (1) Sí")
            eleccio = int(input("→ "))

            while True:
                if eleccio == 0:
                    print("Tornant al menú principal...")
                    time.sleep(0.5)
                    break

                elif eleccio == 1:
                    print("Introdueix el nom que li vols posar al fitxer (sense extensió):")
                    nom = input("→ ")
                    graf_escollit.guardar_graf(nom)
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
