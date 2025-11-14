# Francisco Javier Ruiz Gonzalez
# 3-D
# Programa 10: Una empresa cuenta con 10 empleados, a los cuales les paga $200
# la hora trabajada, realiza el programa que obtenga el sueldo de cada empleado
# y el total que pagara a todos ellos.

i = 1
ht = 200
suma = 0

while i < 11:
    sueldo = int(input(f"Empleado {i}: $"))
    i += 1
    suma += sueldo

    print("Se le pagara a este empleado:", (sueldo * ht))

total = suma * ht

print("\nEl total a pagar de todos los empleados es:", total)
