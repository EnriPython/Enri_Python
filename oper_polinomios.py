#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Importamos las libreria SympY, sys y string

import sympy
from sympy import *
import sys
import string


sys.displayhook = pprint 


# Definimos los simbolos

sympy.init_printing()
x, y = sympy.symbols('x, y')


# evita que el programa se cierre en windows ante algun error de salida

def show_exception_and_exit(exc_type, exc_value, tb):
    import traceback
    traceback.print_exception(exc_type, exc_value, tb)
    raw_input("Presione <ENTER> para salir ------->")
    sys.exit(-1)


sys.excepthook = show_exception_and_exit


print"     ##########################################################################"
print"     #                                                                        #"
print"     #    Algoritmo para la resolucion de operaciones entre 2 polinomios      #"
print"     #                                                                        #"
print"     #       multiplicacion, suma, resta, division, factorial y raiz          #"
print"     #                                                                        #"
print"     #                          Enri_Python v2.0                              #"
print"     #                                                                        #"
print"     #  Exprese el polinomio de ejemplo: 7x(elevado)3 + 2x(elevado)2 + x - 7  #"
print"     #                                                                        #"
print"     #            bajo este formato: 7*x**3 + 2*x**2 + x - 7                  #"
print"     #                                                                        #"
print"     ##########################################################################"
print""

# Entrada de polinomios 

p1 = input("     Primer Polinomio: ")
p2 = input("     Segundo Polinomio: ")
print("\n")


# Luego almacenamos en varibles los dos polinomios procesados por la funcion Poly de sympy

Poly1 = sympy.Poly(p1)
Poly2 = sympy.Poly(p2)

# Declaramos una funcion para cada operacion que queramos utilizar

def mult(p1, p2):
    return p1 * p2


def suma(p1, p2):
    return p1 + p2


def res(p1, p2):
    return p1 - p2


def cociente(p1, p2):
    try:
        C, R = div(p1, p2)
        return [C, R]
    except:
        return "el segundo polinomio no puede ser nulo"


C, R = cociente(p1, p2)


# Guardamos los valores retornados por las funciones y les pasamos los 2 polinomios como parametros,  Poly1 y Poly2

resultMult = mult(Poly1, Poly2)
resultSuma = suma(Poly1, Poly2)
resultRes = res(Poly1, Poly2)
resultDiv = C
resultRest = R


# Mostramos el valor que deseemos

print"     El resultado de la multiplicacion es: ", resultMult
print""
print"     El resultado de la suma es: ", resultSuma
print""
print"     El resultado de la resta es: ", resultRes
print""
print"     El resultado de la division es: ", resultDiv
print""
print"     El resto de la division es: ", resultRest
print""
print""


# Comprobamos que el simbolo <x> esta presente en el polinomio
# Factoriza primer polinomio introducido y raiz

if string.find(Poly1, "x"):
    pa = sympy.simplify(p1)
    pa_exp = pa.expand()
    resultFactor = pa_exp.factor()
    resuligualCero = solve(pa, 'x')

    print"     El primer polinomio factorizado es: ", resultFactor
    print"     El primer polinomio igulado a cero da como raices de <x>: ", resuligualCero
    print""
    print""


# Factoriza el segundo polinomio introducido y raiz

if string.find(Poly2, "x"):
    pe = sympy.simplify(p2)
    pe_exp = pe.expand()
    resultFactorp2 = pe_exp.factor()
    resuligualCerop2 = solve(pe, 'x')

    print"     El segundo polinomio factorizado es: ", resultFactorp2
    print"     El segundo polinomio igulado a cero da como raices de <x>:: ", resuligualCerop2
    print""
    print""


# Factoriza el resultado de la multiplicacion y raiz

if string.find(resultMult, "x"):
    pm = sympy.simplify(mult(p1, p2))
    pm_exp = pm.expand()
    resultFactorpm = pm_exp.factor()
    resuligualCeropm = solve(pm, 'x')

    print"     El resultado de la multiplicacion factorizado es: ", resultFactorpm
    print"     El resultado de la multiplicacion igulado a cero da como raices de <x>: ", resuligualCeropm
    print""
    print""


# Factoriza el resultado de la suma y raiz

if string.find(resultSuma, "x"):
    pis = sympy.simplify(suma(p1, p2))
    pis_exp = pis.expand()
    resultFactorps = pis_exp.factor()
    resuligualCerops = solve(pis, 'x')

    print"     El resultado de la suma factorizado es: ", resultFactorps
    print"     El resultado de la suma igulado a cero da como raices de <x>: ", resuligualCerops
    print""
    print""


# Factoriza el resultado de la resta y raiz

if string.find(resultRes, "x"):
    pr = sympy.simplify(res(p1, p2))
    pr_exp = pr.expand()
    resultFactorpr = pr_exp.factor()
    resuligualCeropr = solve(pr, 'x')

    print"     El resultado de la resta factorizado es: ", resultFactorpr
    print"     El resultado de la resta igulado a cero da como raices de <x>: ", resuligualCeropr
    print""
    print""


# Factoriza el resultado de la division y raiz

if string.find(resultDiv, "x"):
    pd = sympy.simplify(C)
    pd_exp = pd.expand()
    resultFactorpd = pd_exp.factor()
    resuligualCeropd = solve(pd, 'x')

    print"     El resultado de la division factorizado es: ", resultFactorpd
    print"     El resultado de la division igulado a cero da como raices de <x>: ", resuligualCeropd

else:
    print""
    print""
    print"     Fin del programa ..........."


print""
print""

raw_input("         presione <ENTER> para salir del programa ---------->>>>"))
