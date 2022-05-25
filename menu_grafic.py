import glob
from tkinter import Tk, Button, Label, Entry
from tkinter.ttk import Combobox, Frame, Notebook

import classes
import subprogrames


class Menu:
    def __init__(self, win):
        self.__sortir = Button(win, text="Sortir", command=quit)
        self.__sortir.place(x=25, y=25)

        self.__crear_graf = Button(win, text="Crear graf", command=self.crear_graf)
        self.__crear_graf.place(x=25, y=70)
        self.__numero_vertex_text = Label(win, text="Número de vèrtexs")
        self.__numero_vertex_text.place(x=130, y=75)
        self.__mida_nou_graf = Entry()
        self.__mida_nou_graf.place(x=270, y=75)

        self.__llegir = Button(win, text="Llegir un graf d'un fitxer", command=self.llegir_graf)
        self.__llegir.place(x=25, y=120)

        self.__fitxers_grafs = []
        for element in glob.glob("grafs/*.txt"):
            self.__fitxers_grafs.append(element[6:-4])

        self.__escollir_graf = Combobox(win, values=self.__fitxers_grafs)
        self.__escollir_graf.place(x=225, y=125)

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

        algoritmes_menu(graf_fitxer)


class CrearGraf:
    def __init__(self, win, n):
        self.__graf_creat = classes.Graf(n)
        self.__v1_text = Label(win, text="Vèrtex sortida")
        self.__v2_text = Label(win, text="Vèrtex entrada")
        self.__pes_text = Label(win, text="Pes aresta")
        self.__afegir = Button(win, text="Afegir aresta", command=self.afegir_aresta)
        self.__acabar = Button(win, text="Acabar creació de graf", command=self.acabar)

        self.__v1 = Entry(win)
        self.__v2 = Entry(win)
        self.__pes = Entry(win)

        self.__v1_text.place(x=25, y=25)
        self.__v1.place(x=125, y=25)
        self.__v2_text.place(x=25, y=75)
        self.__v2.place(x=125, y=75)
        self.__pes_text.place(x=25, y=125)
        self.__pes.place(x=125, y=125)
        self.__afegir.place(x=25, y=175)

        self.__acabar.place(x=25, y=225)

    def afegir_aresta(self):
        u = int(self.__v1.get())
        v = int(self.__v2.get())
        p = int(self.__pes.get())
        self.__graf_creat.afegir_aresta(u, v, p)

        if p != 0:
            print("Aresta afegida!")

        else:
            print("Aresta eliminada!")

    def acabar(self):
        algoritmes_menu(self.__graf_creat)


class Algoritmes:
    def __init__(self, win, graf):
        self.__tab_control = Notebook(win)
        self.__algoritmes = Frame(self.__tab_control)
        self.__modificar_graf = Frame(self.__tab_control)
        self.__guardar = Frame(self.__tab_control)
        self.__tab_control.add(self.__algoritmes, text="Algoritmes")
        self.__tab_control.add(self.__modificar_graf, text="Modificar el graf")
        self.__tab_control.add(self.__guardar, text="Guardar el graf")

        self.__graf = graf

        #
        # Pàgina d'algoritmes
        #

        self.__menu = Button(self.__algoritmes, text="Tornar al menú principal", command=menu_principal)
        self.__menu.place(x=25, y=25)

        self.__matriu = Button(self.__algoritmes, text="Veure la matriu d'adjacencia del graf", command=self.matriu)
        self.__matriu.place(x=25, y=75)

        self.__veure_graf = Button(self.__algoritmes, text="Veure el graf en format PDF", command=self.pdf)
        self.__veure_graf.place(x=25, y=125)

        self.__connex = Button(self.__algoritmes, text="Veure si és connex", command=self.connex)
        self.__connex.place(x=25, y=175)

        self.__v1_text = Label(self.__algoritmes, text="Vèrtex inicial")
        self.__v1_text.place(x=275, y=230)
        self.__vertex_profunditat = Entry(self.__algoritmes)
        self.__vertex_profunditat.place(x=375, y=230)
        self.__profunditat = Button(self.__algoritmes, text="Aplicar l'algoritme de profunditat",
                                    command=self.profunditat)
        self.__profunditat.place(x=25, y=225)

        self.__warshall = Button(self.__algoritmes, text="Aplicar l'algoritme de Warshall", command=self.warshall)
        self.__warshall.place(x=25, y=275)

        self.__prim = Button(self.__algoritmes, text="Aplicar l'algoritme de Prim", command=self.prim)
        self.__prim.place(x=25, y=325)
        self.__minimal = Button(self.__algoritmes, text="Veure l'arbre minimal", command=self.arbre_minimal)
        self.__minimal.place(x=225, y=325)

        #
        # Pàgina d'editar el graf
        #

        self.__v1_text = Label(self.__modificar_graf, text="Vèrtex sortida")
        self.__v2_text = Label(self.__modificar_graf, text="Vèrtex entrada")
        self.__pes_text = Label(self.__modificar_graf, text="Pes aresta")
        self.__nota_1 = Label(self.__modificar_graf, text="Nota: Si has carregat el graf d'un fitxer, el fitxer no es"
                                                          " modificarà")
        self.__afegir = Button(self.__modificar_graf, text="Afegir aresta", command=self.afegir_aresta)
        self.__eliminar = Button(self.__modificar_graf, text="Eliminar aresta", command=self.eliminar_aresta)

        self.__v1 = Entry(self.__modificar_graf)
        self.__v2 = Entry(self.__modificar_graf)
        self.__pes = Entry(self.__modificar_graf)

        self.__v1_text.place(x=25, y=25)
        self.__v1.place(x=135, y=25)
        self.__v2_text.place(x=25, y=75)
        self.__v2.place(x=135, y=75)
        self.__pes_text.place(x=25, y=125)
        self.__pes.place(x=135, y=125)
        self.__afegir.place(x=25, y=175)
        self.__eliminar.place(x=150, y=175)
        self.__nota_1.place(x=25, y=215)

        #
        # Pàgina de guardar el graf
        #

        self.__nom_fitxer_text = Label(self.__guardar, text="Nom del fitxer (sense extensió):")
        self.__nom_fitxer = Entry(self.__guardar)
        self.__guardar_fitxer = Button(self.__guardar, text="Guardar", command=self.guardar)
        self.__nota_2 = Label(self.__guardar, text="Nota: Si ja existeix un fitxer amb el nom que has introduït,\nes"
                                                   " sobreescriurà i el perderàs")

        self.__nom_fitxer_text.place(x=25, y=25)
        self.__nom_fitxer.place(x=25, y=75)
        self.__guardar_fitxer.place(x=200, y=70)
        self.__nota_2.place(x=25, y=125)

        self.__tab_control.pack(expand=1, fill="both")

    def matriu(self):
        self.__graf.mostrar_graf()
        print("")

    def pdf(self):
        subprogrames.veure_graf(self.__graf)

    def connex(self):
        if subprogrames.es_connex(self.__graf):
            print("Sí que és connex\n")

        else:
            print("No és connex\n")

    def profunditat(self):
        v_0 = int(self.__vertex_profunditat.get())
        print(self.__graf.algoritme_profunditat(v_0))
        print("")

    def warshall(self):
        self.__graf.algoritme_warshall().mostrar_graf()
        print("")

    def prim(self):
        print(self.__graf.algoritme_prim())
        print("")

    def afegir_aresta(self):
        u = int(self.__v1.get())
        v = int(self.__v2.get())
        p = int(self.__pes.get())
        self.__graf.afegir_aresta(u, v, p)
        print("Aresta afegida!")

    def eliminar_aresta(self):
        u = int(self.__v1.get())
        v = int(self.__v2.get())
        self.__graf.afegir_aresta(u, v, 0)
        print("Aresta eliminada!")

    def guardar(self):
        subprogrames.guardar_graf(self.__graf, self.__nom_fitxer.get())
        print("Graf guardat!")

    def arbre_minimal(self):
        self.__graf.veure_arbre_minimal()


def menu_principal():
    global root

    for widget in root.winfo_children():
        widget.destroy()

    Menu(root)


def nou_graf_menu(mida):
    global root

    for widget in root.winfo_children():
        widget.destroy()

    CrearGraf(root, mida)


def algoritmes_menu(graf):
    global root

    for widget in root.winfo_children():
        widget.destroy()

    Algoritmes(root, graf)


if __name__ == "__main__":
    root = Tk()
    root.title("Pràctica grafs")
    root.geometry("600x400+10+10")
    menu_principal()

    root.mainloop()
