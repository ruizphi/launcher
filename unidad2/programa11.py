# Francisco Javier Ruiz Gonzalez
# 3-D
# Programa 11: Programa que obtenga el total a pagar en una tienda
# - el precio de cada producto y cuantos productos lleva
# - debes agregarle el IVA (16%)
# Mostrar el total a pagar

suma = 0

while True:
    precio = float(input("Ingrese el precio: "))
    prods = int(input("Cuantos productos va a llevar: "))
    parcial = precio * prods
    suma += parcial
    
    print(f"Parcial: ${parcial}")

    otro = input("Otro producto? (si/no): ").lower()

    if otro == "no":
        break
    else:
        continue

iva = suma * 0.16
total = suma + iva

print("\nSubtotal:", suma)
print("IVA:", iva)
print("Total:", total)
