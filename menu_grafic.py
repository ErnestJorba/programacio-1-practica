import tkinter
from tkinter import ttk


root = tkinter.Tk()

caixatext = ttk.Entry(root)
caixatext.pack()

etiqueta = ttk.Label(root)
etiqueta.pack()


def text_dintre_caixa():
    vertex_sortida = caixatext.get()
    etiqueta["text"] = vertex_sortida
    vertex_entrada = caixatext.get()
    etiqueta["text"] = vertex_entrada
    aresta_pes = caixatext.get()
    etiqueta["text"] = aresta_pes
    print(vertex_sortida, vertex_entrada, aresta_pes)


boto1 = ttk.Button(root, text="Afegir", command=text_dintre_caixa)
boto1.pack()

root.mainloop()

"""
root = tkinter.Tk()

root.title("Pràctica final de curs")

tkinter.Label(root, text="tk").pack()
ttk.Label(root, text="ttk").pack()

root.mainloop()
"""
