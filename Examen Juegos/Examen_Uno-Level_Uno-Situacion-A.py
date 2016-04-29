# Curso Avanzado de Desarrollo de Aplicaciones Informaticas
#Examen 1 - Level 1

#Adrian Lopez

#Situaciion Problematica A
print ("\n- AdiviNumero -")

import random
n = random.randint(1,100)

intentos = 1
print ("Adivina un Numero del 1 al 100\n(Tienes 5 intentos)")

#Con 5 intentos
while intentos <= 5:
	numeroIngresado = int(input("\nCual es el numero?:"))

	if numeroIngresado > n:
		print (("\nEl numero es menor al que ingresaste\n*Ya has hecho %s intentos*")%(intentos))
	
	elif numeroIngresado < n:
		print (("\nEl numero es mayor al que ingresaste\n*Ya has hecho %s intentos*")%(intentos))
	intentos += 1

	#Se queda sin intentos
	while intentos > 5:
		print ("\nJuego Terminado! -Te has quedado sin intentos-")
		continuar = input("Quieres volver a empezar?(s/n): \n>:")

		if continuar == ("s"):
			intentos = 1
		else:
			print ("\nG A M E - O V E R")

			break

	#Si ganan...
	if numeroIngresado == n:
		print ("\nEse es el numero!\nFELICIDADES\nHas ganado!!!")
		
		break


#Final de la Situacion Problematica A

#
#
#
#
#


