import tkinter as tk
import os
import sys
import subprocess
from tkinter import messagebox

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
        btn_u1_prog1.pack(pady=10)
        lbl_u1_prog1.pack()
        btn_u1_prog2.pack(pady=10)
        lbl_u1_prog2.pack()
        btn_u1_prog3.pack(pady=10)
        lbl_u1_prog3.pack()
        btn_u1_prog4.pack(pady=10)
        lbl_u1_prog4.pack()
        btn_u1_prog5.pack(pady=10)
        msg_u1_prog5.pack()
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

""" -- Log-in -- """
def login():
    toplvl = tk.Toplevel()
    toplvl.geometry("300x150")
    toplvl.title("Login")
    toplvl.grab_set()

    lbl_user = tk.Label(toplvl, text="Usuario:")
    ent_user = tk.Entry(toplvl)

    lbl_pswd = tk.Label(toplvl, text="Contraseña:")
    ent_pswd = tk.Entry(toplvl, show="*")

    # Si el usuario intenta cerrar la ventana de login, simplemente se cierra la aplicacion principal
    toplvl.protocol("WM_DELETE_WINDOW", lambda: ventana.destroy())
    
    def evaluar():
        user = ent_user.get()
        pswd = ent_pswd.get()
        if user == "admin" and pswd == "123":
            messagebox.showinfo("Login Exitoso", "Bienvenido!")
            toplvl.destroy()
        else:
            messagebox.showerror("Login Fallido", "Usuario o contraseña incorrectos.")
    
    btn_ingr = tk.Button(toplvl, text="Ingresar", command=evaluar)

    lbl_user.pack()
    ent_user.pack()
    lbl_pswd.pack()
    ent_pswd.pack()
    btn_ingr.pack(pady=5)

    ventana.wait_window(toplvl)

ventana = tk.Tk()
ventana.geometry("470x400")
ventana.title("Ejecutor de programas")

paned = tk.PanedWindow(orient=tk.HORIZONTAL)
paned.pack(fill=tk.BOTH, expand=True)

frm_unid = tk.Frame(paned, width=150, height=200, relief=tk.SUNKEN, bg="#dddddd")
frm_progs = tk.Frame(paned, width=150, height=200, relief=tk.SUNKEN)

btn_unid1 = tk.Button(frm_unid, text="Unidad 1", width=12, bg="#84b0e4", fg="white", 
                      command=lambda: seleccionar(btn_unid1))
btn_unid2 = tk.Button(frm_unid, text="Unidad 2", width=12, command=lambda: seleccionar(btn_unid2))
btn_unid3 = tk.Button(frm_unid, text="Unidad 3", width=12, command=lambda: seleccionar(btn_unid3))

""" -- Unidad 1 -- """
btn_u1_prog1 = tk.Button(frm_progs, text="Programa 1", width=15, command=lambda: ejecutar("unidad1/programa1.py"))
lbl_u1_prog1 = tk.Label(frm_progs, text="Pedir nombre a usuario para saludarlo")

btn_u1_prog2 = tk.Button(frm_progs, text="Programa 2", width=15, command=lambda: ejecutar("unidad1/programa2.py"))
lbl_u1_prog2 = tk.Label(frm_progs, text="Suma de dos numeros")

btn_u1_prog3 = tk.Button(frm_progs, text="Programa 3", width=15, command=lambda: ejecutar("unidad1/programa3.py"))
lbl_u1_prog3 = tk.Label(frm_progs, text="Promedio de tres numeros")

btn_u1_prog4 = tk.Button(frm_progs, text="Programa 4", width=15, command=lambda: ejecutar("unidad1/programa4.py"))
lbl_u1_prog4 = tk.Label(frm_progs, text="Obtener el sueldo de un empleado que gana $50 la hora trabajada")

# NOTE: La descripcion del programa 5 es larga, por lo que se usa un Message en lugar de Label
btn_u1_prog5 = tk.Button(frm_progs, text="Programa 5", width=15, command=lambda: ejecutar("unidad1/programa5.py"))
msg_u1_prog5 = tk.Message(frm_progs, text="Obtener el total a pagar." \
" Si todos los productos tienen el mismo precio, al subtotal se le debe agregar el IVA (16%)", width=300)

""" -- Empaquetar widgets -- """

paned.add(frm_unid)
paned.add(frm_progs)
btn_unid1.pack()
btn_unid2.pack()
btn_unid3.pack()

btn_u1_prog1.pack(pady=10)
lbl_u1_prog1.pack()
btn_u1_prog2.pack(pady=10)
lbl_u1_prog2.pack()
btn_u1_prog3.pack(pady=10)
lbl_u1_prog3.pack()
btn_u1_prog4.pack(pady=10)
lbl_u1_prog4.pack()
btn_u1_prog5.pack(pady=10)
msg_u1_prog5.pack()

iniciar_seleccion(btn_unid1) # Asegura que Unidad 1 este siendo seleccionado por defecto
ventana.after(100, login) # Muestra la ventana de login al iniciar la aplicacion
ventana.mainloop()