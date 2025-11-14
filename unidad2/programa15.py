# Francisco Javier Ruiz Gonzalez
# 3-D
# Programa 15: Suma de dos numeros con Tkinter

import tkinter as tk

def sumar():
    n1 = int(ent_n1.get())
    n2 = int(ent_n2.get())
    sumar = n1 + n2
    lbl_sum.config(text=f"Resultado: {str(sumar)}")

def cerrar():
    ventana.destroy()

ventana = tk.Tk()
ventana.title("Suma de dos numeros")
ventana.geometry("500x300")
ventana.resizable(False, False)

lbl_n1 = tk.Label(text="\nIngrese el primer numero:")
ent_n1 = tk.Entry()

lbl_n2 = tk.Label(text="\nIngrese el segundo numero: ")
ent_n2 = tk.Entry()

lbl_sum = tk.Label(text="-")

btn_sum = tk.Button(text="Sumar", command=sumar, bg="blue", fg="white")
btn_cerr = tk.Button(text="Cerrar", command=cerrar, bg="red", fg="white")

lbl_n1.pack()
ent_n1.pack()
lbl_n2.pack()
ent_n2.pack()
lbl_sum.pack()
btn_sum.pack()
btn_cerr.pack()

ventana.mainloop()
