# Francisco Javier Ruiz Gonzalez
# 3-D
# Programa 5: Obtener el total a pagar, si todos los productos tienen el mismo
# precio, al sub total se le debe agregar el IVA (16%)
# Debes mostrar en la salida
'''
Total de productos comprados: x
Sub total:                    x
IVA:                          x
Total a pagar:                x
'''

ppr = float(input("Introduce el precio de los productos: "))
pcant = int(input("Ingrese la cantidad de productos: "))

sub = ppr * pcant
iva = sub * 0.16

print("\nTotal de productos comprados:  ", pcant)
print("Sub total:                     ", sub)
print("IVA:                           ", (iva))
print("Total a pagar:                 ", (sub + iva))