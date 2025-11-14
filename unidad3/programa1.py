# Francisco Javier Ruiz Gonzalez
# 3-D
# Programa 1: Introduccion a "Listbox"

import tkinter as tk

ventana = tk.Tk()
ventana.title("Lista en Tk")
ventana.geometry("300x300")

lbx_op = tk.Listbox()
lbx_op.insert(0, "Python")
lbx_op.insert(1, "Nombre")
lbx_op.insert(2, "Grupo")
lbx_op.insert(3, "Turno")

lbx_op.pack()
ventana.mainloop()
