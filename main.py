from clases import *
import os

continentes = []

os.system("cls")

#Continentes:

c1 = Lugar("AM", "America", (2000,9800), "Continente")
c2 = Lugar("EU", "Europa del Este", (100,-7500), "Continente")

continentes.append(c1)
continentes.append(c2)

while True:

    os.system("cls")
    ingreso = Controlador.menu()
    os.system("cls")

    if ingreso == "1":
        Controlador.imprimir_lugar(continentes)
        input()
    elif ingreso == "2":
        Controlador.crear_lugar(continentes)
    elif ingreso == "5":
        exit()
