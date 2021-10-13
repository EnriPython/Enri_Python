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
    print" Saliendo del programa .........."
    time.sleep(2)
    limpiar()
    sys.exit()


def radian():
    print""
    print""
    rad = float(input("     Ingrese valor del angulo en radianes---->: "))
    print""
    print""
    print'     El seno del angulo en radianes es:', round(math.sin(rad), 2)
    print""
    print""
    print'     El coseno  del angulo en radianes es:', round(math.cos(rad), 2)
    print""
    print""
    print'     El arcotangente del angulo en radianes es:', round(math.atan(rad), 2)
    print""
    print""
    print'     El angulo en radianes convertido en grados es:', round(math.degrees(rad), 2), 'grados '
    print""
    print""
    print'     La constante de pi es:', math.pi
    print""
    print""
    print'     El seno de pi es:', math.sin(math.pi/3)
    print""
    print""
    print'     El coseno de pi es:', math.cos(math.pi/3)
    print""
    print""


    tecla = raw_input("Presione <ENTER> para continuar en el programa, [0]--> para salir ......")
    if tecla == "0":
        salir()
    else:

        main()


def grados():
    print""
    print""
    grad = float(input("     Ingrese valor del angulo en grados---->: "))
    rad = (math.radians(grad))
    print""
    print""
    print'     El seno del angulo en radianes es:', round(math.sin(rad), 2)
    print""
    print""
    print'     El coseno  del angulo en radianes es:', round(math.cos(rad), 2)
    print""
    print""
    print'     El arcotangente del angulo en radianes es:', round(math.atan(rad), 2)
    print""
    print""
    print'     Los grados convertidos a radianes dan:', (math.radians(math.degrees(rad))), 'radianes'
    print""
    print""
    print'     La constante de pi es:', math.pi
    print""
    print""
    print'     El seno de pi es:', math.sin(math.pi/3)
    print""
    print""
    print'     El coseno de pi es:', math.cos(math.pi/3)
    print""
    print""


    tecla = raw_input("Presione <ENTER> para continuar en el programa, [0]--> para salir ......")
    if tecla == "0":
        salir()
    else:

        main()


def main():
    print""
    print""
    print"     ##########################################################################################"
    print"     #                                                                                        #"
    print"     #                                TRIGONOMETRIA                                           #"
    print"     #                                                                                        #"
    print"     #  ingresa el valor del angulo en radianes, y devuelve: el seno, coseno y arcotangente   #"
    print"     #  del angulo en radianes; convierte el angulo en radianes a grados, la constante de pi, #"
    print"     #  el seno de pi y  el coseno de pi.                                                     #"
    print"     ##########################################################################################"
    print""
    print""
    print""
    print""
    unidad = raw_input("     Como va a introducir el valor del angulo?, r = radianes, g = grados.  <r/g>, <0> para salir ---->: ")
    if unidad != "r" and unidad != "g" and unidad != "0":
        print "Opcion incorrecta, presione <ENTER> para volver al menu ...."
        raw_input()

        main()


    if unidad == "r":
        radian()

    if unidad == "g":
        grados()


    if unidad == "0":
        salir()


main()
