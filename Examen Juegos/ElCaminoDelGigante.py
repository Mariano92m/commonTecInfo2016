#Situaciion Problematica B
print("\n- Camino del Gigante -")

print("") #Espacio
#Introduccion
print("""- Bienvenido a 'Camino del Gigante' -
	Tu objetivo es que el gigante llegue a su Caverna.
	Supongamos que se llama Bob.
	Tienes 3 intentos lanzando el dado para sumar pasos al gigante.
	\nEmpecemos...""")

print ("\nBob necesita dar 20 pasos para llegar a su caverna, si Bob da mas de 20 pasos cae a un precipicio")

#Variables
import random
pasos = random.randint(1,20)
tiradas = random.randint(1,3)
llegada = 20

#Pasos realizados y faltantes
print (("-El Gigante ha caminado %s pasos-")%(pasos))
restante = (20 - (pasos))
print (("\nAun le quedan %s pasos para llegar a la caverna")%(restante))

intentos = 1

#Mientras los intentos sean menores o iguales a 3
while intentos <= 3:

	dado = input("Lanzar dado? s/n:\n>:")

#Si el dado se lanza...
	if dado == "s":
		tDado = random.randint(1,6)

		print(("\nEl dado ha caido en %s")%(tDado))
		pasos+=tDado

		print (("\nAhora Bob ha hecho %s pasos")%(pasos))
		restante-=tDado

		print (("Y restan %s pasos para llegar")%(restante))


		intentos += 1
		
		#Precipicio
	elif pasos > llegada:
		dado == "x"
		print ("\nHas superado la cantidad de pasos! \nCaiste al precipicio")
		intentos = 4


	
		#En el caso de que se gane...
		if pasos == llegada:
			intentos = 4
			print("\nHas llevado a Bob a la caverna!\n Ganaste! :) ")



#Si el Dado no se Lanza...
	else:
		break


print ("\nBob no lo ha conseguido\n   - GAME OVER - ")

