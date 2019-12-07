#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Importamos las libreria sympy, sys y string

import sympy
from sympy import *
import sys
import string

sys.displayhook = pprint 

# Definimos los simbolos

sympy.init_printing()
x,y = sympy.symbols('x,y')


print"     #######################################################################"
print"     #                                                                     #"
print"     #   Algoritmo para la resolucion de operaciones entre 2 polinomios    #"
print"     #                                                                     #"
print"     #      multiplicacion, suma, resta, division, factorial y raiz        #"
print"     #                                                                     #"
print"     #                        Enri_Python v1.0                             #"
print"     #                                                                     #"
print"     #        Exprese el polinomio de ejemplo: 7x³ + 2x² + x + 7           #"
print"     #                                                                     #"
print"     #            bajo este formato: 7*x**3 + 2*x**2 + x - 7               #"
print"     #                                                                     #"
print"     #######################################################################"
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
		C,R = div(p1, p2)
		return [C, R]
	except:
		return "      El segundo polinomio no puede ser nulo" 

C,R = cociente(p1, p2)


# Guardamos los valores retornados por las funciones y les pasamos los 2 polinomios como parametros,  Poly1 y Poly2

resultMult = mult(Poly1, Poly2)
resultSuma = suma(Poly1, Poly2)
resultRes = res(Poly1, Poly2)
resultDiv = C
resultRest = R


# Mostramos el valor que queremos

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
 
if string.find(Poly1, "x"):

# Factoriza primer polinomio introducido y raiz

	p = sympy.simplify(Poly1)
	p_exp = p.expand()
	resultFactor = p_exp.factor()
	resuligualCero = solve(p, 'x')

	print"     El primer polinomio factorizado es: ", resultFactor
	print"     El primer polinomio igulado a cero da como raices de <x>: ", resuligualCero
	print""
	print""


if string.find(Poly2, "x"):

# Factoriza el segundo polinomio introducido y raiz

	p2 = sympy.simplify(Poly2)
	p2_exp = p2.expand()
	resultFactorp2 = p2_exp.factor()
	resuligualCerop2 = solve(p2, 'x')

	print"     El segundo polinomio factorizado es: ", resultFactorp2
	print"     El segundo polinomio igulado a cero da como raices de <x>:: ", resuligualCerop2
	print""
	print""


if string.find(resultMult, "x"):

# Factoriza el resultado de la multiplicacion y raiz

	pm = sympy.simplify(mult(Poly1, Poly2))
	pm_exp = pm.expand()
	resultFactorpm = pm_exp.factor()
	resuligualCeropm = solve(pm, 'x')

	print"     El resultado de la multiplicacion factorizado es: ", resultFactorpm
	print"     El resultado de la multiplicacion igulado a cero da como raices de <x>: ", resuligualCeropm
	print""
	print""


if string.find(resultSuma, "x"):

# Factoriza el resultado de la suma y raiz

	ps = sympy.simplify(suma(Poly1, Poly2))
	ps_exp = ps.expand()
	resultFactorps = ps_exp.factor()
	resuligualCerops = solve(ps, 'x')	
	
	print"     El resultado de la suma factorizado es: ", resultFactorps
	print"     El resultado de la suma igulado a cero da como raices de <x>: ", resuligualCerops
	print""
	print""


if string.find(resultRes, "x"):

# Factoriza el resultado de la resta y raiz

	pr = sympy.simplify(resultRes)
	pr_exp = pr.expand()
	resultFactorpr = pr_exp.factor()
	resuligualCeropr = solve(pr, 'x')

	print"     El resultado de la resta factorizado es: ", resultFactorpr
	print"     El resultado de la resta igulado a cero da como raices de <x>: ", resuligualCeropr
	print""
	print""


if string.find(resultDiv, "x"):

# Factoriza el resultado de la division y raiz

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




