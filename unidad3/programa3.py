def total():
    sel = lbx_dpto.curselection()
    dpto = lbx_dpto.get(sel)
    cant = int(ent_c.get())
    prec = float(ent_p.get())
    total = cant * prec

    if dpto == "Niños":
        desc = 5
    elif dpto == "Damas":
        desc = 10
    elif dpto == "Caballeros":
        desc = 15
    elif dpto == "Hogar":
        desc = 20
    else:
        desc = 25
    r = total * (100 - desc) / 100
    messagebox.showinfo("Total", f"Total: ${str(r)}")

def limpiar():
    ent_p.delete(0, tk.END)
    ent_c.delete(0, tk.END)

def salir():
    _salir = messagebox.askyesno("Salir?", "Estas seguro de que quieres salir?")
    if _salir:
        ventana.destroy()

import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Departamentos")
ventana.geometry("300x350")

tk.Label(text="Precio: ").pack()
ent_p = tk.Entry()
ent_p.pack()
tk.Label(text="Cantidad: ").pack()
ent_c = tk.Entry()
ent_c.pack()

tk.Label(text="Departamentos: ").pack()
lbx_dpto = tk.Listbox()
lbx_dpto.insert(0, "Niños")
lbx_dpto.insert(1, "Damas")
lbx_dpto.insert(2, "Caballeros")
lbx_dpto.insert(3, "Hogar")
lbx_dpto.insert(4, "Cocina")
lbx_dpto.pack()

frm_botones = tk.Frame()

btn_t = tk.Button(frm_botones, text="Total", command=total)
btn_t.grid(row=0, column=1, padx=5)
btn_limp = tk.Button(frm_botones, text="Limpiar", command=limpiar)
btn_limp.grid(row=0, column=2, padx=5)
btn_cerr = tk.Button(frm_botones, text="Salir", command=salir)
btn_cerr.grid(row=0, column=3, padx=5)

frm_botones.pack(pady=10)

ventana.mainloop()