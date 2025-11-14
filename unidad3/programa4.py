def ejecutar():
    seleccion = []
    if var_colora.get():
        seleccion.append("Azul")
    if var_colorb.get():
        seleccion.append("Blanco")
    if var_colorr.get():
        seleccion.append("Rojo")
    if var_colorn.get():
        seleccion.append("Negro")
    if seleccion:
        messagebox.showinfo("Colores seleccionados", f"Tus colores favoritos son: {', '.join(seleccion)}")
    else:
        messagebox.showinfo("Colores seleccionados", "No seleccionaste ningun color")

import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.geometry("250x200")
ventana.title("Checkbutton")
ventana.config(bg="gray")

lbl_color = tk.Label(text="Selecciona tus colores favoritos: ", bg="gray", fg="white")

# Variables de control de los Checkbuttons
var_colora = tk.BooleanVar()
var_colorb = tk.BooleanVar()
var_colorr = tk.BooleanVar()
var_colorn = tk.BooleanVar()

# Creacion de los Checkbuttons
chb_colora = tk.Checkbutton(text="Azul", variable=var_colora)
chb_colorb = tk.Checkbutton(text="Blanco", variable=var_colorb)
chb_colorr = tk.Checkbutton(text="Rojo", variable=var_colorr)
chb_colorn = tk.Checkbutton(text="Negro", variable=var_colorn)

btn_fav = tk.Button(text="Ejecutar", command=ejecutar, bg="blue", fg="white")

lbl_color.pack()
chb_colora.place(x=100, y=20)
chb_colorb.place(x=100, y=40)
chb_colorr.place(x=100, y=60)
chb_colorn.place(x=100, y=80)
btn_fav.place(x=100, y=120)

ventana.mainloop()
