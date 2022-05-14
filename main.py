import classes
import subprogrames

if __name__ == "__main__":
    print("Benginguts! Aquesta és la pràctica de final de curs de l'Ernest Jorba Calafell, bona sort!")
    print("Què vols fer?\n (1) Crear un graf\n (2) Carregar un graf d'un fitxer")
    eleccio = int(input("→ "))

    if eleccio == 1:
        print("Introdueix el nombre de vertexs")
        graf = classes.Graf(int(input("→ ")))
        print("Quantes arestes vols afegir al graf? ")

        for i in range(int(input("→ "))):
            print("Introdueix el vèrtex de sortida:")
            sortida = int(input("→ "))
            print("Introdueix el vèrtex d'entrada:")
            entrada = int(input("→ "))
            print("Introdueix el pes de l'aresta:")
            pes = int(input("→ "))
            graf.afegir_aresta(sortida, entrada, pes)

        while True:
            print("\nQuè vols fer ara?\n (0) Sortir\n (1) Veure el meu graf\n (2) Veure si és connex\n (3) Aplicar "
                  "l'algorisme de profunditat\n (4) Aplicar l'algorisme de prim\n (5) Aplicar l'algorisme de Warhsall")
            eleccio = int(input("→ "))

            if eleccio == 1:
                print("")
                graf.mostrar_graf()
                print("")

            elif eleccio == 2:
                if subprogrames.es_connex(graf):
                    print("Sí que és connex")
                else:
                    print("No és connex")

            elif eleccio == 3:
                print("Introdueix el vèrtex on vols començar:")
                print(graf.profunditat(int(input("→ "))))

            elif eleccio == 4:
                print(graf.algorisme_prim())

            elif eleccio == 5:
                graf.algorisme_warshall().mostrar_graf()

            elif eleccio == 0:
                print("Vols guardar el graf?\n (0) No\n (1) Sí")
                eleccio = int(input("→ "))

                if eleccio == 0:
                    print("no guardar")

                elif eleccio == 1:
                    print("guardar")

                print("Fins aviat!")
                break

    elif eleccio == 2:
        print("carregar fitxers")

    else:
        print("Fins aviat!")
