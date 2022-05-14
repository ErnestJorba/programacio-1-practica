import classes


def es_connex(graf):  # Nota: només funciona pels grafs no dirigits!!
    matriu_graf = graf.get_graf()
    for i in range(len(matriu_graf)):
        matriu_graf += matriu_graf ** (i + 1)

    matriu = matriu_graf.get_matriu()

    for i in range(len(matriu)):
        for j in range(len(matriu)):
            if matriu[i][j] == 0:
                return False

    return True
