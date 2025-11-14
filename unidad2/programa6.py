# Francisco Javier Ruiz Gonzalez
# 2-D
# Programa 6: Descuento por edad con match
# Menor que 18 - 20%, Mayor que 60 - 25%, Otro - 15%

pago = float(input("Ingrese el pago: "))
edad = int(input("Edad del cliente: "))

match edad:
    case edad if edad < 18:
        desc = pago * 0.20
        r = pago - desc
    case edad if edad > 60:
        desc = pago * 0.25
        r = pago - desc
    case _:
        desc = pago * 0.15
        r = pago - desc

print("El precio final es:", r)
