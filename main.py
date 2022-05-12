import classes

if __name__ == "__main__":
    if int(input("Vols crear un graf? ")) == 1:

        graf = classes.Graf(int(input("Introdueix el nombre de vertexs: ")))
        while True:
            sortida = int(input("Introdueix el vertex de sortida: "))
            entrada = int(input("Introdueix el vertes d'entrada: "))
            pes = int(input("Introdueix el pes de l'aresta: "))
            graf.afegir_aresta(sortida, entrada, pes)
            if int(input("Vols continuar? ")) == 0:
                break
        graf.mostrar_graf()

    else:
        print("Fins aviat!")
