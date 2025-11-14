# Francisco Javier Ruiz Gonzalez
# 3-D
# Programa 17: Obtener el promedio de 3 numeros
import tkinter as tk
def promediar():
    n1 = int(ent_n1.get())
    n2 = int(ent_n2.get())
    n3 = int(ent_n3.get())
    prom = (n1+n2+n3)/3
    lbl_prom.config(text=f"El promedio es: {str(prom)}")
def limpiar():
    ent_n1.delete(0, tk.END)
    ent_n2.delete(0, tk.END)
    ent_n3.delete(0, tk.END)
    lbl_prom.config(text="-")
def cerrar():
    ventana.destroy()
ventana = tk.Tk()
ventana.title("Promedio de tres numeros")
ventana.geometry("500x300")
lbl_n1 = tk.Label(text="Ingrese el primer numero:")
ent_n1 = tk.Entry()
lbl_n2 = tk.Label(text="Ingrese el segundo numero:")
ent_n2 = tk.Entry()
lbl_n3 = tk.Label(text="Ingrese el tercer numero:")
ent_n3 = tk.Entry()
lbl_prom = tk.Label(text="-")
btn_prom = tk.Button(text="Promediar", command=promediar, bg="blue", fg="white")
btn_limp = tk.Button(text="Limpiar", command=limpiar, bg="orange", fg="white")
btn_cerrar = tk.Button(text="Salir", command=cerrar, bg="red", fg="white")
btn_prom.place(x=250, y=100); btn_limp.place(x=250, y=130)
btn_cerrar.place(x=250, y=160)
lbl_n1.place(x=30, y=80)
ent_n1.place(x=30, y=100)
lbl_n2.place(x=30, y=130)
ent_n2.place(x=30, y=150)
lbl_n3.place(x=30, y=180)
ent_n3.place(x=30, y=200)
lbl_prom.place(x=250, y=200)
ventana.mainloop()
