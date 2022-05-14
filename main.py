import classes
import subprogrames

if __name__ == "__main__":
    print("Benginguts! Aquesta és la pràctica de final de curs de l'Ernest Jorba Calafell, bona sort!")
    print("Vols grear un graf?")
    if int(input("→ ")) == 1:

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

        print("Vols veure si és connex?")
        if int(input("→ ")) == 1:
            print(subprogrames.es_connex(graf))

        print("Vols veure el resultat d'aplicar l'algorisme de profunditat a aquest graf?")
        if int(input("→ ")) == 1:
            print("Introdueix el vèrtex on vols començar:")
            print(graf.profunditat(int(input("→ "))))

    else:
        print("Fins aviat!")
