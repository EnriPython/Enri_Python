#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Importando modulos

import math
from math import factorial
from math import pow
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
    print"     Saliendo del programa .........."
    time.sleep(2)
    limpiar()
    sys.exit()


def equa():
    limpiar()
    print""
    print""
    print"       ##################################################################################"
    print"       #####                                                                        #####"
    print"       #####                 RESUELVE ECUACIONES DE SEGUNDO GRADO                   #####"
    print"       #####                                                                        #####"
    print"       #####   Ejemplo (1):  x(elevado a 2)-5x+6=0  -->  ingrese: A:1  B:-5  C:6    #####"
    print"       #####                                                                        #####"
    print"       #####   Ejemplo (2):  2x(elevado a 2)-7x+3=0  --> ingrese: A:2  B:-7  C:3    #####"
    print"       #####                                                                        #####"
    print"       ##################################################################################"
    print""

    a = float(input("     Ingrese el valor de A (cociente del termino cuadratico): "))  # a = cociente del termino cuadratico
    print""
    b = float(input("     Ingrese el valor de B (cociente de termino lineal): "))  # b = cociente de termino lineal
    print""
    c = float(input("     Ingrese el valor de C (cociente de termino independiente): "))  # c = cociente de termino independiente
    print""

    # resolviendo

    x = (b ** 2) - (4 * a * c)

    # Si x es menor que 0, no tendra una solucion dentro de las reglas de los numeros reales

    if x < 0:
        print"     Solucion solo en numeros complejos"

    x1 = (-b + math.sqrt(x)) / (2 * a)
    x2 = (-b - math.sqrt(x)) / (2 * a)

    # resultado

    # Mostramos ambos valores

    print"     X1= ", x1
    print"     X2= ", x2
    print""
    print""

    tecla = raw_input("     Presione <ENTER> para seguir en el programa, [0]--> para volver al menu principal ......> ")
    if tecla == "0":
        main()
    else:

        equa()


def divisor():
    limpiar()
    print""
    print""
    print"    ###############################################################"
    print"    #####    HALLA TODOS LOS DIVISORES DE UN NUMERO ENTERO    #####"
    print"    ###############################################################"
    print""
    print""
    numero = int(input("     Ingresa un numero entero: "))
    divis = 0

    print""
    print"     Divisores de:", numero
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
                print"    ", (int(divis))
            else:
                print""
                print("     %d," % divis)
    print""
    print"     1"
    print""
    print""
    tecla = raw_input("     Presione <ENTER> para seguir en el programa, [0]--> para volver al menu principal ......> ")
    if tecla == "0":
        main()
    else:

        divisor()


def factor():
    limpiar()
    print""
    print""
    print"    ##########################################################"
    print"    #####    CALCULA EL FACTORIAL DE UN NUMERO ENTERO    #####"
    print"    ##########################################################"
    print""
    print""
    valor = int(input("     Ingrese un numero entero: "))
    resu = factorial(valor)
    print ""
    print"     El factorial de", valor, "es:", resu
    print""
    print""
    tecla = raw_input("     Presione <ENTER> para seguir en el programa, [0]--> para volver al menu principal ......> ")
    if tecla == "0":
        main()
    else:

        factor()


def fraccion():
    limpiar()
    print""
    print""
    print"    ########################################################"
    print"    #####        OPERACIONES CON 2 FRACCIONES          #####"
    print"    #####    suma, resta, multiplicacion y division    #####"
    print"    ########################################################"
    print""
    print""
    f1 = raw_input("     Introduce la primera fraccion <numerador/denominador> (ejemplo: 3/4): ")
    print""
    f2 = raw_input("     Introduce la segunda fraccion <numerador/denominador> (ejemplo: 1/5): ")
    print""
    print""

    SumaFrac = Fraction(f1) + Fraction(f2)
    print"     La suma da: ", SumaFrac, "\n"

    RestaFrac = Fraction(f1) - Fraction(f2)
    print"     La resta da: ", RestaFrac, "\n"

    MultiFrac = Fraction(f1) * Fraction(f2)
    print"     La multiplicacion da: ", MultiFrac, "\n"

    DiviFrac = Fraction(f1) / Fraction(f2)
    print"     La division da: ", DiviFrac, "\n"
    print""
    print""
    tecla = raw_input("     Presione <ENTER> para seguir en el programa, [0]--> para volver al menu principal ......> ")
    if tecla == "0":
        main()
    else:

        fraccion()


def longi():
    limpiar()
    print""
    print""
    print"    #################################################################"
    print"    ####                                                         ####"
    print"    ####                 CONVERSOR DE LONGITUDES                 ####"
    print"    ####                                                         ####"
    print"    ####   SELECCIONE UNIDAD DE LONGITUD PARA ENTRADA DE DATOS   ####"
    print"    ####                                                         ####"
    print"    #################################################################"
    print""
    print""

    opcion = raw_input('     Elige opcion < mm, cm, dm, m, Dm, Hm, km, [0] para volver al menu principal ......> ')

    if opcion != "mm" and opcion != "cm" and opcion != "dm" and opcion != "m" and opcion != "Dm" and opcion != "Hm" and opcion != "km" and opcion != "0":

        print""
        print "     Opcion incorrecta, presione la tecla <ENTER> para continuar..."

        raw_input()
        longi()


    elif opcion == "0":
        print ""
        print "     #####   SALIENDO DEL CONVERSOR DE LONGITUDES ...........    #####"
        print ""
        print ""
        time.sleep(2)

        main()

    print""

    cantidad = float(raw_input('     indica una cantidad: '))

    if opcion == 'mm':
        print""
        print '     Calculando..............', cantidad, opcion
        print""

        print"     ", cantidad / 10, 'centimetros'

        print"     ", cantidad / 100, 'decimetros'

        print"     ", cantidad / 1000, 'metros'

        print"     ", cantidad / 10000, 'Decametros'

        print"     ", cantidad / 100000, 'Hectometros'

        print"     ", cantidad / 1000000, 'kilometros'
    print""



    if opcion == 'cm':
        print""
        print '     Calculando..............', cantidad, opcion
        print""

        print"     ", cantidad * 10, 'milimetros'

        print"     ", cantidad / 10, 'decimetros'

        print"     ", cantidad / 100, 'metros'

        print"     ", cantidad / 1000, 'Decametros'

        print"     ", cantidad / 10000, 'Hectometros'

        print"     ", cantidad / 100000, 'kilometros'
    print""


    if opcion == 'dm':
        print""
        print '     Calculando..............', cantidad, opcion
        print""

        print"     ", cantidad * 100, 'milimetros'

        print"     ", cantidad * 10, 'centimetros'

        print"     ", cantidad / 10, 'metros'

        print"     ", cantidad / 100, 'Decametros'

        print"     ", cantidad / 1000, 'Hectometros'

        print"     ", cantidad / 10000, 'kilometros'
    print""


    if opcion == 'm':
        print""
        print '     Calculando..............', cantidad, opcion
        print""

        print"     ", cantidad * 1000, 'milimetros'

        print"     ", cantidad * 100, 'centimetros'

        print"     ", cantidad * 10, 'decimetros'

        print"     ", cantidad / 10, 'Decametros'

        print"     ", cantidad / 100, 'Hectometros'

        print"     ", cantidad / 1000, 'kilometros'
    print""


    if opcion == 'Dm':
        print""
        print '     Calculando..............', cantidad, opcion
        print""

        print"     ", cantidad * 10000, 'milimetros'

        print"     ", cantidad * 1000, 'centimetros'

        print"     ", cantidad * 100, 'decimetros'

        print"     ", cantidad * 10, 'metros'

        print"     ", cantidad / 10, 'Hectometros'

        print"     ", cantidad / 100, 'kilometros'
    print""


    if opcion == 'Hm':
        print""
        print '     Calculando..............', cantidad, opcion
        print""

        print"     ", cantidad * 100000, 'milimetros'

        print"     ", cantidad * 10000, 'centimetros'

        print"     ", cantidad * 1000, 'decimetros'

        print"     ", cantidad * 100, 'metros'

        print"     ", cantidad * 10, 'Decametros'

        print"     ", cantidad / 10, 'kilometros'
    print""


    if opcion == 'km':
        print""
        print '     Calculando..............', cantidad, opcion
        print""

        print"     ", cantidad * 1000000, 'milimetros'

        print"     ", cantidad * 100000, 'centimetros'

        print"     ", cantidad * 10000, 'decimetros'

        print"     ", cantidad * 1000, 'metros'

        print"     ", cantidad * 100, 'Decametros'

        print"     ", cantidad * 10, 'Hectometros'
    print""

    tecla = raw_input("     Presione <ENTER> para seguir en el programa, [0]--> para volver al menu principal ......> ")
    if tecla == "0":
        main()
    else:

        longi()


def maxcd():
    limpiar()
    print""
    print""
    global res
    print"    ###############################################"
    print"    #####    HALLA EL MAXIMO COMUN DIVISOR    #####"
    print"    ###############################################"
    print""
    print""
    # pedimos al usuario que ingrese los numeros
    num1 = int(raw_input("     Ingrese el primer numero entero: "))
    print""
    print""
    num2 = int(raw_input("     Ingrese el segundo numero entero: "))
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
    print('     El Maximo comun divisor de {0} y {1} es: {2}'.format(num1, num2, res))
    print""

    tecla = raw_input("     Presione <ENTER> para seguir en el programa, [0]--> para volver al menu principal ......> ")
    if tecla == "0":
        main()
    else:

        maxcd()


def mincm():
    limpiar()
    print""
    print""
    global mcd, mcm
    print"    ###############################################"
    print"    #####    HALLA EL MINIMO COMUN MULTIPLO    ####"
    print"    ###############################################"
    print""
    print""

    num1 = int(raw_input("     Ingrese el primer numero entero: "))
    print""
    num2 = int(raw_input("     Ingrese el segundo numero entero: "))

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
    print""
    print("     El minimo comun multiplo entre " + str(num1) + " y " + str(num2) + " es: " + str(mcm))
    print""
    print""

    tecla = raw_input("     Presione <ENTER> para seguir en el programa, [0]--> para volver al menu principal ......> ")
    if tecla == "0":
        main()
    else:

        mincm()


def numep():
    limpiar()
    print""
    print""
    print"    ###########################################"
    print"    #####    NUMERO ELEVADO A POTENCIA    #####"
    print"    ###########################################"
    print""
    print""
    valor = float(input("     Ingrese un valor entero o decimal (ejemplo: 12.5): "))
    print""
    potencia = int(input("     elevado a: "))
    r2 = pow(valor, potencia)
    print""

# round redondea a dos decimales el valor que devuelve <r2>
    print"     El resultado de", valor, "elevado a", potencia, "es:", round(r2, 2)
    print""
    print""
    tecla = raw_input("     Presione <ENTER> para seguir en el programa, [0]--> para volver al menu principal ......> ")
    if tecla == "0":
        main()
    else:

        numep()

# resuelve si un numero es primo o no


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
    limpiar()
    print""
    print""
    print"    ################################################"
    print"    #####    AVERIGUA SI UN NUMERO ES PRIMO    #####"
    print"    ################################################"
    print""
    num = int(input("     Ingrese un numero entero: "))
    print""
    result = esprimo(num)

    if result is True:
        print"     El Numero", num, "es primo"
        print""
    else:
        print"     El numero", num, "no es primo"
        print""

    tecla = raw_input("     Presione <ENTER> para seguir en el programa, [0]--> para volver al menu principal ......> ")
    if tecla == "0":
        main()
    else:

        sinoprimo()

# fin resuelve si un numero es primo o no


def raiz():
    limpiar()
    print""
    print""
    print"    ########################################"
    print"    #####    HALLA LA RAIZ CUADRADA    #####"
    print"    ########################################"
    print""

    valor = float(input("     Ingrese un valor entero o decimal (ejemplo: 12.5): "))
    r1 = math.sqrt(valor)
    print ""
    print"     La raiz cuadrada de", valor, "es:", round(r1, 2)
    print ""

    tecla = raw_input("     Presione <ENTER> para seguir en el programa, [0]--> para volver al menu principal ......> ")
    if tecla == "0":
        main()
    else:

        raiz()


global input


def simplfrac():
    limpiar()
    print""
    print""
    global input
    print"     #######################################"
    print"     #####    SIMPLIFICA FRACCIONES    #####"
    print"     #######################################"
    print""
    print""
    try:
        input = raw_input
    except NameError:
        pass
    while True:
        print""
        input_value = input("     Ingrese una fraccion (15/6, por ejemplo): ")
        try:
            fraction = Fraction(input_value)
        except ValueError:
            print""
            print("     Eso no es una fraccion......")
        except ZeroDivisionError:
            print""
            print("     El denominador no puede ser 0.")
        else:
            break
    print""
    print"     Fraccion simplificada:", (fraction)
    print""

    tecla = raw_input("     Presione <ENTER> para seguir en el programa, [0]--> para volver al menu principal ......> ")
    if tecla == "0":
        main()
    else:

        simplfrac()

# Teorema de Pitagoras
# Funcion para la Hipotenusa


def hipo():
    limpiar()
    print""
    print""
    print"    ###################################################"
    print"    #####    HALLA LA HIPOTENUSA DEL TRIANGULO    #####"
    print"    ###################################################"
    print""

    C1 = float(input("     Ingrese el valor del primer cateto: "))
    print""
    C2 = float(input("     Ingrese el valor del segundo cateto: "))
    hipotenusa = round(math.hypot(C1, C2), 2)

    print""
    print"     La hipotenusa es: ", hipotenusa
    print""
    tecla = raw_input("     Presione <ENTER> para seguir en el Teorema de Pitagoras, [0]--> para volver al menu principal ......> ")
    if tecla == "0":
        main()
    else:

        pita()


# Funcion para el cateto

def cate():
    limpiar()
    print""
    print""
    print"    ##################################################"
    print"    #####      HALLA EL CATETO DEL TRIANGULO     #####"
    print"    ##################################################"
    print""

    H1 = float(input("     Ingrese el valor de la hipotenusa: "))
    print""
    C1 = float(input("     Ingrese el valor del cateto conocido: "))

    if H1 < C1:
        cateto = math.sqrt((C1 * C1) - (H1 * H1))
    else:
        cateto = math.sqrt((H1 * H1) - (C1 * C1))
    print""
    print"     El segundo cateto es: ", round(cateto, 2)
    print""
    tecla = raw_input("     Presione <ENTER> para seguir en el Teorema de Pitagoras, [0]--> para volver al menu principal ......> ")
    if tecla == "0":
        main()
    else:

        pita()


# Bucle del menu y opciones

def pita():
    limpiar()
    print""
    print""
    while 1:

        print""
        print""
        print"    #################################################################"
        print"    ####                                                         ####"
        print"    ####                 TEOREMA DE PITAGORAS                    ####"
        print"    ####                                                         ####"
        print"    ####            Halla la hipotenusa o el Cateto              ####"
        print"    ####            del triangulo.                               ####"
        print"    ####---------------------------------------------------------####"
        print"    ####                                                         ####"
        print"    ####     1 - Hallar valor de la hipotenusa                   ####"
        print"    ####     2 - Hallar valor del cateto                         ####"
        print"    ####     0 - Volver al menu principal                        ####"
        print"    ####                                                         ####"
        print"    #################################################################"
        print""
        print""

        # Bloque para manejar opciones

        Opcion = raw_input("     Selecciona la opcion deseada (1-2-0): ")
        print""
        if Opcion != "1" and Opcion != "2" and Opcion != "0":
            print "     Opcion incorrecta, presione <ENTER> para volver al menu ...."
            raw_input()
            pita()

        elif Opcion == "0":
            main()
        if Opcion == "1":
            hipo()
        else:
            cate()

# Fin Teorema de Pitagoras


# Poligonos regulares


def valor_angulo():
    limpiar()
    print""
    print""
    print"     #################################################################"
    print"     #                                                               #"
    print"     #                      Poligonos regulares                      #"
    print"     #                                                               #"
    print"     #       halla los grados individuales del angulo formado        #"
    print"     #       por las caras o lados, la suma de todos los angulos     #"
    print"     #       internos, el numero total de diagonales y las           #"
    print"     #       diagonales desde un vertice.                            #"
    print"     #                                                               #"
    print"     #################################################################"
    print""
    print""
    n = float(input("     Cuantos lados tiene su poligono regular? : "))
    angulointerno = (180 * (n - 2)) / n
    ainternos = 180 * (n - 2)
    anguloexterior = 360 / n
    numdiagonales = ((n ** 2) - (3 * n)) / 2
    diagonalesdelvertice = n - 3
    l = int(n)

    print""
    print"     El angulo interno de cada vertice del poligono regular de", l, "lados es:", round(angulointerno, 2), "grados"
    print""
    print"     La suma de todos los angulos internos es de:", round(ainternos, 2), "grados"
    print""
    print"     El angulo exterior de cada vertice es:", round(anguloexterior, 2), "grados"
    print""
    print"     La suma de los angulos de los", l, "vertices exteriores tiene que dar 360 grados (", round(anguloexterior, 2), "x", l, "= 360 grados??? )"
    print""
    print"     El numero total de diagonales es:", numdiagonales
    print""
    print"     El numero de diagonales desde un vertice es:", diagonalesdelvertice
    print""

    tecla = raw_input("     Presione <ENTER> para seguir en poligonos regulares, [0]--> para volver al menu principal ......> ")
    if tecla == "0":
        main()
    else:

        valor_angulo()

# Fin poligonos regulares

# Trigonometria


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


    tecla = raw_input("     Presione <ENTER> para continuar en el programa, [0]--> para volver al menu principal ......> ")
    if tecla == "0":
        main()
    else:

        trigo()


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
    print'     Los grados convertidos a radianes dan:', round((math.radians(math.degrees(rad))), 5), 'radianes'
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


    tecla = raw_input("     Presione <ENTER> para continuar en el programa, [0]--> para volver al menu principal ......> ")
    if tecla == "0":
        main()
    else:

        trigo()


def trigo():
    limpiar()
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
    unidad = raw_input("     Como va a introducir el valor del angulo?, [r] = radianes, [g] = grados, [0] para volver al menu principal ......>  ")
    if unidad != "r" and unidad != "g" and unidad != "0":
        print""
        print "     Opcion incorrecta, presione <ENTER> para volver al menu ...."
        raw_input()

        trigo()


    if unidad == "r":
        radian()

    if unidad == "g":
        grados()


    if unidad == "0":
        main()

# Fin trigonometria

# Algebra vectorial


def magnitud():
    print""
    print"     Escriba las coordenadas cartesianas, numero positivo, negativo o cero con dos decimales"
    print""
    x = float(input("     Ingrese el valor del vector < x > "))
    print""
    y = float(input("     Ingrese el valor del vector < y > "))
    print""
    z = float(input("     Ingrese el valor del vector < z > "))
    mg = math.sqrt(x**2 + y**2 + z**2)
    mag = round(mg, 2)
    print""
    print"     La magnitud del vector", x, y, z, "es: ", mag
    print""
    print""
    tecla = raw_input("     Presione <ENTER> para continuar en el programa, [0]--> para volver al menu principal ......> ")
    if tecla == "0":
        main()
    else:

        algebra()


def angulos():
    print""
    print"     escriba las coordenadas cartesianas, numero positivo, negativo o cero con dos decimales"
    print""
    x = float(input("     Ingrese el valor del vector < x > "))
    print""
    y = float(input("     Ingrese el valor del vector < y > "))
    print""
    z = float(input("     Ingrese el valor del vector < z > "))
    Ar = math.atan2(y, x)
    A = math.degrees(Ar)
    Br = math.atan2(math.sqrt(x**2 + y**2), z)
    B = math.degrees(Br)
    print""
    print"     Los angulos A y B  en grados del vector", x, y, z, " son: A=", round(A, 2), " B=", round(B, 2)
    print""
    print""
    tecla = raw_input("     Presione <ENTER> para continuar en el programa, [0]--> para volver al menu principal ......> ")
    if tecla == "0":
        main()
    else:

        algebra()


def mas_menos():
    print""
    print"     Escriba las coordenadas cartesianas, numero positivo, negativo o cero con dos decimales"
    print""
    x1 = float(input("     Ingrese el valor del vector < x1 > "))
    print""
    y1 = float(input("     Ingrese el valor del vector < y1 > "))
    print""
    z1 = float(input("     Ingrese el valor del vector < z1 > "))
    print""
    x2 = float(input("     Ingrese el valor del vector < x2 > "))
    print""
    y2 = float(input("     Ingrese el valor del vector < y2 > "))
    print""
    z2 = float(input("     Ingrese el valor del vector < z2 > "))
    suma = x1 + x2, y1 + y2, z1 + z2
    resta = x1 - x2, y1 - y2, z1 - z2
    print""
    print "     La suma y la resta de los vectores", x1, y1, z1, "y", x2, y2, z2, "es, SUMA:", suma, " RESTA:", resta
    print""
    print""
    tecla = raw_input("     Presione <ENTER> para continuar en el programa, [0]--> para volver al menu principal ......> ")
    if tecla == "0":
        main()
    else:

        algebra()


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
    tecla = raw_input("     Presione <ENTER> para continuar en el programa, [0]--> para volver al menu principal ......> ")
    if tecla == "0":
        main()
    else:

        algebra()


def algebra():
    limpiar()
    print""
    print""
    print"     ###########################################################################"
    print"     #                                                                         #"
    print"     #                           ALGEBRA VECTORIAL                             #"
    print"     #                                                                         #"
    print"     #               Magnitud, angulos, suma, resta y productos                #"
    print"     #                                                                         #"
    print"     ###########################################################################"
    print""
    print""
    print"     1- MAGNITUD"
    print""
    print"     2- ANGULOS"
    print""
    print"     3- MAS_MENOS"
    print""
    print"     4- PRODUCTO"
    print""
    print"     0- Volver al menu principal"
    print""
    print""
    opcion = raw_input("     Ingresa un numero del menu ---> ")
    print""

    if opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4" and opcion != "0":
        print "     Opcion incorrecta, presione <ENTER> para volver al menu ...."

        raw_input()

        algebra()


    if opcion == "1":

        magnitud()

    if opcion == "2":

        angulos()

    if opcion == "3":

        mas_menos()

    if opcion == "4":

        producto()

    if opcion == "0":

        main()


# fin algebra vectorial

# inicio area y volumen de figuras geometricas


def cuadrado():
    limpiar()
    print""
    print""
    print"     #######################################################"
    print"     #########    AREA DEL CUADRADO    #####################"
    print"     #######################################################"
    print""
    l = float(input("     Cuanto mide el lado del cuadrado?: "))
    a = l * l
    print""
    print"     El area del cuadrado es: " + str(a) + "\n"
    print""
    tecla = raw_input("     Presione <ENTER> para continuar con otra figura geometrica, [0]--> para volver al menu principal -----> ")
    if tecla == "0":
        main()
    else:

        arevol()


def rectangulo():
    limpiar()
    print""
    print""
    print"     #######################################################"
    print"     #########    AREA DEL RECTANGULO    ###################"
    print"     #######################################################"
    print""
    l = float(input("     Cuanto mide el largo del Rectangulo?: "))
    print""
    ar = float(input("     Cuanto mide el ancho del rectangulo?: "))
    a = ar * l
    print""
    print"     El area del Rectangulo es: ", a
    print""
    tecla = raw_input("     Presione <ENTER> para continuar con otra figura geometrica, [0]--> para volver al menu principal -----> ")
    if tecla == "0":
        main()
    else:

        arevol()


def rombo():
    limpiar()
    print""
    print""
    print"     #######################################################"
    print"     #########    AREA DEL ROMBO    ########################"
    print"     #######################################################"
    print""
    lma = float(input("     Cuanto mide la diagonal mayor?: "))
    print""
    lm = float(input("     Cuanto mide la diagonal menor?: "))
    a = (lma * lm) / 2
    print""
    print"     El area del rombo es:  ", a
    print""
    tecla = raw_input("     Presione <ENTER> para continuar con otra figura geometrica, [0]--> para volver al menu principal -----> ")
    if tecla == "0":
        main()
    else:

        arevol()


def triangulo():
    limpiar()
    print""
    print""
    print"     #######################################################"
    print"     #########    AREA DEL TRIANGULO    ####################"
    print"     #######################################################"
    print""
    b = float(input("     Cuanto mide la base?: "))
    print""
    h = float(input("     Cuanto mide la altura?: "))
    a = (b * h) / 2
    print""
    print"     El area del triangulo es: ", a
    print""
    tecla = raw_input("     Presione <ENTER> para continuar con otra figura geometrica, [0]--> para volver al menu principal -----> ")
    if tecla == "0":
        main()
    else:

        arevol()


def romboide():
    limpiar()
    print""
    print""
    print"     #######################################################"
    print"     #########    AREA DEL ROMBOIDE#########################"
    print"     #######################################################"
    print""
    b = float(input("     Cuanto mide la base?: "))
    print""
    h = float(input("     Cuanto mide la altura?: "))
    a = b * h
    print""
    print"     El area del romboide es: ", a
    print""
    tecla = raw_input("     Presione <ENTER> para continuar con otra figura geometrica, [0]--> para volver al menu principal -----> ")
    if tecla == "0":
        main()
    else:

        arevol()


def trapecio(tecla=None):
    limpiar()
    print""
    print""
    print"     #######################################################"
    print"     #########    AREA DEL TRAPECIO    #####################"
    print"     #######################################################"
    print""
    bma = float(input("     Cuanto mide la base mayor?: "))
    print""
    b = float(input("     Cuanto mide la base menor?: "))
    print""
    h = float(input("     Cuanto mide la altura?: "))
    a = h * (bma + b) / 2
    print""
    print"     El area del trapecio es: ", a
    print""
    raw_input("     Presione <ENTER> para continuar con otra figura geometrica, [0]--> para volver al menu principal -----> ")
    if tecla == "0":
        main()
    else:

        arevol()


def poligono():
    limpiar()
    print""
    print""
    print"     #######################################################"
    print"     #########    AREA DEL POLIGONO REGULAR    #############"
    print"     #######################################################"
    print""
    n = int(input("     Cuantos lados tiene el polígono?: "))
    print""
    l = float(input("     Cuanto mide cada lado?: "))
    print""
    g = (360 / n)
    ap = round(l / (2 * math.tan(math.radians(g / 2))), 3)
    a = n * l * ap / 2
    print"     El area del Polígono regular es: ", a
    print""
    tecla = raw_input("     Presione <ENTER> para continuar con otra figura geometrica, [0]--> para volver al menu principal -----> ")
    if tecla == "0":
        main()
    else:

        arevol()


def circulo():
    limpiar()
    print""
    print""
    print"     #######################################################"
    print"     #########    AREA DEL CIRCULO    ######################"
    print"     #######################################################"
    print""
    r = float(input("     Cuanto mide el Radio?: "))
    a = (math.pi * (r ** 2))
    print""
    print"     El area del circulo es: ", a
    print""
    tecla = raw_input("     Presione <ENTER> para continuar con otra figura geometrica, [0]--> para volver al menu principal -----> ")
    if tecla == "0":
        main()
    else:

        arevol()


def corona():
    limpiar()
    print""
    print""
    print"     #######################################################"
    print"     #########    AREA DE LA CORONA CIRCULAR    ############"
    print"     #######################################################"
    print""
    rma = float(input("     Cuanto mide el radio mayor?: "))
    print""
    r = float(input("     Cuanto mide el radio menor?: "))
    a = math.pi * ((rma ** 2) - (r + +2))
    print""
    print"     El area de la corona es: ", a
    print""
    tecla = raw_input("     Presione <ENTER> para continuar con otra figura geometrica, [0]--> para volver al menu principal -----> ")
    if tecla == "0":
        main()
    else:

        arevol()


def sector():
    limpiar()
    print""
    print""
    print"     #######################################################"
    print"     #########    AREA DEL SECTOR CIRCULAR    ##############"
    print"     #######################################################"
    print""
    n = float(input("     Cuantos grados tiene el angulo formado entre los dos radios?: "))
    print""
    r = float(input("     Cuanto mide el radio?: "))
    a = (math.pi * (r ** 2) * n) / 360
    print""
    print"     El area del sector circular es: ", a
    print""
    tecla = raw_input("     Presione <ENTER> para continuar con otra figura geometrica, [0]--> para volver al menu principal -----> ")
    if tecla == "0":
        main()
    else:

        arevol()


def cubo():
    limpiar()
    print""
    print""
    print"     #######################################################"
    print"     #########    AREA Y VOLUMEN DEL CUBO    ###############"
    print"     #######################################################"
    print""
    l = float(input("     Cuanto mide el lado?: "))
    a = 6 * (l ** 2)
    v = (l ** 3)
    print""
    print"     El area del cubo es: ", a
    print""
    print"     El volumen del cubo es: ", v
    print""
    tecla = raw_input("     Presione <ENTER> para continuar con otra figura geometrica, [0]--> para volver al menu principal -----> ")
    if tecla == "0":
        main()
    else:

        arevol()


def cilindro():
    limpiar()
    print""
    print""
    print"     #######################################################"
    print"     #########    AREA Y VOLUMEN DEL CILINDRO    ###########"
    print"     #######################################################"
    print""
    r = float(input("     Cuanto mide el radio del cilindro?: "))
    print""
    h = float(input("     Cuanto mide la altura del cilindro?: "))
    a = (2 * math.pi * r * (h + r))
    v = (math.pi * (r ** 2) * h)
    print""
    print"     El area del  cilindro es: ", a
    print""
    print"     El volumen del cilindro es: ", v
    print""
    tecla = raw_input("     Presione <ENTER> para continuar con otra figura geometrica, [0]--> para volver al menu principal -----> ")
    if tecla == "0":
        main()
    else:

        arevol()


def ortoedro():
    limpiar()
    print""
    print""
    print"     #######################################################"
    print"     #########    AREA Y VOLUMEN DEL ORTOEDRO    ###########"
    print"     #######################################################"
    print""
    an = float(input("     Cuanto mide el ancho?: "))
    print""
    l = float(input("     Cuanto mide el largo?: "))
    print""
    h = float(input("     Cuanto mide de altura?: "))
    a = 2 * ((an * l) + (an * h) + (h * l))
    v = an * l * h
    print""
    print"     El area del ortoedro es: ", a
    print""
    print"     El volumen del ortoedro es: ", v
    print""
    tecla = raw_input("     Presione <ENTER> para continuar con otra figura geometrica, [0]--> para volver al menu principal -----> ")
    if tecla == "0":
        main()
    else:

        arevol()


def cono():
    limpiar()
    print""
    print""
    print"     #######################################################"
    print"     #########    AREA Y VOLUMEN DEL CONO    ###############"
    print"     #######################################################"
    print""
    h = float(input("     Cuanto mide la altura del cono?: "))
    print""
    r = float(input("     Cuanto mide el radio del cono?: "))
    l = (math.sqrt((r ** 2) + (h ** 2)))
    a = (math.pi * r) * (l + r)
    v = (math.pi * (r ** 2) * h) / 3
    print""
    print"     El area del cono es: ", a
    print""
    print"     El volumen del cono es: ", v
    print""
    tecla = raw_input("     Presione <ENTER> para continuar con otra figura geometrica, [0]--> para volver al menu principal -----> ")
    if tecla == "0":
        main()
    else:

        arevol()


def prisma():
    limpiar()
    print""
    print""
    print"     #######################################################"
    print"     #######    AREA Y VOLUMEN DEL PRISMA REGULAR    #######"
    print"     #######################################################"
    print""
    n = int(input("     Cuantos lados tiene el prisma?: "))
    print""
    l = float(input("     Cuanto mide el lado?: "))
    print""
    h = float(input("     Cuanto mide la altura?: "))
    g = (360 / n)
    ap = round(l / (2 * math.tan(math.radians(g / 2))), 3)
    a = 2 * ((n * l) * ap / 2) + n * (l * h)
    v = (n * l) * (ap / 2) * h
    print""
    print"     El area del prisma recto es: ", a
    print""
    print"     El volumen del prisma regular es: ", v
    print""
    tecla = raw_input("     Presione <ENTER> para continuar con otra figura geometrica, [0]--> para volver al menu principal -----> ")
    if tecla == "0":
        main()
    else:

        arevol()


def tronco():
    limpiar()
    print""
    print""
    print"     #######################################################"
    print"     #######    AREA Y VOLUMEN DEL TRONCO DE CONO    #######"
    print"     #######################################################"
    print""
    h = float(input("     Cuanto mide la altura?: "))
    print""
    r = float(input("     Cuanto mide el radio menor?: "))
    print""
    rma = float(input("     Cuanto mide el radio mayor?: "))
    l = math.sqrt((h ** 2) + (rma - r) ** 2)
    a = math.pi * ((l * (rma + r)) + (rma ** 2) + (r ** 2))
    v = (math.pi * h * ((rma ** 2) + (r ** 2) + (rma * r))) / 3
    print""
    print"     El area del tronco de cono es: ", a
    print""
    print"     El volumen del tronco de cono es: ", v
    print""
    tecla = raw_input("     Presione <ENTER> para continuar con otra figura geometrica, [0]--> para volver al menu principal -----> ")
    if tecla == "0":
        main()
    else:

        arevol()


def tetraedro():
    limpiar()
    print""
    print""
    print"     #######################################################"
    print"     #####    AREA Y VOLUMEN DEL TETRAEDRO REGULAR    ######"
    print"     #######################################################"
    print""
    l = float(input("     Cuanto mide el lado?: "))
    a = (l ** 2) * math.sqrt(3)
    v = ((l ** 3) * math.sqrt(2)) / 3
    print""
    print"     El area del tetraedro es: ", a
    print""
    print"     El volumen del tetraedro es: ", v
    print""
    tecla = raw_input("     Presione <ENTER> para continuar con otra figura geometrica, [0]--> para volver al menu principal -----> ")
    if tecla == "0":
        main()
    else:

        arevol()


def esfera():
    limpiar()
    print""
    print""
    print"     #######################################################"
    print"     #########    AREA Y VOLUMEN DE LA ESFERA    ###########"
    print"     #######################################################"
    print""
    r = float(input("     Cuanto mide el radio?: "))
    a = math.pi * 4 * (r ** 2)
    v = (math.pi * 4 * (r ** 3)) / 3
    print""
    print"     El area de la esfera es: ", a
    print""
    print"     El volumen de la esfera es: ", v
    print""
    tecla = raw_input("     Presione <ENTER> para continuar con otra figura geometrica, [0]--> para volver al menu principal -----> ")
    if tecla == "0":
        main()
    else:

        arevol()


def octaedro():
    limpiar()
    print""
    print""
    print"     #######################################################"
    print"     ######    AREA y VOLUMEN DEL OCTAEDRO REGULAR    ######"
    print"     #######################################################"
    print""
    l = float(input("     Cuanto mide el lado o arista?: "))
    a = 2 * (l ** 2) * math.sqrt(3)
    v = (l ** 3) / 3 * math.sqrt(2)
    print""
    print"     El area del octaedro es: ", a
    print""
    print"     El volumen del octaedro es: ", v
    print""
    tecla = raw_input("     Presione <ENTER> para continuar con otra figura geometrica, [0]--> para volver al menu principal -----> ")
    if tecla == "0":
        main()
    else:

        arevol()


def huso():
    limpiar()
    print""
    print""
    print"     #######################################################"
    print"     #####    AREA Y VOLUMEN DEL HUSO-CUÑA ESFERICA    #####"
    print"     #######################################################"
    print""
    n = float(input("     Cuantos grados tiene el angulo formado entre los dos radios?: "))
    print""
    r = float(input("     Cuanto mide el radio?: "))
    a = (4 * math.pi * (r ** 2) * n) / 360
    v = (4 * math.pi * (r ** 3) * n) / (360 * 3)
    print""
    print"     El area del huso-cuña esferica es: ", a
    print""
    print"     El volumen del huso-cuña esferica es: ", v
    print""
    tecla = raw_input("     Presione <ENTER> para continuar con otra figura geometrica, [0]--> para volver al menu principal -----> ")
    if tecla == "0":
        main()
    else:

        arevol()


def piramide():
    limpiar()
    print""
    print""
    print"     #######################################################"
    print"     ##    AREA Y VOLUMEN DE LA PIRAMIDE CUADRANGULAR    ###"
    print"     #######################################################"
    print""
    b = float(input("     Cuanto mide la apotema de la base?: "))
    print""
    c = float(input("     Cuanto mide la apotema de base triangular?: "))
    print""
    l = float(input("     Cuanto mide el lado o arista de la base?: "))
    print""
    h = float(input("     Cuanto mide la altura?: "))
    a = ((4 * l) * (b + c)) / 2
    v = ((l ** 2) * h) / 3
    print""
    print"     El area de la piramide cuadrangular es: ", a
    print""
    print"     El Volumen de la piramide cuadrangular es: ", v
    print""
    tecla = raw_input("     Presione <ENTER> para continuar con otra figura geometrica, [0]--> para volver al menu principal -----> ")
    if tecla == "0":
        main()
    else:

        arevol()


def casquete():
    limpiar()
    print""
    print""
    print"     #######################################################"
    print"     #####    AREA Y VOLUMEN DEL CASQUETE ESFERICO    ######"
    print"     #######################################################"
    print""
    r = float(input("     Cuanto mide el radio?: "))
    print""
    h = float(input("     Cuanto mide la altura?: "))
    a = 2 * math.pi * r * h
    v = math.pi * (h ** 2) * ((3 * r) - h) * 1 / 3
    print""
    print"     El area del casquete esferico es: ", a
    print""
    print"     El volumen del casquete esferico es: ", v
    print""
    tecla = raw_input("     Presione <ENTER> para continuar con otra figura geometrica, [0]--> para volver al menu principal -----> ")
    if tecla == "0":
        main()
    else:

        arevol()


def tronpi():
    limpiar()
    print""
    print""
    print"     ############################################################"
    print"     #    AREA Y VOLUMEN DEL TRONCO DE PIRAMIDE CUADRANGULAR    #"
    print"     ############################################################"
    print""
    lma = float(input("     Cuanto mide el lado de la base mayor?: "))
    print""
    l = float(input("     Cuanto mide el lado de la base menor?: "))
    print""
    h = float(input("     Cuanto mide la altura del tronco de la piramide?: "))
    apma = lma / 2
    apm = l / 2
    ap = apma - apm
    amapma = round((math.sqrt((ap ** 2) + (h ** 2))), 3)
    abma = (lma ** 2)
    ab = (l ** 2)
    a = (((lma * 4) + (l * 4)) / 2) * amapma + (abma + ab)
    v = h / 3 * (abma + (math.sqrt(abma * ab) + ab))
    print""
    print"     El area del tronco de piramide es: ", a
    print""
    print"     El volumen del tronco de piramide es: ", v
    print""
    tecla = raw_input("     Presione <ENTER> para continuar con otra figura geometrica, [0]--> para volver al menu principal -----> ")
    if tecla == "0":
        main()
    else:

        arevol()


def zona():
    limpiar()
    print""
    print""
    print"     #######################################################"
    print"     ######    AREA Y VOLUMEN DE LA ZONA ESFERICA    #######"
    print"     #######################################################"
    print""
    rma = float(input("     Cuanto mide el radio mayor?: "))
    print""
    r = float(input("     Cuanto mide el radio menor?: "))
    print""
    h = float(input("     Cuanto mide la altura?: "))
    a = 2 * math.pi * rma * h
    v = math.pi / 6 * h * ((h ** 2) + (3 * (rma ** 2)) + (3 * (r ** 2)))
    print""
    print"     El area de la zona esferica es: ", a
    print""
    print"     El volumen de la zona esferica es: ", v
    print""
    tecla = raw_input("     Presione <ENTER> para continuar con otra figura geometrica, [0]--> para volver al menu principal -----> ")
    if tecla == "0":
        main()
    else:

        arevol()


def elipse():
    limpiar()
    print""
    print""
    print"     #######################################################"
    print"     #########    AREA DEL ELIPSE    #######################"
    print"     #######################################################"
    print""
    b = float(input("     Cuanto mide el semieje mayor?: "))
    print""
    h = float(input("     Cuanto mide el semieje menor?: "))
    pi = 3.1416
    a = pi * b * h
    print""
    print "     El area del elipse es:", a
    print""
    tecla = raw_input("     Presione <ENTER> para continuar con otra figura geometrica, [0]--> para volver al menu principal -----> ")
    if tecla == "0":
        main()
    else:

        arevol()


def toro():
    limpiar()
    print""
    print""
    print"     #######################################################"
    print"     #########    AREA Y VOLUMEN DEL TORO    ###############"
    print"     #######################################################"
    print""
    rma = float(input("     Cuanto mide el radio de la circunferencia directriz?: "))
    print""
    r = float(input("     Cuanto mide el radio del circulo generatriz?: "))
    a = 4 * (math.pi ** 2) * rma * r
    v = 2 * (math.pi ** 2) * rma * r ** 2
    print""
    print "     El area del toro es:", a
    print""
    print "     El volumen del toro es:", v
    print""
    tecla = raw_input("     Presione <ENTER> para continuar con otra figura geometrica, [0]--> para volver al menu principal -----> ")
    if tecla == "0":
        main()
    else:

        arevol()


def elipsoide():
    limpiar()
    print""
    print""
    print"     #######################################################"
    print"     #########    AREA Y VOLUMEN DEL ELIPSOIDE    ##########"
    print"     #######################################################"
    print""
    a = float(input("     Cuanto mide el radio mayor?: "))
    print""
    b = float(input("     Cuanto mide el segundo radio?: "))
    print""
    c = float(input("     Cuanto mide el tercer radio?: "))
    area = 4 * math.pi * pow(
        (pow(a, 1.6075) * pow(b, 1.6075) + pow(a, 1.6075) * pow(c, 1.6075) + pow(b, 1.6075) * pow(c, 1.6075)) / 3,
        1 / 1.6075)
    v = 4 * math.pi * a * b * c / 3
    print""
    print "     El area del elipsoide es:", area
    print""
    print "     El volumen del elipsoide es:", v
    print""
    tecla = raw_input("     Presione <ENTER> para continuar con otra figura geometrica, [0]--> para volver al menu principal -----> ")
    if tecla == "0":
        main()
    else:

        arevol()


def prisma_rect():
    limpiar()
    print""
    print""
    print"     #######################################################"
    print"     #####    AREA Y VOLUMEN DEL PRISMA RECTANGULAR    #####"
    print"     #######################################################"
    print""
    print""
    lma = float(input("     Cuanto mide el lado mayor?: "))
    print""
    l = float(input("     Cuanto mide el lado menor?: "))
    print""
    h = float(input("     Cuanto mide la altura?: "))
    a = 2 * (lma * l) + 2 * (lma * h) + 2 * (l * h)
    v = lma * l * h
    print""
    print"     El area del prisma rectangular es: ", a
    print""
    print"     El volumen del prisma rectangular es: ", v
    print""
    tecla = raw_input("     Presione <ENTER> para continuar con otra figura geometrica, [0]--> para volver al menu principal -----> ")
    if tecla == "0":
        main()
    else:

        arevol()


def arevol():
    limpiar()

    print"     ###############################################################################################################################################################################################"
    print"     #                                                                                                                                                                                             #"
    print"     #                                                                                FIGURAS GEOMETRICAS                                                                                          #"
    print"     #                                                                                                                                                                                             #"
    print"     ###############################################################################################################################################################################################"
    print"     #                                                                                                                                                                                             #"
    print"     #                                                                                                                                                                                             #"
    print"     #    [1] Area del cuadrado                            [2] Area del rectangulo                     [3] Area del rombo                           [4] Area del triangulo                         #"
    print"     #    [5] Area del romboide                            [6] Area del trapecio                       [7] Area del poligono regular                [8] Area del circulo                           #"
    print"     #    [9] Area de la corona circular                   [10] Area del sector circular               [11] Area y volumen del cubo                 [12] Area y volumen del cilindro               #"
    print"     #    [13] Area y volumen del ortoedro                 [14] Area y volumen del cono                [15] Area y volumen del prisma regular       [16] Area y volumen del tronco de cono         #"
    print"     #    [17] Area y volumen del tetraedro regular        [18] Area y volumen de la esfera            [19] Area y volumen del octaedro regular     [20] Area y volumen del huso-cuna esferica     #"
    print"     #    [21] Area y volumen de la piramide cuadrangular  [22] Area y volumen del casquete esferico   [23] Area y volumen del tronco de piramide   [24] Area y volumen de zona esferica           #"
    print"     #    [25] Area del elipse                             [26] Area y volumen del toro                [27] Area y volumen del elipsoide            [28] Area y volumen del prisma rectangular     #"
    print"     #    [0] Volver al menu principal                                                                                                                                                             #"
    print"     #                                                                                                                                                                                             #"
    print"     #                                                                                                                                                                                             #"
    print"     ###############################################################################################################################################################################################"
    print""
    print""
    opcionn = raw_input("     Ingresa un numero del menu ---> ")
    print""

    if opcionn != "1" and opcionn != "2" and opcionn != "3" and opcionn != "4" and opcionn != "5" and opcionn != "6" and opcionn != "7" and opcionn != "8" and opcionn != "9" and opcionn != "10" and opcionn != "11" and opcionn != "12" and opcionn != "13" and opcionn != "14" and opcionn != "15" and opcionn != "16" and opcionn != "17" and opcionn != "18" and opcionn != "19" and opcionn != "20" and opcionn != "21" and opcionn != "22" and opcionn != "23" and opcionn != "24" and opcionn != "25" and opcionn != "26" and opcionn != "27" and opcionn != "28" and opcionn != "0":

        print "     Opcion incorrecta, presione <ENTER> para volver al menu ----> "

        raw_input()

        arevol()

    elif opcionn == "1":

        cuadrado()

    elif opcionn == "2":

        rectangulo()

    elif opcionn == "3":

        rombo()

    elif opcionn == "4":

        triangulo()

    elif opcionn == "5":

        romboide()

    elif opcionn == "6":

        trapecio()

    elif opcionn == "7":

        poligono()

    elif opcionn == "8":

        circulo()

    elif opcionn == "9":

        corona()

    elif opcionn == "10":

        sector()

    elif opcionn == "11":

        cubo()

    elif opcionn == "12":

        cilindro()

    elif opcionn == "13":

        ortoedro()

    elif opcionn == "14":

        cono()

    elif opcionn == "15":

        prisma()

    elif opcionn == "16":

        tronco()

    elif opcionn == "17":

        tetraedro()

    elif opcionn == "18":

        esfera()

    elif opcionn == "19":

        octaedro()

    elif opcionn == "20":

        huso()

    elif opcionn == "21":

        piramide()

    elif opcionn == "22":

        casquete()

    elif opcionn == "23":

        tronpi()

    elif opcionn == "24":

        zona()

    elif opcionn == "25":

        elipse()

    elif opcionn == "26":

        toro()

    elif opcionn == "27":

        elipsoide()

    elif opcionn == "28":

        prisma_rect()

    elif opcionn == "0":

        main()

# fin area y volumen de figuras geometricas


def main():
    limpiar()
    print""
    print""
    print"     ##############################################################################"
    print"     #                       Un poco de matematicas v2.0                          #"
    print"     #                              by Enri_Python                                #"
    print"     ##############################################################################"
    print"     #                                                                            #"
    print"     #                              MENU PRINCIPAL                                #"
    print"     #                                                                            #"
    print"     #              La coma [,] para los decimales es el punto [.]                #"
    print"     ##############################################################################"
    print"     #                                      #                                     #"
    print"     #   1 - Ecuaciones segundo grado       #   11 - Simplificar fraccion         #"
    print"     #                                      #                                     #"
    print"     #   2 - TODOS LOS DIVISORES            #   12 - HIPOTENUSA Y CATETO          #"
    print"     #                                      #                                     #"
    print"     #   3 - Calcula el factorial           #   13 - Grados poligono regular      #"
    print"     #                                      #                                     #"
    print"     #   4 - OPERACIONES CON FRACCIONES     #   14 - TRIGONOMETRIA                #"
    print"     #                                      #                                     #"
    print"     #   5 - Conversor de longitud          #   15 - Algebra vectorial            #"
    print"     #                                      #                                     #"
    print"     #   6 - MAXIMO COMUN DIVISOR (MCD)     #   16 - AREA Y VOLUMEN               #"
    print"     #                                      #                                     #"
    print"     #   7 - minimo comun multiplo (mcm)    #    0 - Salir del programa           #"
    print"     #                                      #                                     #"
    print"     #   8 - NUMERO ELEVADO A POTENCIA      #                                     #"
    print"     #                                      #                                     #"
    print"     #   9 - Numero es primo?               #                                     #"
    print"     #                                      #                                     #"
    print"     #  10 - RAIZ CUADRADA                  #                                     #"
    print"     #                                      #                                     #"
    print"     ##############################################################################"
    print""
    print""

    opcion = raw_input("     ELIGE UNA OPCION DEL MENU PRINCIPAL (DEL 1 AL 16 o [0] = SALIR ---->> ")

    print""
    print""

    if opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4" and opcion != "5" and opcion != "6" and opcion != "7" and opcion != "8" and opcion != "9" and opcion != "10" and opcion != "11" and opcion != "12" and opcion != "13" and opcion != "14" and opcion != "15" and opcion != "16" and opcion != "0":

        print "     Opcion incorrecta, presione <ENTER> para volver al menu ...."

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

    elif opcion == "13":
        valor_angulo()

    elif opcion == "14":
        trigo()

    elif opcion == "15":
        algebra()

    elif opcion == "16":
        arevol()


main()
