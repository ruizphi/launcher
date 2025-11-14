# Francisco Javier Ruiz Gonzalez
# 3-D
# Programa 3: Programa que obtiene el total a pagar de un empleado

ht = int(input("Ingrese las horas trabajadas del empleado: "))
asistencia = int(input("Cuantas veces asistio el empleado a la semana? "))
aut = input("El supervisor autorizo un bono de productividad? ").lower()

sueldo_extra = 0
sueldo = 0
bono_p = 0

if ht > 40:
    sueldo = 40 * 100
    sueldo_extra = (ht - 40) * 200
else:
    sueldo = ht * 100

if asistencia == 5:
    bono_a = sueldo * 0.10

if aut == "si":
    bono_p = 200

subtotal = sueldo + sueldo_extra + bono_p + bono_a
isr = subtotal * 0.35
total = subtotal - isr

print("\n-- Datos --")
print("Sueldo base:", sueldo)
print("Horas extra:", sueldo_extra)
print("Bono por asistencia:", bono_a)
print("Bono por productividad:", bono_p)
print("ISR:", isr)
print("Total a pagar:", total)
