import os
from clases.lugar import Lugar
from clases.barrio import Barrio

class Controlador(object):

    @classmethod
    def menu(cls):

        print("1: Ver lugares")
        print("2: Crear lugar")
        print("5. Salir")
        print("")
        print("Ingresame que queres hacer")
        ingreso = input()
        return ingreso

    @classmethod
    def menu_creacion(cls):

        print("1: Continente")
        print("2: Pais")
        print("3: Provincia")
        print("4: Ciudad")
        print("5: Barrio")
        print("6: Salir")
        print("")
        print("Ingresame que queres crear")
        ingreso = input()
        return ingreso

    @classmethod
    def imprimir_lugar(cls, lista):

        print("--- CONTINENTES")
        for i in lista:
            print(i.codigo + " | " + i.nombre + " | " + i.tipo + " | " + str(len(i.dependencias)))
        print("")
        print("--- PAISES")
        print("")
        for continente in lista:
            for pais in continente.dependencias:
                print(pais.codigo + " | " + pais.nombre + " | " + continente.nombre + " | " + str(len(pais.dependencias)))
                print("")
                for provincia in pais.dependencias:
                    print("    - " + provincia.codigo + " | " + provincia.nombre + " | " + provincia.tipo + " | " + str(len(provincia.dependencias)))
                    print("")
                    for ciudad in provincia.dependencias:
                        print("        - " + ciudad.codigo + " | " + ciudad.nombre + " | " + ciudad.tipo + " | " + str(len(ciudad.dependencias)))
                        print("")
                        for barrio in ciudad.dependencias:
                            print("            - " + barrio.codigo + " | " + barrio.nombre + " | " + str(barrio.poblacion))
                    print("")


    @classmethod
    def crear_lugar(cls, continentes):

        os.system("cls")
        ingreso = Controlador.menu_creacion()
        os.system("cls")
        if ingreso == "1":
            Controlador.ingresar_datos_lugar(continentes, "Continente")
        if ingreso == "2":
            Controlador.ingresar_datos_lugar(continentes, "Pais")
        if ingreso == "3":
            Controlador.ingresar_datos_lugar(continentes, "Provincia")
        if ingreso == "4":
            Controlador.ingresar_datos_lugar(continentes, "Ciudad")
        if ingreso == "5":
            Controlador.ingresar_datos_lugar(continentes, "Barrio")
        if ingreso == "6":
            return

    @classmethod
    def ingresar_datos_lugar(cls, continentes, tipo):

        print("Ingresa el codigo")
        #TODO: Verificar que no se repita
        codigo = input()
        print("")

        print("Ingresa el nombre")
        nombre = input()
        print("")

        print("Ingresa las coordenadas")
        x = input()
        y = input()
        print("")

        if tipo != "Barrio":
            l = Lugar(codigo, nombre, (x,y), tipo)
            if tipo == "Continente":
                continentes.append(l)
            else:
                Controlador.meter_lista(l, continentes)
        else:
            print("Ingresa la poblacion")
            poblacion = input()
            poblacion = int(poblacion)
            print("")
            b = Barrio(codigo, nombre, (x,y), poblacion)
            Controlador.insertar_barrio(b, continentes)
        return

    @classmethod
    def meter_lista(cls, lugar, continentes):

        if lugar.tipo == "Pais":
            print("Ingrese el codigo de continente")
            continente = input()

        elif lugar.tipo == "Provincia":
            print("")
            print("Ingrese el codigo de pais")
            pais = input()

        elif lugar.tipo == "Ciudad":
            print("")
            print("Ingrese el codigo de provincia")
            provincia = input()

        for con in continentes:
            if lugar.tipo == "Pais":
                if con.codigo == continente:
                    con.dependencias.append(lugar)
            else:
                for pa in con.dependencias:
                    if lugar.tipo == "Provincia":
                        if pa.codigo == pais:
                            pa.dependencias.append(lugar)
                    else:
                        for pro in pa.dependencias:
                            if lugar.tipo == "Ciudad":
                                if pro.codigo == provincia:
                                    pro.dependencias.append(lugar)


    @classmethod
    def insertar_barrio(cls, barrio, continentes):

        print("Ingrese el codigo de ciudad")
        ciudad = input()
        print("")

        ciudad = Controlador.devolver_ciudad(continentes, ciudad)

        ciudad.dependencias.append(barrio)

    @classmethod
    def devolver_ciudad(cls, continentes, ciudad):

        for con in continentes:
            for pa in con.dependencias:
                for pro in pa.dependencias:
                    for ciu in pro.dependencias:
                        if ciu.codigo == ciudad:
                            return ciu
        return False

    @classmethod
    def buscar_barrio(cls, continentes):

        print("Ingrese el codigo de contientente")
        continente = input()
        print("")
        print("Ingrese el codigo de pais")
        pais = input()
        print("")
        print("Ingrese el codigo de provincia")
        provincia = input()
        print("")
        print("Ingrese el codigo de ciudad")
        ciudad = input()
        print("")
        print("Ingrese el codigo del barrio")
        barrio = input()
        print("")

        ciudad = Controlador.devolver_ciudad(continentes, ciudad)
