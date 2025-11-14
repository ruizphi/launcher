# Francisco Javier Ruiz Gonzalez
# 3-D
# Programa 14: Configuraciones adicionales

from tkinter import Tk, Label # importamos Tk y el widget "Label"

ventana = Tk() # Creamos nuestra ventana
ventana.title("Francisco") # Damos titulo a la ventana
ventana.geometry("400x400") # Fijar un tamaño por defecto
ventana.resizable(False, False) # ancho, alto

lbl_msg = Label(text="\nHola, mundo!\n", bg="blue", fg="white",
                font=("Times", 15, "bold italic"))
lbl_msg.pack()

# ventana.destroy() # Cerrar la ventana
