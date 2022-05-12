import classes
import subprogrames

if __name__ == "__main__":
    graf_test1 = classes.Graf(4)
    graf_test1.afegir_aresta(0, 1, 1)
    graf_test1.afegir_aresta(2, 1, 1)
    graf_test1.afegir_aresta(3, 1, 1)
    graf_test1.afegir_aresta(1, 3, 1)
    graf_test1.afegir_aresta(3, 3, 1)

    graf_test1.afegir_aresta(1, 0, 1)
    graf_test1.afegir_aresta(1, 2, 1)

    # graf_test1.mostrar_graf()
    # print(graf_test1.profunditat(2))
    print(f"Graf 1: {subprogrames.es_connex(graf_test1)}")

    graf_test2 = classes.Graf(4)
    graf_test2.afegir_aresta(0, 1, 1)
    graf_test2.afegir_aresta(1, 0, 1)
    graf_test2.afegir_aresta(1, 2, 1)
    graf_test2.afegir_aresta(2, 1, 1)
    graf_test2.afegir_aresta(0, 2, 1)
    graf_test2.afegir_aresta(2, 0, 1)
    graf_test2.afegir_aresta(2, 3, 1)
    graf_test2.afegir_aresta(3, 2, 1)

    # graf_test2.mostrar_graf()
    print(f"Graf 2: {subprogrames.es_connex(graf_test2)}")
