# Francisco Javier Ruiz Gonzalez
# 3-D
# Programa 18: Obtener el sueldo de un empleado usando messagebox
import tkinter as tk
from tkinter import messagebox
def pago():
    ht = int(ent_ht.get())
    sueldo_hora = float(ent_sh.get())
    total = sueldo_hora * ht
    messagebox.showinfo("LA NACIONAL", f"El pago al empleado es ${str(total)}")
def limpiar():
    ent_ht.delete(0, tk.END)
    ent_sh.delete(0, tk.END)
def salir():
    prg_salir = messagebox.askyesno("Salir?", "Estas seguro de que quieres salir? ")
    if prg_salir:
        ventana.destroy()
ventana = tk.Tk()
ventana.geometry("450x300")
ventana.title("Calcular sueldo de un empleado")
ventana.config(bg="gray")
ventana.resizable(False, False)

lbl_ht = tk.Label(text="Ingrese las horas trabajadas", bg="gray", fg="white")
ent_ht = tk.Entry()
lbl_sh = tk.Label(text="Ingrese el sueldo por hora", bg="gray", fg="white")
ent_sh = tk.Entry()
btn_calc = tk.Button(text="Calcular", font=("Verdana", 10), command=pago,
                     bg="blue", fg="white")
btn_limp = tk.Button(text="Limpiar", font=("Verdana", 10), command=limpiar,
                     bg="orange", fg="white")
btn_cerr = tk.Button(text=" Salir ", command=salir, font=("Verdana", 10),
                     bg="red", fg="white")
lbl_ht.place(x=40, y=110); ent_ht.place(x=200, y=110)
lbl_sh.place(x=40, y=150)
ent_sh.place(x=200, y=150)
btn_limp.place(x=350, y=130)
btn_calc.place(x=350, y=100)
btn_cerr.place(x=350, y=160)
ventana.mainloop()
