import classes


def es_connex(graf):
    matriu_graf = graf.get_graf()
    for i in range(1, len(matriu_graf) + 1):
        matriu_graf += matriu_graf ** i

    matriu = matriu_graf.get_matriu()

    for i in range(len(matriu)):
        for j in range(len(matriu)):
            if matriu[i][j] == 0:
                return False

    return True


if __name__ == "__main__":
    print("Hello world!")
