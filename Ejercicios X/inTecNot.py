#Funciones

#
def inNum(n):
	while not n.isnumeric():
		print("\n Error vuelva a ingresar \n")
		n= input("--> ")
	return int(n)

#
def deseaContinuar():
	#Init Variable
	c=True
	#Funcion
	while c == True:
		cont=input("S/N: ").upper()
		if cont=="N" :
			c=False
			return False
		if cont!="N" and cont!="S":
			print("Error, por favor ingrese S o N:")
		else:
			c=False

#
def newPass(): 
	#Init Variable
	passb=False
	#Cambio realizado
	while passb==False:
		pass1= input("Ingrese su password: ")
		pass2= input("Ingrese su password nuevamente por favor: ")
		if pass1==pass2:
			passb=True
		else:
			print ("Ha ingresado mal sus password")

#
def promedio(cantMat): 
	#Init Variable
	notaTot=0
	#Funcion
	for x in range(1,cantMat+1):
		nota=0		
		while nota<=0 or nota>10:
			nota=float(input("Nota de examen de materia %s: " %(x)))
			if(nota<=0 or nota>10):
				print("Error Ingrese de nuevo")
				print("") #Espacio
		notaTot+=nota
	return float(notaTot/cantMat)


#Cuerpo del programa
print ("<<Instituto Amanecer>>")
continuar=True

while continuar==True:
	#Variables
	mayorNota = 0 #
	menorNota = 10 #

	pAlumno = 0 #
	mAlumno = 0 #
	
	#Ingreso de usuario
	usuario= input("Ingrese su nombre de usuario: ")

	#Agrega una pass nueva
	newPass()
	
	print("") #Espacio

	#Se piden la cantidad de aulas
	print("Ingrese la cantidad de aulas existentes: ")
	cantAula=inNum(input("--> "))
	
	#Se piden la cantidad de materias
	print("Ingrese la cantidad de materias: ")
	cantMat=inNum(input("--> "))

	#Se comienza a agregar
	for aula in range(1,cantAula+1): #Rango de aulas cambiado a no estatico

		#Se piden la cantidad de alumnos
		print("Ingrse la cantida de alumnos en el aula %s"%aula)
		cantAlum=inNum(input("--> "))

		print("") #Espacio
		print ("Aula Nro. ", aula)

		for i in range(1,cantAlum+1): #Cantidad de alumnos podemos cambiar

			notatot = 0
			print ("INGRESE DATOS DEL ALUMNO.")

			#Ingresa un nuevo alumno
			nombre= input("Nombre del alumno: ")
			while not nombre.isalpha():
				nombre= input("Error\nNombre del alumno: ")

			#Ingresa materias y saca promedio
			prom=promedio(cantMat)

			print("") #Espacio

			print ("El promedio total de notas del alumno ", nombre , " es:", prom)

			if prom > mayorNota:
				mayorNota = prom
				mAlumno = nombre
			
			if prom < menorNota:
				menorNota = prom
				pAlumno = nombre

			print("") #Espacio

			if i<cantAlum:
				print("Desea continuar cargando alumnos?")
				conti=deseaContinuar()
				if conti==False:
					break

		print ("El mejor alumno del aula %s es %s con un promedio de notas de: %s"%(aula, mAlumno, mayorNota))
		print ("El alumno con el promedio mas bajo del aula %s es %s con: %s" %(aula, pAlumno,menorNota))

		print("Desea continuar cargando las aulas?")
		finite=deseaContinuar()
		if finite==False:
			break
	
	print("Desea continuar la sesion? ")
	continuar=deseaContinuar()