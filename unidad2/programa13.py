# Francisco Javier Ruiz Gonzalez
# 3-D
# Programa 13: Mi primera interfaz en Tkinter

from tkinter import Tk, Label # importamos Tk y el widget "Label"

ventana = Tk() # Creamos nuestra ventana

lbl_hola = Label(text="\nHola, mundo!\n")
lbl_yo = Label(text="Soy Francisco\n")
lbl_metas = Label(text="Quiero ser un gran programador\n")

# Visualizarlo
lbl_hola.pack()
lbl_yo.pack()
lbl_metas.pack()
