# Variable global para seguir el botón seleccionado
seleccionado = None

def seleccionar(boton):
    global seleccionado

    # Si ya hay un botón seleccionado, vuelve a su color original
    if seleccionado is not None:
        seleccionado.config(bg="white", fg="black")

    # Actualiza el color del botón seleccionado
    boton.config(bg="#6899d4", fg="white")
    
    # Actualiza el botón seleccionado
    seleccionado = boton

def act_interfaz():
    """
    Actualiza frm_progs para que cada boton de unidad muestre
    lo que le corresponde.
    """
    for widget in frm_progs.winfo_children():
        widget.destroy()

def ejecutar(programa):
    ruta = os.path.join(os.path.dirname(__file__), programa)
    
    if os.name == "nt": # Windows
        subprocess.Popen(["start", "cmd", "/k", sys.executable, ruta], shell=True)
    else: # macOS, Linux
        subprocess.Popen(["x-terminal-emulator", "-e", f"{sys.executable} {ruta}"])

import tkinter as tk
import os
import sys
import subprocess

ventana = tk.Tk()
ventana.geometry("450x400")
ventana.title("Ejecutor de programas")

paned = tk.PanedWindow(orient=tk.HORIZONTAL)
paned.pack(fill=tk.BOTH, expand=True)

frm_unid = tk.Frame(paned, width=150, height=200, relief=tk.SUNKEN, bg="#dddddd")
frm_progs = tk.Frame(paned, width=150, height=200, relief=tk.SUNKEN)

btn_unid1 = tk.Button(frm_unid, text="Unidad 1", width=10, bg="#84b0e4", fg="white", command=lambda: seleccionar(btn_unid1))
btn_unid2 = tk.Button(frm_unid, text="Unidad 2", width=10, command=lambda: seleccionar(btn_unid2))
btn_unid3 = tk.Button(frm_unid, text="Unidad 3", width=10, command=lambda: seleccionar(btn_unid3))

btn_prog1 = tk.Button(frm_progs, text="Programa 1", command=lambda: ejecutar("unidad1/programa1.py"))
lbl_prog1 = tk.Label(frm_progs, text="Pedir nombre a usuario para saludarlo")

btn_prog2 = tk.Button(frm_progs, text="Programa 2", command=lambda: ejecutar("unidad1/programa2.py"))
lbl_prog2 = tk.Label(frm_progs, text="Suma de dos numeros")

paned.add(frm_unid)
paned.add(frm_progs)
btn_unid1.pack()
btn_unid2.pack()
btn_unid3.pack()
btn_prog1.pack(pady=5)
lbl_prog1.pack()
btn_prog2.pack(pady=5)
lbl_prog2.pack()
seleccionar(btn_unid1) # Controla que Unidad 1 este siendo seleccionado por defecto

ventana.mainloop()