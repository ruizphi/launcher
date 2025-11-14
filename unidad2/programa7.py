# Francisco Javier Ruiz Gonzalez
# 3-D
# Programa 7: Programa que obtenga el precio final de un producto si sabemos que
# segun el departamento
# Bebes: 15%, Calzado: 5%, Damas: 10%, Caballeros: 8%, Accesorios: 20%

print("-- Departamentos --")
print("1.- Bebes")
print("2.- Calzado")
print("3.- Damas")
print("4.- Caballeros")
print("5.- Accesorios")

dpto = int(input("En cual departamento quieres entrar? "))
precio = float(input("Ingrese el precio del producto: "))

match dpto:
    case 1: # bebes
        desc = 15
    case 2: # calzado
        desc = 5
    case 3: # damas
        desc = 10
    case 4: # caballeros
        desc = 8
    case 5: # accesorios
        desc = 20
    case _:
        print("Departamento no disponible")

r = precio * (100 - desc) / 100

print("El precio final es:", r)
