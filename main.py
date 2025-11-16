import tkinter as tk
import os
import sys
import subprocess

# Variable global para seguir el boton seleccionado
seleccionado = None

def seleccionar(boton):
    """Gestiona la seleccion de unidades y actualiza los programas mostrados."""
    global seleccionado

    # Si ya hay un boton seleccionado, vuelve a su color original
    if seleccionado is not None:
        seleccionado.config(bg="white", fg="black")

    # Actualiza el boton seleccionado
    boton.config(bg="#6899d4", fg="white")
    seleccionado = boton

    # Limpiar frm_progs por defecto
    for widget in frm_progs.winfo_children():
        widget.pack_forget()

    # Agregar programas segun la unidad seleccionada
    if boton.cget("text") == "Unidad 1":
        btn_u1_prog1.pack(pady=5)
        lbl_u1_prog1.pack()
        btn_u1_prog2.pack(pady=5)
        lbl_u1_prog2.pack()
        btn_u1_prog3.pack(pady=5)
        lbl_u1_prog3.pack()
        btn_u1_prog4.pack(pady=5)
        lbl_u1_prog4.pack()
    elif boton.cget("text") == "Unidad 2":
        # TODO: Agregar botones y etiquetas para Unidad 2
        pass
    elif boton.cget("text") == "Unidad 3":
        # TODO: Agregar botones y etiquetas para Unidad 3
        pass

def iniciar_seleccion(boton):
    """
    Inicia la seleccion de un boton al iniciar la aplicacion.
    Es de un solo uso:
    >>> iniciar_seleccion(btn_unid1)
    """
    global seleccionado

    if seleccionado is None:
        boton.config(bg="#6899d4", fg="white")
    seleccionado = boton

def ejecutar(programa: str) -> None:
    """
    Ejecuta el programa especificado en una nueva terminal.
    programa: Ruta al archivo .py
    
    >>> ejecutar("unidad{n}/programa{n}.py")
    """
    ruta = os.path.join(os.path.dirname(__file__), programa)
    
    if os.name == "nt": # Windows
        subprocess.Popen(["start", "cmd", "/k", sys.executable, ruta], shell=True)
    else: # macOS, Linux
        subprocess.Popen(["x-terminal-emulator", "-e", f"{sys.executable} {ruta}"])

ventana = tk.Tk()
ventana.geometry("470x400")
ventana.title("Ejecutor de programas")

paned = tk.PanedWindow(orient=tk.HORIZONTAL)
paned.pack(fill=tk.BOTH, expand=True)

frm_unid = tk.Frame(paned, width=150, height=200, relief=tk.SUNKEN, bg="#dddddd")
frm_progs = tk.Frame(paned, width=150, height=200, relief=tk.SUNKEN)

btn_unid1 = tk.Button(frm_unid, text="Unidad 1", width=10, bg="#84b0e4", fg="white", 
                      command=lambda: seleccionar(btn_unid1))
btn_unid2 = tk.Button(frm_unid, text="Unidad 2", width=10, command=lambda: seleccionar(btn_unid2))
btn_unid3 = tk.Button(frm_unid, text="Unidad 3", width=10, command=lambda: seleccionar(btn_unid3))

""" -- Unidad 1 -- """
btn_u1_prog1 = tk.Button(frm_progs, text="Programa 1", command=lambda: ejecutar("unidad1/programa1.py"))
lbl_u1_prog1 = tk.Label(frm_progs, text="Pedir nombre a usuario para saludarlo")

btn_u1_prog2 = tk.Button(frm_progs, text="Programa 2", command=lambda: ejecutar("unidad1/programa2.py"))
lbl_u1_prog2 = tk.Label(frm_progs, text="Suma de dos numeros")

btn_u1_prog3 = tk.Button(frm_progs, text="Programa 3", command=lambda: ejecutar("unidad1/programa3.py"))
lbl_u1_prog3 = tk.Label(frm_progs, text="Promedio de tres numeros")

btn_u1_prog4 = tk.Button(frm_progs, text="Programa 4", command=lambda: ejecutar("unidad1/programa4.py"))
lbl_u1_prog4 = tk.Label(frm_progs, text="Obtener el sueldo de un empleado que gana $50 la hora trabajada")

paned.add(frm_unid)
paned.add(frm_progs)
btn_unid1.pack()
btn_unid2.pack()
btn_unid3.pack()

btn_u1_prog1.pack(pady=5)
lbl_u1_prog1.pack()
btn_u1_prog2.pack(pady=5)
lbl_u1_prog2.pack()
btn_u1_prog3.pack(pady=5)
lbl_u1_prog3.pack()
btn_u1_prog4.pack(pady=5)
lbl_u1_prog4.pack()

iniciar_seleccion(btn_unid1) # Asegura que Unidad 1 este siendo seleccionado por defecto
ventana.mainloop()