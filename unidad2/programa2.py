# Francisco Javier Ruiz Gonzalez
# 3-D
# Programa 2: Descuento de croquetas segun tamaño de bolsa

kg = int(input("Ingrese la bolsa en kg: "))
prc = float(input("Ingrese el precio de una bolsa promedio: "))

if kg == 20:
    desc = prc * 0.20
    precio = prc - desc
elif kg == 10:
    desc = prc * 0.10
    precio = prc - desc
else:
    desc = prc * 0.05
    precio = prc - desc

print("El precio de la bolsa ahora es:", precio)
