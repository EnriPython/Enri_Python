#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import time
import os
import sys





def limpiar():
    """Limpia la pantalla"""

    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")


def salir():
    print""
    print"     Saliendo del programa .........."
    time.sleep(2)
    limpiar()
    sys.exit()


def magnitud():
    print""
    print"     Escriba las coordenadas cartesianas, numero positivo, negativo o cero con dos decimales"
    print""
    x = float(input("     Ingrese el valor del vector < x > "))
    y = float(input("     Ingrese el valor del vector < y > "))
    z = float(input("     Ingrese el valor del vector < z > "))
    mg = math.sqrt(x**2 + y**2 + z**2)
    mag = round(mg, 2)
    print""
    print"     La magnitud del vector", x, y, z, "es: ", mag
    print""
    print""
    raw_input("     Presione <ENTER> para volver al menu principal ---->")
    main()


def angulos():
    print""
    print"     escriba las coordenadas cartesianas, numero positivo, negativo o cero con dos decimales"
    print""
    x = float(input("     Ingrese el valor del vector < x > "))
    y = float(input("     Ingrese el valor del vector < y > "))
    z = float(input("     Ingrese el valor del vector < z > "))
    Ar = math.atan2(y, x)
    A = math.degrees(Ar)
    Br = math.atan2(math.sqrt(x**2 + y**2), z)
    B = math.degrees(Br)
    print""
    print"     Los angulos A y B  en grados del vector", x, y, z, " son: A=", round(A, 2), " B=", round(B, 2)
    print""
    print""
    raw_input("     Presione <ENTER> para volver al menu principal ---->")
    main()


def mas_menos():
    print""
    print"     Escriba las coordenadas cartesianas, numero positivo, negativo o cero con dos decimales"
    print""
    x1 = float(input("     Ingrese el valor del vector < x1 > "))
    y1 = float(input("     Ingrese el valor del vector < y1 > "))
    z1 = float(input("     Ingrese el valor del vector < z1 > "))
    x2 = float(input("     Ingrese el valor del vector < x2 > "))
    y2 = float(input("     Ingrese el valor del vector < y2 > "))
    z2 = float(input("     Ingrese el valor del vector < z2 > "))
    suma = x1 + x2, y1 + y2, z1 + z2
    resta = x1 - x2, y1 - y2, z1 - z2
    print""
    print "     La suma y la resta de los vectores", x1, y1, z1, "y", x2, y2, z2, "es, SUMA:", suma, " RESTA:", resta
    print""
    print""
    raw_input("     Presione <ENTER> para volver al menu principal ---->")
    main()


def producto():
    x1 = float(input("     Ingrese el valor del vector < x1 >"))
    y1 = float(input("     Ingrese el valor del vector < y1 >"))
    z1 = float(input("     Ingrese el valor del vector < z1 >"))
    x2 = float(input("     Ingrese el valor del vector < x2 >"))
    y2 = float(input("     Ingrese el valor del vector < y2 >"))
    z2 = float(input("     Ingrese el valor del vector < z2 >"))
    punto = x1*x2+y1*y2+z1*z2
    crus = round(y1*z2-y2*z1, 3), round(x2*z1-x1*z2, 3), round(x1*y2-x2*y1, 3)
    mag1 = math.sqrt(x1**2+y1**2+z1**2)
    mag2 = math.sqrt(x2**2+y2**2+z2**2)
    magcrus = math.sqrt((y1*z2-y2*z1)**2+(x2*z1-x1*z2)**2+(x1*y2-x2*y1)**2)
    ang12r = math.acos(punto/(mag1*mag2))
    angulo12 = math.degrees(ang12r)
    angle21r = math.asin(magcrus/(mag1*mag2))
    angle21 = math.degrees(angle21r)
    print""
    print"     El producto escalar es:", round(punto, 2), "y el producto vectorial:", crus
    print""
    print"     Los angulos V1 y V2:", round(angulo12, 2), round(angle21, 2)
    print""
    print"     Si los valores son diferentes, analice un diagrama vectorial y decida."
    print""
    print""
    raw_input("     Presione <ENTER> para volver al menu principal ---->")
    main()


def main():
    limpiar()
    print""
    print""
    print"     ###########################################################################"
    print"     #                                                                         #"
    print"     #                             Enri_Python                                 #"
    print"     #                                                                         #"
    print"     #                        ALGEBRA VECTORIAL v1.0                           #"
    print"     #                                                                         #"
    print"     #               Magnitud, angulos, suma, resta y productos                #"
    print"     #                                                                         #"
    print"     ###########################################################################"
    print""
    print""
    print"     1- MAGNITUD --->  "
    print""
    print"     2- ANGULOS"
    print""
    print"     3- MAS_MENOS"
    print""
    print"     4- PRODUCTO"
    print""
    print"     0- Salir --> "
    print""
    opcion = raw_input("     Ingresa un numero del menu -> ")
    print""

    if opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4" and opcion != "0":
        print "     Opcion incorrecta, presione <ENTER> para volver al menu ...."

        raw_input()

        main()


    if opcion == "1":

        magnitud()

    if opcion == "2":

        angulos()

    if opcion == "3":

        mas_menos()

    if opcion == "4":

        producto()

    if opcion == "0":

        salir()


main()
