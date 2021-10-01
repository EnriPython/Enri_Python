#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Importando modulos

import math
from math import factorial
from math import pow

# import subprocess

import sys
import os
from fractions import Fraction
import time

res = None
mcd = None
mcm = None
inputt = None


# Operaciones matematicas varias by Enri_Python

# Limpia terminal


def limpiar():
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


def equa():
    print"    ##################################################################################"
    print"    #####                                                                        #####"
    print"    #####                 RESUELVE ECUACIONES DE SEGUNDO GRADO                   #####"
    print"    #####                                                                        #####"
    print"    #####   Ejemplo (1):  x(elevado a 2)-5x+6=0  -->  ingrese: A:1  B:-5  C:6    #####"
    print"    #####                                                                        #####"
    print"    #####   Ejemplo (2):  2x(elevado a 2)-7x+3=0  --> ingrese: A:2  B:-7  C:3    #####"
    print"    #####                                                                        #####"
    print"    ##################################################################################"
    print""

    a = float(input("Ingrese el valor de A (cociente del termino cuadratico): "))  # a = cociente del termino cuadratico
    print""
    b = float(input("Ingrese el valor de B (cociente de termino lineal): "))  # b = cociente de termino lineal
    print""
    c = float(input("Ingrese el valor de C (cociente de termino independiente): "))  # c = cociente de termino independiente
    print""

    # resolviendo

    x = (b ** 2) - (4 * a * c)

    # Si x es menor que 0, no tendra una solucion dentro de las reglas de los numeros reales

    if x < 0:
        print"Solucion solo en numeros complejos"

    x1 = (-b + math.sqrt(x)) / (2 * a)
    x2 = (-b - math.sqrt(x)) / (2 * a)

    # resultado

    # Mostramos ambos valores

    print"X1= ", x1
    print"X2= ", x2

    tecla = raw_input("Presione <ENTER> para seguir en el programa, [0]--> para salir ......")
    if tecla == "0":
        salir()
    else:

        main()


def divisor():
    print"    ########################################################"
    print"    #####    HALLA TODOS LOS DIVISORES DE UN NUMERO    #####"
    print"    ########################################################"
    print""
    numero = int(input("Ingresa un numero entero: "))
    divis = 0

    print""

    print("Divisores:")
    if numero % 2 == 0:
        iterar = numero / 2
    else:
        iterar = (numero - 1) / 2

    for i in range(1, int(iterar) + 1):
        if numero % i == 0:
            aux = numero / i
            if aux != divis:
                divis = aux
            if i == iterar:
                print""
                print (int(divis))
            else:
                print""
                print("%d," % divis)
    print""
    print"1"


    tecla = raw_input("Presione <ENTER>a para seguir en el programa, [0]--> para salir ......")
    if tecla == "0":
        salir()
    else:

        main()


def factor():
    print"    ###################################################"
    print"    #####    CALCULA EL FACTORIAL DE UN NUMERO    #####"
    print"    ###################################################"
    print""
    print""
    valor = int(input(" Ingrese un numero entero:"))
    resu = factorial(valor)
    print ""
    print" El factorial de", valor, "es:", resu
    print""

    tecla = raw_input("Presione <ENTER> para seguir en el programa, [0]--> para salir ......")
    if tecla == "0":
        salir()
    else:

        main()


def fraccion():
    print"    ########################################################"
    print"    #####        OPERACIONES CON 2 FRACCIONES          #####"
    print"    #####    suma, resta, multiplicacion y division    #####"
    print"    ########################################################"
    print""

    f1 = raw_input("Introduce la primera fraccion <numerador/denominador> (ejemplo: 3/4): ")
    f2 = raw_input("Introduce la segunda fraccion <numerador/denominador> (ejemplo: 1/5): ")

    print""

    SumaFrac = Fraction(f1) + Fraction(f2)
    print"La suma da: ", SumaFrac, "\n"

    RestaFrac = Fraction(f1) - Fraction(f2)
    print"La resta da: ", RestaFrac, "\n"

    MultiFrac = Fraction(f1) * Fraction(f2)
    print"La multiplicacion da: ", MultiFrac, "\n"

    DiviFrac = Fraction(f1) / Fraction(f2)
    print"La division da: ", DiviFrac, "\n"

    tecla = raw_input("Presione <ENTER> para seguir en el programa, [0]--> para salir ......")
    if tecla == "0":
        salir()
    else:

        main()


def longi():
    print"    #################################################################"
    print"    ####                                                         ####"
    print"    ####                 CONVERSOR DE LONGITUDES                 ####"
    print"    ####                                                         ####"
    print"    ####   SELECCIONE UNIDAD DE LONGITUD PARA ENTRADA DE DATOS   ####"
    print"    ####                                                         ####"
    print"    #################################################################"
    print""
    print""

    opcion = raw_input('Elige opcion < mm, cm, dm, m, Dm, Hm, km, [0] para salir--->:  ')

    print""

    if opcion != "mm" and opcion != "cm" and opcion != "dm" and opcion != "m" and opcion != "Dm" and opcion != "Hm" and opcion != "km" and opcion != "0":

        print""
        print "Opcion incorrecta, presione la tecla <ENTER> para continuar..."

        raw_input()
        longi()


    elif opcion == "0":

        print ""

        print "#####   SALIENDO DEL PROGRAMA...    #####"

        print ""

        print ""

        time.sleep(2)

        exit()

    cantidad = float(raw_input('indica una cantidad: '))

    if opcion == 'mm':

        print""
        print 'Calculando..............', cantidad, opcion
        print""

        print cantidad / 10, 'centimetros'

        print cantidad / 100, 'decimetros'

        print cantidad / 1000, 'metros'

        print cantidad / 10000, 'Decametros'

        print cantidad / 100000, 'Hectometros'

        print cantidad / 1000000, 'kilometros'



    elif opcion == 'cm':

        print""
        print 'Calculando..............', cantidad, opcion
        print""

        print cantidad * 10, 'milimetros'

        print cantidad / 10, 'decimetros'

        print cantidad / 100, 'metros'

        print cantidad / 1000, 'Decametros'

        print cantidad / 10000, 'Hectometros'

        print cantidad / 100000, 'kilometros'



    elif opcion == 'dm':

        print""
        print 'Calculando..............', cantidad, opcion
        print""

        print cantidad * 100, 'milimetros'

        print cantidad * 10, 'centimetros'

        print cantidad / 10, 'metros'

        print cantidad / 100, 'Decametros'

        print cantidad / 1000, 'Hectometros'

        print cantidad / 10000, 'kilometros'



    elif opcion == 'm':

        print""
        print 'Calculando..............', cantidad, opcion
        print""

        print cantidad * 1000, 'milimetros'

        print cantidad * 100, 'centimetros'

        print cantidad * 10, 'decimetros'

        print cantidad / 10, 'Decametros'

        print cantidad / 100, 'Hectometros'

        print cantidad / 1000, 'kilometros'



    elif opcion == 'Dm':

        print""
        print 'Calculando..............', cantidad, opcion
        print""

        print cantidad * 10000, 'milimetros'

        print cantidad * 1000, 'centimetros'

        print cantidad * 100, 'decimetros'

        print cantidad * 10, 'metros'

        print cantidad / 10, 'Hectometros'

        print cantidad / 100, 'kilometros'



    elif opcion == 'Hm':

        print""
        print 'Calculando..............', cantidad, opcion
        print""

        print cantidad * 100000, 'milimetros'

        print cantidad * 10000, 'centimetros'

        print cantidad * 1000, 'decimetros'

        print cantidad * 100, 'metros'

        print cantidad * 10, 'Decametros'

        print cantidad / 10, 'kilometros'



    elif opcion == 'km':

        print""
        print 'Calculando..............', cantidad, opcion
        print""

        print cantidad * 1000000, 'milimetros'

        print cantidad * 100000, 'centimetros'

        print cantidad * 10000, 'decimetros'

        print cantidad * 1000, 'metros'

        print cantidad * 100, 'Decametros'

        print cantidad * 10, 'Hectometros'

    tecla = raw_input("Presione <ENTER>a para seguir en el programa, [0]--> para salir ......")
    if tecla == "0":
        salir()
    else:

        main()


def maxcd():
    global res
    print"    ###############################################"
    print"    #####    HALLA EL MAXIMO COMUN DIVISOR    #####"
    print"    ###############################################"
    print""
    # pedimos al usuario que ingrese los numeros
    num1 = int(raw_input("Ingrese el primer numero entero: "))
    num2 = int(raw_input("Ingrese el segundo numero entero: "))
    print""
    # seleccionamos el mayor y el menor y los asignamos a las variables "a" y "b"
    a = max(num1, num2)
    b = min(num1, num2)
    # realizamos el ciclo encargado de hacer las interaciones
    while b != 0:
        res = b
        b = a % b
        a = res
    # mostramos resultado por pantalla
    print('El Maximo comun divisor de {0} y {1} es: {2}'.format(num1, num2, res))
    print""

    tecla = raw_input("Presione <ENTER> para seguir en el programa, [0]--> para salir ......")
    if tecla == "0":
        salir()
    else:

        main()


def mincm():
    global mcd, mcm
    print"    ###############################################"
    print"    #####    HALLA EL MINIMO COMUN MULTIPLO    ####"
    print"    ###############################################"
    print""

    num1 = int(raw_input("Ingrese el primer numero entero: "))
    num2 = int(raw_input("Ingrese el segundo numero entero: "))

    # seleccionamos el menor entre num1 y num2

    menor = min(num1, num2)

    # ciclo for para interactuar entre 1 y el menor de los dos numeros

    for i in range(1, menor):
        if num1 % i == 0 and num2 % i == 0:
            mcd = i

        # calculamos el minimo comun multiplo

        mcm = (num1 * num2) / mcd

    # mostramos resultado por pantalla

    print""
    print("El minimo comun multiplo entre " + str(num1) + " y " + str(num2) + " es: " + str(mcm))
    print""

    tecla = raw_input("Presione <ENTER> para seguir en el programa, [0]--> para salir ......")
    if tecla == "0":
        salir()
    else:

        main()


def numep():
    print"    ###########################################"
    print"    #####    NUMERO ELEVADO A POTENCIA    #####"
    print"    ###########################################"
    print""
    valor = float(input("Ingrese un valor entero o decimal (ejemplo: 12.5): "))
    print""
    potencia = int(input("elevado a: "))
    r2 = pow(valor, potencia)
    print""
    print"El resultado de", valor, "elevado a", potencia, "es:", r2
    print""
    tecla = raw_input("Presione <ENTER> para seguir en el programa, [0]--> para salir ......")
    if tecla == "0":
        salir()
    else:

        main()


def esprimo(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


def sinoprimo():
    print"    ################################################"
    print"    #####    AVERIGUA SI UN NUMERO ES PRIMO    #####"
    print"    ################################################"
    print""
    num = int(input("Ingrese un numero entero: "))
    print""
    result = esprimo(num)

    if result is True:
        print"El Numero", num, "es primo"
        print""
    else:
        print"El numero", num, "no es primo"
        print""

    tecla = raw_input("Presione <ENTER> para seguir en el programa, [0]--> para salir ......")
    if tecla == "0":
        salir()
    else:

        main()


def raiz():
    print"    ########################################"
    print"    #####    HALLA LA RAIZ CUADRADA    #####"
    print"    ########################################"
    print""

    valor = float(input("Ingrese un valor entero o decimal (ejemplo: 12.5): "))
    r1 = math.sqrt(valor)
    print ""
    print"La raiz cuadrada de", valor, "es:", r1
    print ""

    tecla = raw_input("Presione <ENTER> para seguir en el programa, [0]--> para salir ......")
    if tecla == "0":
        salir()
    else:

        main()


def simplfrac():
    global input
    print"    #######################################"
    print"    #####    SIMPLIFICA FRACCIONES    #####"
    print"    #######################################"
    print""
    try:
        input = raw_input
    except NameError:
        pass
    while True:
        input_value = input("Ingrese una fraccion (-3/5, por ejemplo): ")
        try:
            fraction = Fraction(input_value)
        except ValueError:
            print("¡Eso no es una fraccion!")
        except ZeroDivisionError:
            print("El denominador no puede ser 0.")
        else:
            break
    print""
    print"Fraccion simplificada:", (fraction)
    print""

    tecla = raw_input("Presione <ENTER> para seguir en el programa, [0]--> para salir ......")
    if tecla == "0":
        salir()
    else:

        main()


# Funcion para la Hipotenusa

def hipo():
    print"    ###################################################"
    print"    #####    HALLA LA HIPOTENUSA DEL TRIANGULO    #####"
    print"    ###################################################"
    print""

    C1 = float(input("Ingrese el valor del primer cateto: "))
    C2 = float(input("Ingrese el valor del segundo cateto: "))
    hipotenusa = math.hypot(C1, C2)

    print""
    print"La hipotenusa es: ", hipotenusa


# Funcion para el cateto

def cate():
    print"    ##################################################"
    print"    #####      HALLA EL CATETO DEL TRIANGULO     #####"
    print"    ##################################################"
    print""

    H1 = float(input("Ingrese el valor de la hipotenusa: "))
    C1 = float(input("Ingrese el valor del cateto conocido: "))

    if H1 < C1:
        cateto = math.sqrt((C1 * C1) - (H1 * H1))
    else:
        cateto = math.sqrt((H1 * H1) - (C1 * C1))
    print""
    print"El segundo cateto es: ", cateto


# Bucle del menu y opciones

def pita():
    limpiar()
    while 1:

        print""
        print""
        print"    #################################################################"
        print"    ####                                                         ####"
        print"    ####                 TEOREMA DE PITAGORAS                    ####"
        print"    ####                                                         ####"
        print"    ####            Halla la hipotenusa o el Cateto              ####"
        print"    ####                    del triangulo                        ####"
        print"    ####---------------------------------------------------------####"
        print"    ####                                                         ####"
        print"    ####     1 - Hallar valor de la hipotenusa                   ####"
        print"    ####     2 - Hallar valor del cateto                         ####"
        print"    ####     0 - Salir                                           ####"
        print"    ####                                                         ####"
        print"    #################################################################"
        print""

        # Bloque para manejar opciones

        Opcion = raw_input("Selecciona la opcion deseada (1-2-0): ")
        print""
        if Opcion != "1" and Opcion != "2" and Opcion != "0":
            print "Opcion incorrecta, presione <ENTER> para volver al menu ...."
            raw_input()
            pita()

        elif Opcion == "0":
            main()
        if Opcion == "1":
            limpiar()
            hipo()
        else:
            limpiar()
            cate()


def main():

    limpiar()

    print"    #######################################"
    print"    #     Un poco de matematicas v1.0     #"
    print"    #                                     #"
    print"    #           by Enri_Python            #"
    print"    #                                     #"
    print"    #######################################"
    print"    #                                     #"
    print"    #           MENU PRINCIPAL            #"
    print"    #                                     #"
    print"    #######################################"
    print"    #                                     #"
    print"    #  1 - Ecuaciones segundo grado       #"
    print"    #                                     #"
    print"    #  2 - TODOS LOS DIVISORES            #"
    print"    #                                     #"
    print"    #  3 - Calcula el factorial           #"
    print"    #                                     #"
    print"    #  4 - OPERACIONES CON FRACCIONES     #"
    print"    #                                     #"
    print"    #  5 - Conversor de longitud          #"
    print"    #                                     #"
    print"    #  6 - MAXIMO COMUN DIVISOR (MCD)     #"
    print"    #                                     #"
    print"    #  7 - minimo comun multiplo (mcm)    #"
    print"    #                                     #"
    print"    #  8 - NUMERO ELEVADO A POTENCIA      #"
    print"    #                                     #"
    print"    #  9 - Numeros primos                 #"
    print"    #                                     #"
    print"    # 10 - RAIZ CUADRADA                  #"
    print"    #                                     #"
    print"    # 11 - Simplificar fraccion           #"
    print"    #                                     #"
    print"    # 12 - HIPOTENUSA Y CATETO            #"
    print"    #                                     #"
    print"    #  0 - Salir del programa             #"
    print"    #                                     #"
    print"    #######################################"
    print""
    print""

    opcion = raw_input("ELIGE UNA OPCION DEL MENU PRINCIPAL (DEL 1 AL 12 o [0] = SALIR ---->> ")

    print""
    print""

    if opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4" and opcion != "5" and opcion != "6" and opcion != "7" and opcion != "8" and opcion != "9" and opcion != "10" and opcion != "11" and opcion != "12" and opcion != "0":

        print "Opcion incorrecta, presione <ENTER> para volver al menu ...."

        raw_input()

        main()

    elif opcion == "0":
        salir()

    elif opcion == "1":
        equa()

    elif opcion == "2":
        divisor()

    elif opcion == "3":
        factor()

    elif opcion == "4":
        fraccion()

    elif opcion == "5":
        longi()

    elif opcion == "6":
        maxcd()

    elif opcion == "7":
        mincm()

    elif opcion == "8":
        numep()

    elif opcion == "9":
        sinoprimo()

    elif opcion == "10":
        raiz()

    elif opcion == "11":
        simplfrac()

    elif opcion == "12":
        pita()


main()







