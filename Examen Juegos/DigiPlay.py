import random
print ("*********************************************************************")
print ("                           DigiPlay                                         designed by /commonTec: real game engineering/")
print ("*********************************************************************")
print(" ")
print(" ")
print ("Bienvenido a DigiPlay!")
print ("El juego ideal para el recreo")
numeroDigi = random.randint(1000,1999)

#Funcion que genera la suma de los cuatro digitos
def sumaDeDigitos():
	suma = 0

	for cifra in str(numeroDigi):
		suma+=int(cifra)

	return suma

#Presentacion
print ("")#Espacio
print (("""El juego consiste en adivinar un numero de 4 cifras,
pero solo conoceras la suma de las mismas...

La suma del numero es %s
Tienes 3 intentos para adivinar el numero que lo forma""")%(sumaDeDigitos()))

intentos = 1
#El jugador tiene 3 intentos
while intentos <= 3:
	respuesta = int(input("\nCual piensas que es el numero?:  "))

	if respuesta == numeroDigi:

		print("Felicidades: has acertado el numero!")
		print("\nGanaste!")

	else:
		print("\nEse no es numero, vuelve a intentarlo")

	intentos += 1

	#Se queda sin intentos
	while intentos > 3:

		print ("\nLo sentimos: te has quedado sin intentos-- Juego Terminado! ")

		continuar = input("Quieres volver a empezar?(s/n): \n>:")

		if continuar == ("s"):
			intentos = 1

		else:
			print ("\nG A M E - O V E R")

			break





print ("No lo has conseguido...el numero era...")

print (numeroDigi)
