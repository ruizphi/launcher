# Francisco Javier Ruiz Gonzalez
# 3-D
# Programa 20: Obtener el total a pagar de n productos que tienen precio fijo
import tkinter as tk
from tkinter import messagebox
def total():
    cant = int(ent_cant.get())
    prec = float(ent_prec.get())
    _total = cant * prec
    messagebox.showinfo("Total", f"El total es ${str(_total)}")
def limpiar():
    ent_cant.delete(0, tk.END)
    ent_prec.delete(0, tk.END)
def salir():
    prg_salir = messagebox.askyesno("Salir?", "Estas seguro de que quieres salir? ")
    if prg_salir:
        ventana.destroy()
ventana = tk.Tk()
ventana.title("Tienda")
ventana.geometry("450x400")
ventana.config(bg="gray")
lbl_cant = tk.Label(text="Cantidad:", bg="gray", fg="white")
ent_cant = tk.Entry()
lbl_prec = tk.Label(text="Precio:", bg="gray", fg="white")
ent_prec = tk.Entry()
frm_botones = tk.Frame(ventana, bg="gray")
btn_total = tk.Button(frm_botones, text="Total", command=total, bg="blue",
                      fg="white")
btn_total.grid(row=0, column=1, padx=5)
btn_limp = tk.Button(frm_botones, text="Limpiar", command=limpiar,
                     bg="orange", fg="white")
btn_limp.grid(row=0, column=2, padx=5)
btn_cerr = tk.Button(frm_botones, text="Salir", command=salir,
                     bg="red", fg="white")
btn_cerr.grid(row=0, column=3, padx=5)
lbl_cant.place(x=120, y=30); ent_cant.place(x=180, y=30)
lbl_prec.place(x=120, y=70)
ent_prec.place(x=180, y=70)
frm_botones.place(x=150, y=130)
ventana.mainloop()
