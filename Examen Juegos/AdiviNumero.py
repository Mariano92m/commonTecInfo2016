import random
print ("*********************************************************************")
print ("                       AdiviNumero                                            designed by /commonTec: real game engineering/")
print ("*********************************************************************")
print(" ")
print(" ")
print ("Bienvenido a AdiviNumero!")
print ("El juego de adivinanzas ideal para la familia")
n = random.randint(1,100)
print (" ")
print (" ")
intentos = 1
print ("Adivina un Numero del 1 al 100\n(Tienes 5 intentos)")
print (" ")
#Con 5 intentos
while intentos <= 5:
	numeroIngresado = int(input("\nCual es el numero?:"))
print (" ")
	if numeroIngresado > n:
		print (("\nEl numero es menor al que ingresaste\nYa has hecho %s intentos")%(intentos))
	
	elif numeroIngresado < n:
		print (("\nEl numero es mayor al que ingresaste\nYa has hecho %s intentos")%(intentos))
	intentos += 1

	#Se queda sin intentos
	while intentos > 5:
		print ("\nLo sentimos: re has quedado sin intentos-- Juego Terminado!")
		print(" ")
		continuar = input("Quieres volver a empezar?(s/n): \n>:")

		if continuar == ("s"):
			intentos = 1
		else:
			print ("\nG A M E - O V E R")

			break

	#Si ganan...
	if numeroIngresado == n:
		print ("\nBien hecho: ese es el numero!\nHas ganado el juego!")
		
		break