# Francisco Javier Ruiz Gonzalez
# 3-D
# Programa 19: Obtener el pago de un envio donde el envio nacional es de $50
# y el envio internacional es de $90
import tkinter as tk
from tkinter import messagebox
def calcular_envio():
    km = int(ent_km.get())
    nacional = messagebox.askyesno("Nacional o Internacional", "¿El tipo de envío es nacional?")
    if nacional:
        total = 50 * km
        messagebox.showinfo("Total nacional", f"El total a pagar por el envío es: {total}")
    else:
        total = 90 * km
        messagebox.showinfo("Total internacional", f"El total a pagar por el envío es: {total}")
def limpiar():
    ent_km.delete(0, tk.END)
def salir():
    prg_salir = messagebox.askyesno("Salir?", "Estas seguro de que quieres salir? ")
    if prg_salir:
        ventana.destroy()
ventana = tk.Tk()
ventana.title("Calculadora de Envío")
ventana.geometry("450x400")
ventana.config(bg="gray")
lbl_km = tk.Label(text="Ingrese los kilómetros recorridos:", bg="gray", fg="white")
ent_km = tk.Entry()
btn_calc = tk.Button(text="Calcular", command=calcular_envio, bg="blue", fg="white")
btn_limp = tk.Button(text="Limpiar", command=limpiar, bg="orange", fg="white")
btn_cerr = tk.Button(text=" Salir ", command=salir, bg="red", fg="white")

lbl_km.place(x=20, y=175)
ent_km.place(x=200, y=175)
btn_limp.place(x=350, y=170)
btn_calc.place(x=350, y=140)
btn_cerr.place(x=350, y=200)

ventana.mainloop()
