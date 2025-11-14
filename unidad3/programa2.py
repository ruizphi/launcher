# Francisco Javier Ruiz Gonzalez
# 3-D
# Programa 2: Obtiene el sueldo de un empleado depende de la categoria

import tkinter as tk
from tkinter import messagebox

def sueldo():
    select = lbx_cate.curselection()
    cate = lbx_cate.get(select)

    if cate == 'a':
        sueldo = 100
    elif cate == 'b':
        sueldo = 150
    elif cate == 'c':
        sueldo = 200
    else:
        sueldo = 250
    ht = int(ent_ht.get())
    pago = ht * sueldo
    messagebox.showinfo("Sueldo de empleado",
                        f"El sueldo del empleado {ent_nomb.get()} es ${str(pago)}")

def limpiar():
    ent_nomb.delete(0, tk.END)
    ent_ht.delete(0, tk.END)

def salir():
    _salir = messagebox.askyesno("Salir?", "Estas seguro de que quieres salir?")
    if _salir:
        ventana.destroy()

ventana = tk.Tk()
ventana.geometry("300x350")
ventana.config(bg="black")

lbl_nomb = tk.Label(text="Ingrese su nombre: ", bg="black", fg="white")
ent_nomb = tk.Entry()

lbl_ht = tk.Label(text="Ingrese las horas trabajadas: ", bg="black", fg="white")
ent_ht = tk.Entry()

lbl_cate = tk.Label(text="Selecciona la categoria", bg="black", fg="white")
lbx_cate = tk.Listbox()

lbx_cate.insert(0, "a")
lbx_cate.insert(1, "b")
lbx_cate.insert(2, "c")
lbx_cate.insert(3, "d")

frm_botones = tk.Frame(ventana, bg="black")

btn_sueldo = tk.Button(frm_botones, text="Sueldo", command=sueldo)
btn_sueldo.grid(row=0, column=0, padx=5)
btn_limp = tk.Button(frm_botones, text="Limpiar", command=limpiar)
btn_limp.grid(row=0, column=1, padx=5)
btn_cerr = tk.Button(frm_botones, text="Salir", command=salir)
btn_cerr.grid(row=0, column=2, padx=5)

lbl_nomb.pack()
ent_nomb.pack()
lbl_ht.pack()
ent_ht.pack()
lbl_cate.pack()
lbx_cate.pack(pady=7)
frm_botones.pack(pady=10)

ventana.mainloop()
