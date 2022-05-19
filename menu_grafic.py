import glob
from tkinter import *
from tkinter.ttk import Combobox

import classes
import subprogrames


class Menu:
    def __init__(self, win):
        self.__sortir = Button(win, text="Sortir", command=quit)
        self.__sortir.place(x=25, y=25)

        self.__crear_graf = Button(win, text="Crear graf", command=self.crear_graf)
        self.__crear_graf.place(x=25, y=70)
        self.__lbl1 = Label(win, text="Número de vèrtexs")
        self.__lbl1.place(x=125, y=75)
        self.__mida_nou_graf = Entry()
        self.__mida_nou_graf.place(x=250, y=75)

        self.__llegir = Button(win, text="Llegir un graf d'un fitxer", command=self.llegir_graf)
        self.__llegir.place(x=25, y=120)

        self.__fitxers_grafs = []
        for element in glob.glob("grafs/*.txt"):
            self.__fitxers_grafs.append(element[6:-4])

        self.__escollir_graf = Combobox(win, values=self.__fitxers_grafs)
        self.__escollir_graf.place(x=200, y=125)

    def crear_graf(self):
        nou_graf_menu(int(self.__mida_nou_graf.get()))

    def llegir_graf(self):
        graf_escollit = "grafs/" + self.__escollir_graf.get() + ".txt"

        with open(graf_escollit) as f:
            for line in f:
                fields = line.split()
                if len(fields) == 1:
                    graf_fitxer = classes.Graf(int(fields[0]))
                elif len(fields) == 3:
                    graf_fitxer.afegir_aresta(int(fields[0]), int(fields[1]), int(fields[2]))

        que_fer_amb_el_graf_menu(graf_fitxer)


class CrearGraf:
    def __init__(self, win, n):
        self.__graf_creat = classes.Graf(n)
        self.__lbl1 = Label(win, text="Vèrtex sortida")
        self.__lbl2 = Label(win, text="Vèrtex entrada")
        self.__lbl3 = Label(win, text="Pes aresta")
        self.__btn1 = Button(win, text="Afegir aresta")
        self.__b1 = Button(win, text="Afegir aresta", command=self.afegir_aresta)

        self.__t1 = Entry()
        self.__t2 = Entry()
        self.__t3 = Entry()

        self.__lbl1.place(x=25, y=25)
        self.__t1.place(x=125, y=25)
        self.__lbl2.place(x=25, y=75)
        self.__t2.place(x=125, y=75)
        self.__lbl3.place(x=25, y=125)
        self.__t3.place(x=125, y=125)
        self.__b1.place(x=25, y=175)

        self.__acabar = Button(win, text="Acabar creació de graf", command=self.acabar)
        self.__acabar.place(x=25, y=250)

    def afegir_aresta(self):
        u = int(self.__t1.get())
        v = int(self.__t2.get())
        p = int(self.__t3.get())
        self.__graf_creat.afegir_aresta(u, v, p)
        print("Aresta afegida!")

    def acabar(self):
        que_fer_amb_el_graf_menu(self.__graf_creat)


class QueFer:
    def __init__(self, win, graf):
        self.__graf = graf

        self.__menu = Button(win, text="Tornar al menú principal", command=main)
        self.__menu.place(x=25, y=25)

        self.__matriu = Button(win, text="Veure la matriu d'adjacencia del graf", command=self.matriu)
        self.__matriu.place(x=25, y=75)

        self.__veure_graf = Button(win, text="Veure el graf en format PDF", command=self.pdf)
        self.__veure_graf.place(x=25, y=125)

        self.__connex = Button(win, text="Veure si és connex", command=self.connex)
        self.__connex.place(x=25, y=175)

        self.__lbl1 = Label(win, text="Vertex inicial")
        self.__lbl1.place(x=25, y=225)
        self.__vertex_profunditat = Entry()
        self.__vertex_profunditat.place(x=150, y=225)
        self.__profunditat = Button(win, text="Aplicar l'algoritme de profunditat", command=self.profunditat)
        self.__profunditat.place(x=325, y=220)

        self.__warshall = Button(win, text="Aplicar l'algoritme de Warshall", command=self.warshall)
        self.__warshall.place(x=25, y=275)

        self.__prim = Button(win, text="Aplicar l'algoritme de Prim", command=self.prim)
        self.__prim.place(x=25, y=325)

    def matriu(self):
        self.__graf.mostrar_graf()

    def pdf(self):
        subprogrames.veure_graf(self.__graf)

    def connex(self):
        print(subprogrames.es_connex(self.__graf))

    def profunditat(self):
        v_0 = int(self.__vertex_profunditat.get())
        print(self.__graf.algoritme_profunditat(v_0))

    def warshall(self):
        print(self.__graf.algoritme_warshall())

    def prim(self):
        print(self.__graf.algoritme_prim())


def main():
    root = Tk()
    Menu(root)
    root.title('Menú principal')
    root.geometry("600x400+10+10")

    root.mainloop()


def nou_graf_menu(mida):
    creacio_graf = Tk()
    graf_creat = CrearGraf(creacio_graf, mida)
    creacio_graf.title('Creació graf')
    creacio_graf.geometry("400x300+10+10")

    creacio_graf.mainloop()


def que_fer_amb_el_graf_menu(graf):
    menu_que_fer = Tk()
    opcions = QueFer(menu_que_fer, graf)
    menu_que_fer.title('Què vols fer amb el graf?')
    menu_que_fer.geometry("600x400+10+10")

    menu_que_fer.mainloop()


if __name__ == "__main__":
    main()
