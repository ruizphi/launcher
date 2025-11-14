# Francisco Javier Ruiz Gonzalez
# 3-D
# Programa 4: Realiza el programa que obtenga cuanto pagara el alumno para su
# proxima inscripcion

costo_inscrip = 5000
costo_libro = 900
cobro_exm = 0
cobro_atr = 0

preg_mr = input("El alumno tiene alguna materia reprobada? (si/no): ").lower()

if preg_mr == "si":
    mr = int(input("Entonces, cuantas materias reprobadas tiene? "))

    cobro_exm = 500 * mr

atraso = input("El alumno tuvo algun atraso? ").lower()

if atraso == "si":
    da = int(input("Cuantos dias se atraso? "))

    cobro_atr = da * 10

semestre = int(input("De que semestre es? (1/2/3...): "))

if semestre == 1:
    costo_libro = 1200

total = costo_inscrip + costo_libro + cobro_exm + cobro_atr
print("\nInscripcion:", costo_inscrip)
print("Pago del libro:", costo_libro)
print("Pago por extraordinario:", cobro_exm)
print("Pago por algun atraso:", cobro_atr)
print("\nTotal a pagar:", total)


