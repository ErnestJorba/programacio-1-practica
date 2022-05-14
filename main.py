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

        graf.mostrar_graf()

        while True:
            print("Què vols fer ara?\n (0) Sortir\n (1) Veure si és connex\n (2) Aplicar l'algorisme de profunditat\n "
                  "(3) Aplicar l'algorisme de prim")
            eleccio = int(input("→ "))

            if eleccio == 1:
                print(subprogrames.es_connex(graf))

            elif eleccio == 2:
                print("Introdueix el vèrtex on vols començar:")
                print(graf.profunditat(int(input("→ "))))

            elif eleccio == 3:
                print(graf.prim())

            elif eleccio == 0:
                print("Fins aviat!")
                break

    elif eleccio == 2:
        print("carregar fitxers")

    else:
        print("Fins aviat!")
