class Matriu:  # No la faig servir perquè he substituït aquesta classe per les matrius de numpy

    # Classe matriu quadrada.
    # El constructor rep la mida de la matriu i en crea una de buida
    def __init__(self, n):
        self.__matriu = []
        self.__n = n

        for i in range(n):
            fila = [0] * n

            self.__matriu.append(fila)

    def modificar_valor(self, fila, columna, valor):

        if -1 < fila < self.__n and -1 < columna < self.__n:
            self.__matriu[fila][columna] = valor

    def get_valor(self, fila, columna):

        return self.__matriu[fila][columna]

    def get_matriu(self):
        return self.__matriu

    # Sobreescrivim la funció len de Python, aquest mètode retorna la mida de la matriu.
    def __len__(self):

        return self.__n

    def mostrar_per_pantalla(self):

        n = self.__n

        for i in range(n):
            for j in range(n):
                if self.__matriu[i][j] < 10:
                    print("0", end="")
                print(self.__matriu[i][j], end=" ")

            print("")

    def maxim(self):
        maxim = 0
        for fila in self.__matriu:
            for numero in fila:
                if numero > maxim:
                    maxim = numero
        return maxim

    def copia(self):
        copia = Matriu(self.__n)

        for i in range(copia.__n):
            for j in range(copia.__n):
                copia.__matriu[i][j] = self.__matriu[i][j]

        return copia

    def fer_identitat(self):
        for i in range(len(self.__matriu)):
            for j in range(len(self.__matriu[i])):
                if i != j:
                    self.__matriu[i][j] = 0
                else:
                    self.__matriu[i][j] = 1

    def __mul__(self, other):
        matriu_mult = Matriu(len(self.__matriu))

        for i in range(len(self.__matriu)):
            for j in range(len(self.__matriu)):
                for k in range(len(self.__matriu)):
                    matriu_mult.__matriu[i][j] += self.__matriu[i][k] * other.__matriu[k][j]

        return matriu_mult

    def __pow__(self, power, modulo=None):
        m = self.copia()

        if power > 0:
            for i in range(power):
                m *= self

        elif power == 0:
            m.fer_identitat()

        return m

    def __add__(self, other):
        matriu_suma = Matriu(len(self.__matriu))

        for i in range(len(self.__matriu)):
            for j in range(len(self.__matriu)):
                matriu_suma.__matriu[i][j] = self.__matriu[i][j] + other.__matriu[i][j]

        return matriu_suma