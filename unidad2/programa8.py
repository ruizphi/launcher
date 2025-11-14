# Francisco Javier Ruiz Gonzalez
# 3-D
# Programa 8: Programa que obtenga el promedio de 5 numeros
"""
print("1")
print("2")
print("3")
print("4")
print("5")
print("6")
. . .
n = 1
while n < 11:
    print(n)
    n += 1
print("Fin del ciclo")
"""
i = 1
suma = 0
print("-- Promedio de 5 numeros --")
while i < 6:
    num = int(input(f"Ingrese el numero {i}: "))
    if num < 0:
        print("El numero ingresado no es valido")
        break
    else:
        i += 1
        suma += num
    if i == 6:
        prom = suma/5
        print("\nEl promedio de los 5 numeros es:", prom)
