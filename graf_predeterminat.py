import classes

if __name__ == "__main__":
    graf_apunts = classes.Graf(4)
    graf_apunts.afegir_aresta(0, 1, 1)
    graf_apunts.afegir_aresta(2, 1, 1)
    graf_apunts.afegir_aresta(3, 1, 1)
    graf_apunts.afegir_aresta(1, 3, 1)
    graf_apunts.afegir_aresta(3, 3, 1)
    graf_apunts.mostrar_graf()
    print(graf_apunts.profunditat(0))
