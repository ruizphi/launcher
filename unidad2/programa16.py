# Francisco Javier Ruiz Gonzalez
# 3-D
# Programa 16: Obtener el mayor de 2 numeros con Tkinter
import tkinter as tk
def mayor():
    n1 = int(ent_n1.get())
    n2 = int(ent_n2.get())
    if n1 > n2:
        mayor = n1
    else:
        mayor = n2
    lbl_may.config(text=f"El mayor es: {str(mayor)}")
def limpiar():
    ent_n1.delete(0, tk.END)
    ent_n2.delete(0, tk.END)
    lbl_may.config(text="-")
def cerrar():
    ventana.destroy()
ventana = tk.Tk()
ventana.title("¿Cuál de los dos números es mayor?")
ventana.geometry("500x300")
ventana.resizable(False, False)
lbl_n1 = tk.Label(text="Ingrese el primer número:")
ent_n1 = tk.Entry()
lbl_n2 = tk.Label(text="Ingrese el segundo número:")
ent_n2 = tk.Entry()
lbl_may = tk.Label(text="-", font=("Arial", 14))
btn_may = tk.Button(text="Ejecutar", command=mayor, bg="blue", fg="white", width=10)
btn_limp = tk.Button(text="Limpiar", command=limpiar, bg="orange", fg="white", width=10)
btn_cerr = tk.Button(text="Cerrar", command=cerrar, bg="red", fg="white", width=10)
btn_may.place(x=250, y=50)
btn_limp.place(x=250, y=100)
btn_cerr.place(x=250, y=150)
lbl_n1.place(x=30, y=50)
ent_n1.place(x=30, y=80)
lbl_n2.place(x=30, y=120)
ent_n2.place(x=30, y=150)
lbl_may.place(x=250, y=200)
ventana.mainloop()
