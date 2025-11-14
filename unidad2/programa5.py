# Francisco Javier Ruiz Gonzalez
# 3-D
# Programa 5: Menu de opciones

print("Menu de opciones\n")
print("-- Color favorito --")

print("1.- Rojo")
print("2.- Negro")
print("3.- Morado")
print("4.- Naranja")
print("5.- Verde")
print("6.- Otro\n")
opcion = int(input("Elige una opcion: "))

match opcion:
    case 1:
        print("Tu color favorito es el rojo")
    case 2:
        print("Tu color favorito es el negro")
    case 3:
        print("Tu color favorito es el morado")
    case 4:
        print("Tu color favorito es el naranja")
    case 5:
        print("Tu color favorito es el verde")
    case 6:
        color_fav = input("Cual es tu color favorito? ").lower()

        print("Tu color favorito es el", color_fav)
    case _:
        print("Opcion no valida")
