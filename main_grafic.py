import glob
import tkinter as tk
import tkinter.ttk as ttk
import graf


class Menu:
    def __init__(self, win):
        self.__sortir = tk.Button(win, text="Sortir", command=quit)
        self.__sortir.place(x=25, y=25)

        self.__crear_graf = tk.Button(win, text="Crear graf", command=self.crear_graf)
        self.__crear_graf.place(x=25, y=70)
        self.__numero_vertex_text = tk.Label(win, text="Número de vèrtexs")
        self.__numero_vertex_text.place(x=130, y=75)
        self.__ordre_nou_graf = tk.Entry()
        self.__ordre_nou_graf.place(x=270, y=75)

        self.__llegir = tk.Button(win, text="Llegir un graf d'un fitxer", command=self.llegir_graf)
        self.__llegir.place(x=25, y=120)

        self.__fitxers_grafs = []
        for element in glob.glob("grafs/*.txt"):
            self.__fitxers_grafs.append(element[6:-4])

        self.__escollir_graf = ttk.Combobox(win, values=self.__fitxers_grafs)
        self.__escollir_graf.place(x=225, y=125)

    def crear_graf(self):
        nou_graf_menu(int(self.__ordre_nou_graf.get()))

    def llegir_graf(self):
        graf_escollit = "grafs/" + self.__escollir_graf.get() + ".txt"

        with open(graf_escollit) as f:
            for line in f:
                fields = line.split()
                if len(fields) == 1:
                    graf_fitxer = graf.Graf(int(fields[0]))

                elif len(fields) == 3:
                    graf_fitxer.afegir_aresta(int(fields[0]), int(fields[1]), int(fields[2]))

        algoritmes_menu(graf_fitxer)


class CrearGraf:
    def __init__(self, win, n):
        self.__graf_creat = graf.Graf(n)
        self.__v1_text = tk.Label(win, text="Vèrtex sortida")
        self.__v2_text = tk.Label(win, text="Vèrtex entrada")
        self.__pes_text = tk.Label(win, text="Pes aresta")
        self.__afegir = tk.Button(win, text="Afegir aresta", command=self.afegir_aresta)
        self.__eliminar = tk.Button(win, text="Eliminar aresta", command=self.eliminar_aresta)
        self.__acabar = tk.Button(win, text="Acabar creació de graf", command=self.acabar)

        self.__v1 = tk.Entry(win)
        self.__v2 = tk.Entry(win)
        self.__pes = tk.Entry(win)

        self.__v1_text.place(x=25, y=25)
        self.__v1.place(x=125, y=25)
        self.__v2_text.place(x=25, y=75)
        self.__v2.place(x=125, y=75)
        self.__pes_text.place(x=25, y=125)
        self.__pes.place(x=125, y=125)
        self.__afegir.place(x=25, y=175)
        self.__eliminar.place(x=150, y=175)

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

    def eliminar_aresta(self):
        u = int(self.__v1.get())
        v = int(self.__v2.get())
        self.__graf_creat.eliminar_aresta(u, v)
        print("Aresta eliminada!\n")

    def acabar(self):
        algoritmes_menu(self.__graf_creat)


class Algoritmes:
    def __init__(self, win, graf_escollit):
        self.__tab_control = ttk.Notebook(win)
        self.__algoritmes = ttk.Frame(self.__tab_control)  # Sigui self.__algoritmes la pestanya pels algoritmes
        self.__modificar_graf = ttk.Frame(self.__tab_control)  # Sigui self.__modificar la pestanya on pots
        # canviar el graf
        self.__guardar = ttk.Frame(self.__tab_control)  # Sigui self.__guardar la pestanya on es pot guardar el graf
        self.__tab_control.add(self.__algoritmes, text="Algoritmes")
        self.__tab_control.add(self.__modificar_graf, text="Modificar el graf")
        self.__tab_control.add(self.__guardar, text="Guardar el graf")

        self.__graf = graf_escollit

        #
        # Pàgina d'algoritmes
        #

        self.__menu = tk.Button(self.__algoritmes, text="Tornar al menú principal", command=menu_principal)
        self.__menu.place(x=25, y=25)

        self.__matriu = tk.Button(self.__algoritmes, text="Veure la matriu d'adjacència del graf", command=self.matriu)
        self.__matriu.place(x=25, y=75)

        self.__veure_graf = tk.Button(self.__algoritmes, text="Veure el graf en format PDF", command=self.pdf)
        self.__veure_graf.place(x=25, y=125)

        self.__connex = tk.Button(self.__algoritmes, text="Veure si és connex", command=self.connex)
        self.__connex.place(x=25, y=175)

        self.__v1_text = tk.Label(self.__algoritmes, text="Vèrtex inicial")
        self.__v1_text.place(x=275, y=230)
        self.__vertex_profunditat = tk.Entry(self.__algoritmes)
        self.__vertex_profunditat.place(x=375, y=230)
        self.__profunditat = tk.Button(self.__algoritmes, text="Aplicar l'algoritme de profunditat",
                                       command=self.profunditat)
        self.__profunditat.place(x=25, y=225)

        self.__warshall = tk.Button(self.__algoritmes, text="Aplicar l'algoritme de Warshall", command=self.warshall)
        self.__warshall.place(x=25, y=275)

        self.__prim = tk.Button(self.__algoritmes, text="Aplicar l'algoritme de Prim", command=self.prim)
        self.__prim.place(x=25, y=325)
        self.__minimal = tk.Button(self.__algoritmes, text="Veure l'arbre minimal", command=self.arbre_minimal)
        self.__minimal.place(x=225, y=325)

        #
        # Pàgina d'editar el graf
        #

        self.__v1_text = tk.Label(self.__modificar_graf, text="Vèrtex sortida")
        self.__v2_text = tk.Label(self.__modificar_graf, text="Vèrtex entrada")
        self.__pes_text = tk.Label(self.__modificar_graf, text="Pes aresta")
        self.__nota_1 = tk.Label(self.__modificar_graf, text="Nota: Si has carregat el graf d'un fitxer, el fitxer no"
                                                             " es modificarà")
        self.__afegir = tk.Button(self.__modificar_graf, text="Afegir aresta", command=self.afegir_aresta)
        self.__eliminar = tk.Button(self.__modificar_graf, text="Eliminar aresta", command=self.eliminar_aresta)

        self.__v1 = tk.Entry(self.__modificar_graf)
        self.__v2 = tk.Entry(self.__modificar_graf)
        self.__pes = tk.Entry(self.__modificar_graf)

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

        self.__nom_fitxer_text = tk.Label(self.__guardar, text="Nom del fitxer (sense extensió):")
        self.__nom_fitxer = tk.Entry(self.__guardar)
        self.__guardar_fitxer = tk.Button(self.__guardar, text="Guardar", command=self.guardar)
        self.__nota_2 = tk.Label(self.__guardar, text="Nota: Si ja existeix un fitxer amb el nom que has introduït,\nes"
                                                      " sobreescriurà i el perdràs")

        self.__nom_fitxer_text.place(x=25, y=25)
        self.__nom_fitxer.place(x=25, y=75)
        self.__guardar_fitxer.place(x=200, y=70)
        self.__nota_2.place(x=25, y=125)

        self.__tab_control.pack(expand=1, fill="both")  # Sincerament, desconec la raó per la qual això funciona però
        # és el que vaig trobar i, sense aquesta línia, no es poden veure les pestanyes correctament

    def matriu(self):  # No sé per què, però no puc assignar certes comandes directament el botó (crec que són només
        # les que reben un paràmetre), però per fer-ho tot uniforme ho he acabat fent tot amb mètodes i, des del botó,
        # cridar al mètode corresponent
        self.__graf.mostrar_graf()
        print("")

    def pdf(self):
        self.__graf.veure_graf()

    def connex(self):
        if self.__graf.es_connex():
            print("Sí que és connex\n")

        else:
            print("No és connex\n")

    def profunditat(self):
        v_0 = int(self.__vertex_profunditat.get())  # Obtenim el valor que ha introduït l'usuari en l'Entry amb .get()
        print(self.__graf.algoritme_profunditat(v_0))
        print("")  # Al final de cada mètode afegeixo aquesta línia perquè trobo que, si tots els prints fossin
        # seguits, no es podrien distingir gaire i quedaria tot massa junt

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

        if p != 0:
            print("Aresta afegida!\n")

        else:
            print("Aresta eliminada!\n")

    def eliminar_aresta(self):
        u = int(self.__v1.get())
        v = int(self.__v2.get())
        self.__graf.eliminar_aresta(u, v)
        print("Aresta eliminada!\n")

    def guardar(self):
        self.__graf.guardar_graf(self.__nom_fitxer.get())
        print("Graf guardat!\n")

    def arbre_minimal(self):
        self.__graf.veure_arbre_minimal()


def menu_principal():
    global root

    for widget in root.winfo_children():  # Per evitar que en canviar de menú surtin els widgets del menú anterior,
        # hem d'eliminar tots els existents per sobreescriure el que necessitem
        widget.destroy()

    Menu(root)


def nou_graf_menu(ordre):
    global root

    for widget in root.winfo_children():  # Mateix raonament que abans
        widget.destroy()

    CrearGraf(root, ordre)


def algoritmes_menu(graf_escollit):
    global root

    for widget in root.winfo_children():  # Mateix raonament que abans
        widget.destroy()

    Algoritmes(root, graf_escollit)


if __name__ == "__main__":
    root = tk.Tk()  # Creo una finestra principal (root) on vaig afegint o eliminant tots els "widgets" que necessito
    root.title("Pràctica grafs")
    root.geometry("600x400+10+10")
    menu_principal()

    root.mainloop()
