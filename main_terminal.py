import glob
import time
import graf
import subprogrames

if __name__ == "__main__":
    while True:
        print("Atenció!! Pot ser que faltin algunes opcions en aquest menú.\nAixò és degut a que, una vegada ja vaig "
              "fer el menú gràfic, em vaig centrar en afegir les opcions noves allà i no en actualitzar aquest menú.")
        print("\nQuè vols fer?\n (0) Sortir\n (1) Crear un graf\n (2) Carregar un graf d'un fitxer")
        eleccio = int(input("→ "))

        if eleccio == 1:
            print("Introdueix el nombre de vèrtexs:")
            graf_creat = graf.Graf(int(input("→ ")))
            print("Quantes arestes vols afegir al graf?")

            for i in range(int(input("→ "))):
                print("Introdueix el vèrtex de sortida:")
                sortida = int(input("→ "))
                print("Introdueix el vèrtex d'entrada:")
                entrada = int(input("→ "))
                print("Introdueix el pes de l'aresta:")
                pes = int(input("→ "))
                graf_creat.afegir_aresta(sortida, entrada, pes)

            subprogrames.que_fer_amb_el_graf(graf_creat)

        elif eleccio == 2:
            fitxers_grafs = glob.glob("grafs/*.txt")
            print("Selecciona el fitxer que vols carregar:")

            for i in range(len(fitxers_grafs)):
                print(f"({i + 1}) {fitxers_grafs[i][6:-4]}")

            graf_llegit = subprogrames.llegir_graf()

            subprogrames.que_fer_amb_el_graf(graf_llegit)

        elif eleccio == 0:
            print("Fins aviat!")
            break

        else:
            print("\nSi us plau, introdueix una opció vàlida")
            time.sleep(0.5)
