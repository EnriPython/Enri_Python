#!/usr/bin/env python
# -*- coding: utf-8 -*-


#Modulos importados

import time

import os

import math

import sys


#Declaración de las funciones

def limpiar():

	"""Limpia la pantalla"""

	if os.name == "posix":

		os.system("clear")

	elif os.name == ("ce", "nt", "dos"):

		os.system("cls")

def salir():
	print""
	print" Saliendo del programa .........."
	time.sleep(2)
	limpiar()
	sys.exit()


def cuadrado():
	print"#######################################################"
	print("#########    AREA DEL CUADRADO    #####################")
	print"#######################################################"
	print""
	l=float(input("¿Cuanto mide el lado del cuadrado?: "))
	a=l*l
	print""
	print("El área del cuadrado es: " + str(a) +"\n")
	print""
	tecla=raw_input("Presione una tecla para continuar con otra figura geométrica, [0]--> para salir ......")
	if tecla=="0":
		salir()
	else:

		main()



def rectangulo():
	print"#######################################################"
	print("#########    AREA DEL RECTANGULO    ###################")
	print"#######################################################"
	print""
	l=float(input("¿Cuanto mide el largo del Rectángulo?: "))
	print""
	A=float(input("¿Cuanto mide el ancho del rectángulo?: "))
	a=A*l
	print""
	print"El área del Rectángulo es: ",a
	print""
	tecla=raw_input("Presione una tecla para continuar con otra figura geométrica, [0]--> para salir ......")
	if tecla=="0":
		salir()
	else:

		main()



def rombo():
	print"#######################################################"
	print("#########    AREA DEL ROMBO    ########################")
	print"#######################################################"
	print""
	lM=float(input("¿Cuanto mide el lado mayor?: "))
	print""
	lm=float(input("¿Cuanto mide el lado menor?: "))
	a=(lM*lm)/2
	print""
	print"El área del rombo es:  ",a
	print""
	tecla=raw_input("Presione una tecla para continuar con otra figura geométrica, [0]--> para salir ......")
	if tecla=="0":
		salir()
	else:

		main() 



def triangulo():
	print"#######################################################"
	print("#########    AREA DEL TRIANGULO    ####################")
	print"#######################################################"
	print""
	b=float(input("¿Cuanto mide la base?: "))
	print""
	h=float(input("Cuanto mide la altura?: "))
	a=(b*h)/2
	print""
	print"El área del triángulo es: ",a
	print""
	tecla=raw_input("Presione una tecla para continuar con otra figura geométrica, [0]--> para salir ......")
	if tecla=="0":
		salir()
	else:

		main()




def romboide():
	print"#######################################################"
	print("#########    AREA DEL ROMBOIDE#########################")
	print"#######################################################"
	print""
	b=float(input("¿Cuanto mide la base?: "))
	print""
	h=float(input("¿Cuanto mide la altura?: "))
	a=b*h
	print""
	print"El área del romboide es: ",a
	print""
	tecla=raw_input("Presione una tecla para continuar con otra figura geométrica, [0]--> para salir ......")

	main()



def trapecio():
	print"#######################################################"
	print("#########    AREA DEL TRAPECIO    #####################")
	print"#######################################################"
	print""
	B=float(input("¿Cuanto mide la base mayor?: "))
	print""
	b=float(input("¿Cuanto mide la base menor?: "))
	print""
	h=float(input("¿Cuanto mide la altura?: "))
	a=h*(B+b)/2
	print""
	print"El área del trapecio es: ",a
	print""
	raw_input("Presione una tecla para continuar con otra figura geométrica, [0]--> para salir ......")
	if tecla=="0":
		salir()
	else:

		main()



def poligono():
	print"#######################################################"
	print("#########    AREA DEL POLIGONO REGULAR    #############")
	print"#######################################################"
	print""
	n=int(input("¿Cuantos lados tiene el polígono?: "))
	print""
	l=float(input("¿Cuanto mide cada lado?: "))
	print""
	g=(360/n)
	ap=round(l/(2*math.tan(math.radians(g/2))), 3)
	a=n*l*ap/2
	print"El área del Polígono regular es: ",a
	print""
	tecla=raw_input("Presione una tecla para continuar con otra figura geométrica, [0]--> para salir ......")
	if tecla=="0":
		salir()
	else:

		main()



def circulo():
	print"#######################################################"
	print("#########    AREA DEL CIRCULO    ######################")
	print"#######################################################"
	print""
	r=float(input("¿Cuanto mide el Radio?: "))
	a=(math.pi*(r**2))
	print""
	print"El area del círculo es: ",a
	print""
	tecla=raw_input("Presione una tecla para continuar con otra figura geométrica, [0]--> para salir ......")
	if tecla=="0":
		salir()
	else:

		main()
 


def corona():
	print"#######################################################"
	print("#########    AREA DE LA CORONA CIRCULAR    ############")
	print"#######################################################"
	print""
	R=float(input("¿Cuanto mide el radio mayor?: "))
	print""
	r=float(input("¿Cuanto mide el radio menor?: "))
	a=math.pi*((R**2)-(r++2))
	print""
	print"El área de la corona es: ",a
	print""
	tecla=raw_input("Presione una tecla para continuar con otra figura geométrica, [0]--> para salir ......")
	if tecla=="0":
		salir()
	else:

		main()



def sector():
	print"#######################################################"
	print("#########    AREA DEL SECTOR CIRCULAR    ##############")
	print"#######################################################"
	print""
	n=float(input("¿Cuantos grados tiene el ángulo formado entre los dos radios?: "))
	print""
	r=float(input("¿Cuanto mide el radio?: "))
	a=(math.pi*(r**2)*n)/360
	print""
	print"El área del sector circular es: ",a
	print""
	tecla=raw_input("Presione una tecla para continuar con otra figura geométrica, [0]--> para salir ......")
	if tecla=="0":
		salir()
	else:

		main()



def cubo():
	print"#######################################################"
	print("#########    AREA Y VOLUMEN DEL CUBO    ###############")
	print"#######################################################"
	print""
	l=float(input("¿Cuanto mide el lado?: "))
	a=6*(l**2)
	v=(l**3)
	print""
	print"El área del cubo es: ",a
	print""
	print"El volumen del cubo es: ",v
	print""
	tecla=raw_input("Presione una tecla para continuar con otra figura geométrica, [0]--> para salir ......")
	if tecla=="0":
		salir()
	else:

		main()



def cilindro():
	print"#######################################################"
	print("#########    AREA Y VOLUMEN DEL CILINDRO    ###########")
	print"#######################################################"
	print""
	r=float(input("¿Cuanto mide el radio del cilindro?: "))
	print""
	h=float(input("¿Cuanto mide la altura del cilindro?: "))
	a=(2*(math.pi)*r*(h+r))
	v=(math.pi*(r**2)*h)
	print""
	print"El área del  cilindro es: ",a
	print""
	print"El volumen del cilindro es: ",v
	print""
	tecla=raw_input("Presione una tecla para continuar con otra figura geométrica, [0]--> para salir ......")
	if tecla=="0":
		salir()
	else:

		main()



def ortoedro():
	print"#######################################################"
	print("#########    AREA Y VOLUMEN DEL ORTOEDRO    ###########")
	print"#######################################################"
	print""
	A=float(input("¿Cuanto mide el ancho?: "))
	print""
	l=float(input("¿Cuanto mide el largo?: "))
	print""
	h=float(input("¿Cuanto mide de altura?: "))
	a=2*((A*l)+(A*h)+(h*l))
	v=A*l*h
	print""
	print"El área del ortoedro es: ",a
	print""
	print"El volumen del ortoedro es: ",v
	print""
	tecla=raw_input("Presione una tecla para continuar con otra figura geométrica, [0]--> para salir ......")
	if tecla=="0":
		salir()
	else:

		main()




def cono():
	print"#######################################################"
	print("#########    AREA Y VOLUMEN DEL CONO    ###############")
	print"#######################################################"
	print""
	h=float(input("¿Cuanto mide la altura del cono?: "))
	print""
	r=float(input("¿Cuanto mide el radio del cono?: "))
	l=(math.sqrt((r**2)+(h**2)))
	a=(math.pi*r)*(l+r)
	v=(math.pi*(r**2)*h)/3
	print""
	print"El área del cono es: ",a
	print""
	print"El volumen del cono es: ",v
	print""
	tecla=raw_input("Presione una tecla para continuar con otra figura geométrica, [0]--> para salir ......")
	if tecla=="0":
		salir()
	else:

		main()



def prisma():
	print"#######################################################"
	print("#######    AREA Y VOLUMEN DEL PRISMA REGULAR    #######")
	print"#######################################################"
	print""
	n=int(input("¿Cuantos lados tiene el prisma?: "))
	print""
	l=float(input("¿Cuanto mide el lado?: "))
	print""
	h=float(input("¿Cuanto mide la altura?: "))
	g=(360/n)
	ap=round(l/(2*math.tan(math.radians(g/2))), 3)
	a=2*((n*l)*ap/2)+n*(l*h)
	v=(n*l)*(ap/2)*h
	print"" 
	print"El área del prisma recto es: ",a
	print""
	print"El volumen del prisma regular es: ",v
	print""
	tecla=raw_input("Presione una tecla para continuar con otra figura geométrica, [0]--> para salir ......")
	if tecla=="0":
		salir()
	else:

		main()



def tronco():
	print"#######################################################"
	print("#######    AREA Y VOLUMEN DEL TRONCO DE CONO    #######")
	print"#######################################################"
	print""
	h=float(input("¿Cuanto mide la altura?: "))
	print""
	r=float(input("¿Cuanto mide el radio menor?: "))
	print""
	R=float(input("¿Cuanto mide el radio mayor?: "))
	l=math.sqrt((h**2)+(R-r)**2)
	a=math.pi*((l*(R+r))+(R**2)+(r**2))
	v=(math.pi*h*((R**2)+(r**2)+(R*r)))/3
	print""
	print"El área del tronco de cono es: ",a
	print""
	print"El volumen del tronco de cono es: ",v
	print""
	tecla=raw_input("Presione una tecla para continuar con otra figura geométrica, [0]--> para salir ......")
	if tecla=="0":
		salir()
	else:

		main()



def tetraedro():
	print"#######################################################"
	print("#####    AREA Y VOLUMEN DEL TETRAEDRO REGULAR    ######")
	print"#######################################################"
	print""
	l=float(input("¿Cuanto mide el lado?: "))
	a=(r**2)*math.sqrt(3)
	v=((l**3)*math.sqrt(2))/3
	print""
	print"El área del tetraedro es: ",a
	print""
	print"El volumen del tetraedro es: ",v
	print""
	tecla=raw_input("Presione una tecla para continuar con otra figura geométrica, [0]--> para salir ......")
	if tecla=="0":
		salir()
	else:

		main()



def esfera():
	print"#######################################################"
	print("#########    AREA Y VOLUMEN DE LA ESFERA    ###########")
	print"#######################################################"
	print""
	r=float(input("¿Cuanto mide el radio?: "))
	a=math.pi*4*(r**2)
	v=(math.pi*4*(r**3))/3
	print""
	print"El área de la esfera es: ",a
	print""
	print"El volumen de la esfera es: ",v
	print""
	tecla=raw_input("Presione una tecla para continuar con otra figura geométrica, [0]--> para salir ......")
	if tecla=="0":
		salir()
	else:

		main()



def octaedro():
	print"#######################################################"
	print("######    AREA y VOLUMEN DEL OCTAEDRO REGULAR    ######")
	print"#######################################################"
	print""
	l=float(input("¿Cuanto mide el lado o arista?: "))
	a=2*(l**2)*math.sqrt(3)
	v=(l**3)/3*math.sqrt(2)
	print""
	print"El área del octaedro es: ",a
	print""
	print"El volumen del octaedro es: ",v
	print""
	tecla=raw_input("Presione una tecla para continuar con otra figura geométrica, [0]--> para salir ......")
	if tecla=="0":
		salir()
	else:

		main()



def huso():
	print"#######################################################"
	print("#####    AREA Y VOLUMEN DEL HUSO-CUÑA ESFERICA    #####")
	print"#######################################################"
	print""
	n=float(input("¿Cuantos grados tiene el ángulo formado entre los dos radios?: "))
	print""
	r=float(input("¿Cuanto mide el radio?: "))
	a=(4*math.pi*(r**2)*n)/360
	v=(4*math.pi*(r**3)*n)/(360*3)
	print""
	print"El área del huso-cuña esférica es: ",a
	print""
	print"El volumen del huso-cuña esférica es: ",v
	print""
	tecla=raw_input("Presione una tecla para continuar con otra figura geométrica, [0]--> para salir ......")
	if tecla=="0":
		salir()
	else:

		main()
   
  

def piramide():
	print"#######################################################"
	print("##    AREA Y VOLUMEN DE LA PIRAMIDE CUADRANGULAR    ###")
	print"#######################################################"
	print""
	b=float(input("¿Cuanto mide la apotema de la base?: "))
	print""
	c=float(input("¿Cuanto mide la apotema de base triángular?: "))
	print""
	l=float(input("¿Cuanto mide el lado o arista de la base?: "))
	print""
	h=float(input("¿Cuanto mide la altura?: "))
	a=((4*l)*(b+c))/2
	v=((l**2)*h)/3
	print""
	print"El área de la piramide cuadrangular es: ",a
	print""
	print"El Volumen de la piramide cuadrangular es: ",v
	print""
	tecla=raw_input("Presione una tecla para continuar con otra figura geométrica, [0]--> para salir ......")
	if tecla=="0":
		salir()
	else:

		main()



def casquete():
	print"#######################################################"
	print("#####    AREA Y VOLUMEN DEL CASQUETE ESFERICO    ######")
	print"#######################################################"
	print""
	r=float(input("¿Cuanto mide el radio?: "))
	print""
	h=float(input("¿Cuanto mide la altura?: "))
	a=2*math.pi*r*h
	v=math.pi*(h**2)*((3*r)-h)*1/3
	print""
	print"El área del casquete esférico es: ",a
	print""
	print"El volumen del casquete esférico es: ",v
	print""
	tecla=raw_input("Presione una tecla para continuar con otra figura geométrica, [0]--> para salir ......")
	if tecla=="0":
		salir()
	else:

		main()



def tronpi():
	print"############################################################"
	print("#    AREA Y VOLUMEN DEL TRONCO DE PIRAMIDE CUADRANGULAR    #")
	print"############################################################"
	print""
	L=float(input("¿Cuanto mide el lado de la base mayor?: "))
	print""
	l=float(input("¿Cuanto mide el lado de la base menor?: "))
	print""
	h=float(input("¿Cuanto mide la altura del tronco de la piramide?: "))
	apM=L/2
	apm=l/2
	ap=apM-apm
	AP=round((math.sqrt((ap**2)+(h**2))), 3)
	aB=(L**2)
	ab=(l**2)
	a=(((L*4)+(l*4))/2)*AP+((aB)+(ab))
	v=h/3*(aB+(math.sqrt(aB*ab)+ab))
	print""
	print"El área del troco de piramide es: ",a
	print""
	print"El volumen del tronco de piramide es: ",v
	print""
	tecla=raw_input("Presione una tecla para continuar con otra figura geométrica, [0]--> para salir ......")
	if tecla=="0":
		salir()
	else:

		main()


def zona():
	print"#######################################################"
	print("######    AREA Y VOLUMEN DE LA ZONA ESFERICA    #######")
	print"#######################################################"
	print""
	R=float(input("¿Cuanto mide el radio mayor?: "))
	print""
	r=float(input("¿Cuanto mide el radio menor?: "))
	print""
	h=float(input("¿Cuanto mide la altura?: "))
	a=2*math.pi*R*h
	v=math.pi/6*h*((h**2)+(3*(R**2))+(3*(r**2)))
	print""
	print"El área de la zona esférica es: ",a
	print""
	print"El volumen de la zona esférica es: ",v
	print""
	tecla=raw_input("Presione una tecla para continuar con otra figura geométrica, [0]--> para salir ......")
	if tecla=="0":
		salir()
	else:

		main()


def elipse():
	print"#######################################################"
	print("#########    AREA DEL ELIPSE    #######################")
	print"#######################################################"
	print""
	b=float(input("¿Cuanto mide el semieje mayor?: "))
	print""
	h=float(input("¿Cuanto mide el semieje menor?: "))
	pi=3.1416
	a=pi*b*h
	print""
	print "El área del elípse es:" ,a
	print""
	tecla=raw_input("Presione una tecla para continuar con otra figura geométrica, [0]--> para salir ......")
	if tecla=="0":
		salir()
	else:

		main()

def toro():
	print"#######################################################"
	print("#########    AREA Y VOLUMEN DEL TORO    ###############")
	print"#######################################################"
	print""
	R=float(input("¿Cuanto mide el radio de la circunferencia directriz?: "))
	print""
	r=float(input("¿Cuanto mide el radio del círculo generatriz?: "))
	a=4*(math.pi**2)*R*r
	v=2*(math.pi**2)*R*r**2
	print""
	print "El área del toro es:" ,a
	print""
	print "El volumen del toro es:" ,v
	print""
	tecla=raw_input("Presione una tecla para continuar con otra figura geométrica, [0]--> para salir ......")
	if tecla=="0":
		salir()
	else:

		main()

def elipsoide():
	print"#######################################################"
	print("#########    AREA Y VOLUMEN DEL ELIPSOIDE    ##########")
	print"#######################################################"
	print""
	a=float(input("¿Cuanto mide el radio mayor?: "))
	print""
	b=float(input("¿Cuanto mide el segundo radio?: "))
	print""
	c=float(input("¿Cuanto mide el tercer radio?: "))
	A=4*math.pi*pow((pow(a, 1.6075)*pow(b, 1.6075)+pow(a, 1.6075)*pow(c, 1.6075)+pow(b, 1.6075)*pow(c, 1.6075))/3, 1/1.6075)
	v=4*math.pi*a*b*c/3
	print""
	print "El área del elipsóide es:" ,A
	print""
	print "El volumen del elipsóide es:" ,v
	print""
	tecla=raw_input("Presione una tecla para continuar con otra figura geométrica, [0]--> para salir ......")
	if tecla=="0":
		salir()
	else:
	
		main()


def main():

	"""Funcion principal del menu"""

	limpiar()


	print "							                      #########################################"
	print "							                      #                                       #"
	print "							                      #          by Enri_python               #"
	print "							                      #                                       #"
	print "							                      #     FIGURAS GEOMETRICAS v1.0          #"
	print "							                      #                                       #"
	print "							                      #########################################"

	print """

	[1] Area del cuadrado                            [2] Area del rectángulo                     [3] Area del rombo                           [4] Area del triángulo
        [5] Area del romboide                            [6] Area del trapecio                       [7] Area del polígono regular                [8] Area del círculo
	[9] Area de la corona circular                   [10] Area del sector circular               [11] Area y volumen del cubo                 [12] Area y volumen del cilindro
        [13] Area y volumen del ortoedro                 [14] Area y volumen del cono                [15] Area y volumen del prisma regular       [16] Area y volumen del tronco de cono
	[17] Area y volumen del tetraedro regular        [18] Area y volumen de la esfera            [19] Area y volumen del octaedro regular     [20] Area y volumen de huso-cuña esférica
        [21] Area y volumen de la pirámide cuadrangular  [22] Area y volumen del casquete esférico   [23] Area y volumen del tronco de pirámide   [24] Area y volumen de zona esférica
	[25] Area del elipse                             [26] Area y volumen del toro                [27] Area y volumen del elipsóide            [0] Salir                        	 

	"""

	opcion = raw_input("Ingresa un número del menu -> ")
	print""

	if opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4" and opcion != "5" and opcion != "6" and opcion != "7" and opcion != "8" and opcion != "9" and opcion != "10" and opcion != "11" and opcion != "12" and opcion != "13" and opcion != "14" and opcion != "15" and opcion != "16" and opcion != "17" and opcion != "18" and opcion != "19" and opcion != "20" and opcion != "21" and opcion != "22" and opcion != "23" and opcion != "24" and opcion != "25" and opcion != "26" and opcion != "27" and opcion != "0" :

		print "Opción incorrecta, presione una tecla para volver al menú ...."

		raw_input()

		main()

	elif opcion == "1":

		cuadrado()


	elif opcion == "2":

		rectangulo()


	elif opcion == "3":

		rombo()


	elif opcion == "4":

		triangulo()

	elif opcion == "5":

		romboide()


	elif opcion == "6":

		trapecio()


	elif opcion == "7":

		poligono()


	elif opcion == "8":

		circulo()

	elif opcion == "9":

		corona()


	elif opcion == "10":

		sector()


	elif opcion == "11":

		cubo()


	elif opcion == "12":

		cilindro()


	elif opcion == "13":

		ortoedro()


	elif opcion == "14":

		cono()


	elif opcion == "15":

		prisma()


	elif opcion == "16":

		tronco()


	elif opcion == "17":

		tetraedro()


	elif opcion == "18":

		esfera()


	elif opcion == "19":

		octaedro()


	elif opcion == "20":

		huso()


	elif opcion == "21":

		piramide()

	elif opcion == "22":

		casquete()


	elif opcion == "23":

		tronpi()


	elif opcion == "24":

		zona()


	elif opcion == "25":

		elipse()


	elif opcion == "26":

		toro()


	elif opcion == "27":

		elipsoide()


	elif  opcion == "0":

		salir()
main()