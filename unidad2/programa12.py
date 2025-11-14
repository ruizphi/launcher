# Francisco Javier Ruiz Gonzalez
# 3-D
# Programa 12: Programa que muestre el total de hombres y mujeres que ingresaron
# en lugar X

h, m = 0, 0
while True:
    resp = input("Eres hombre o mujer? (h/m): ")

    if resp == "h":
        h += 1
    elif resp == "m":
        m += 1

    terminar = int(input("Terminar encuesta? (0: no, 1: si): "))

    if terminar == 1:
        break
    elif terminar == 0:
        continue
    else:
        print("Opcion invalida")
    
total = h + m

print("Hombres:", h)
print("Mujeres:", m)
print("\nEl total de hombres y mujeres fueron:", total)
