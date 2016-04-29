#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Situación Problemática B): Ahorcado
#El Ahorcado es un juego tradicional en el que cual el jugador debe descubrir la palabra que pensó
#su oponente, ingresando de a una letra por vez. El jugador tiene disponible 4 errores antes de lograr
#la palabra completa. Para el Ahorcado Recargado se incluyen las siguientes indicaciones adicionales:
#- La palabra a adivinar debe tener 5 letras
#- Si el jugador adivina una letra de la palabra, y ésta se repite más veces, el juego no debe indicarlo.
#- El jugador puede solicitar una pista, en cuyo caso, el juego ofrecerá una letra de la palabra pero el
#jugador perderá un intento.
import random

a =["1","2","3","4","5"]
letra1 = str(raw_input("\nIngrese la primera letra : "))
letra2 = str(raw_input("\nIngrese la segunda letra : "))
letra3 = str(raw_input("\nIngrese la tercera letra : "))
letra4 = str(raw_input("\nIngrese la cuarta letra  : "))
letra5 = str(raw_input("\nIngrese la quinta letra  : "))
error=0
ganador=0
ayuda=0
a[0]=letra1
a[1]=letra2
a[2]=letra3
a[3]=letra4
a[4]=letra5
print "\nTURNO DE ADIVINAR LAS LETRAS"
while (error<4 and ganador<=4):	
	jugador = raw_input("\nIngrese una letra :")
	i=0
	acerto=False
	while (i<5):
		if (jugador==a[i]):
			a[i]="gano"
			ganador+=1
			acerto=True
			print "\nAcerto con la letra",jugador
			i=6
		i+=1
	if(acerto==False):
		print "\nNo acerto con la letra ",jugador
		error+=1
		ayuda = random.randint(1,6)
		if(ayuda>=3):
			if(a[0]!="gano"):
				print "\nTE DOY UNA AYUDA, UNA DE LAS LETRA ES ",a[0]
				continue
			elif(a[1]!="gano"):
				print "\nTE DOY UNA AYUDA, UNA DE LAS LETRA ES ",a[1]
				continue
			elif(a[2]!="gano"):
				print "\nTE DOY UNA AYUDA, UNA DE LAS LETRA ES ",a[2]
				continue
			elif(a[3]!="gano"):
				print "\nTE DOY UNA AYUDA, UNA DE LAS LETRA ES ",a[3]
				continue
			elif(a[4]!="gano"):
				print "\nTE DOY UNA AYUDA, UNA DE LAS LETRA ES ",a[4]
				continue
if(error==4):	
	print "\nUSTED QUEDO AHORCADO Y PERDIO  :("
	print "\n Esta fue la palabra que eligio su contrario ",letra1,letra2,letra3,letra4,letra5
elif ganador==5:
	print "\nGANO EL JUEGO"



