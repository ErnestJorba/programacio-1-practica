import classes
import subprogrames

if __name__ == "__main__":
    print("Benginguts! Aquesta és la pràctica de final de curs de l'Ernest Jorba Calafell, bona sort!")

    if int(input("Vols crear un graf? ")) == 1:

        graf = classes.Graf(int(input("Introdueix el nombre de vertexs: ")))
        while True:
            sortida = int(input("Introdueix el vertex de sortida: "))
            entrada = int(input("Introdueix el vertes d'entrada: "))
            pes = int(input("Introdueix el pes de l'aresta: "))
            graf.afegir_aresta(sortida, entrada, pes)
            if int(input("Vols continuar? ")) != 1:
                break
        graf.mostrar_graf()

        if int(input("Vols veure si és connex? ")) == 1:
            print(subprogrames.es_connex(graf))

        if int(input("Vols veure el resultat d'aplicar l'algorisme de profunditat a aquest graf? ")) == 1:
            print(graf.profunditat(int(input("Introdueix el vèrtex on vols començar: "))))

    else:
        print("Fins aviat!")
