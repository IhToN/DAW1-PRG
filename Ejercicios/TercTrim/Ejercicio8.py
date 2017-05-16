"""
    Hacer cochinadas con TkInter
        Crear una ventana con tres etiquetas
"""

import tkinter

root = tkinter.Tk()  # Ventana raíz de la app básica

lbl = tkinter.Label(root, text="Ke pasa premoh!")
lbl.grid(row=0, column=1)
lbl = tkinter.Label(root, text="Zoi otra estiketa!")
lbl.grid(row=3, column=2)
lbl = tkinter.Label(root, text="Dame un lerito, no?")
lbl.grid(row=2, column=3)

btn = tkinter.Button(root, text="PO TE RAHO")
btn.grid(row=4, column=2)

root.mainloop()
