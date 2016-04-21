#Contadores
cantP=0
contH=0
contM=0


contMayorDeEdadM=0
contMenorDeEdadM=0

contMayorDeEdadH=0
contMenorDeEdadH=0

contHacenDeporte=0

#Booleanos
salir=False


print("")#Espacio
print("")#Espacio

print("-------Bienvenido Usuario-------") #Titulo 

while salir!=True:
	
	mientras=True
	mientrasS=True
	mientrasE=True

	print("")#Espacio
	print("")#Espacio

	nombreApe=input("Ingrese nombre y apellido:")
	
	
	while mientrasS==True:
		sexo=(input("Ingrese Sexo H/M: ")).upper()
		if(sexo=="H" or sexo == "M"):
			mientrasS=False
		else:
			print("Error! Ingreso equivocado")
			print("")#Espacio

	
	while mientrasE==True:
		edad=int(input("Ingrese la edad: "))
		if(edad>0):
			mientrasE=False
		else:
			print("Error! Ingreso equivocado")
			print("")#Espacio
	
	
	while mientras==True: #Verifica si se ingreso S o N, sino vuelve a recorrer
		print("")#Espacio
		haceDep=(input("Hace deporte S/N? ")).upper()

		if(haceDep=="S"):
			if(sexo=="H"):
				contH=contH+1
				if(edad>1 and edad<18):
					contMenorDeEdadH=contMenorDeEdadH+1
				elif(edad>=18):
					contMayorDeEdadH=contMayorDeEdadH+1

			if(sexo=="M"):
				contM=contM+1
				if(edad>1 and edad<18):
					contMenorDeEdadM=contMenorDeEdadM+1

				elif(edad>=18):
					contMayorDeEdadM=contMayorDeEdadM+1

		elif(haceDep=="N"):
			mientras=False
		else:
			print("Error! Ingreso equivocado!")
		mientras=False;
		
	cantP=cantP+1

	print("")#Espacio

	print("Desea ingresar otra persona? ")
	terminar=(input("S/N: ")).upper()
	if terminar=="N":
		salir=True
	
print("")#Espacio
print("")#Espacio
print("")#Espacio

print("El porcentaje de persona que no hacen deporte es de  %",(((cantP-(contH+contM))*100)/cantP))
print("")#Espacio
print("El porcentaje de personas que hacen deporte es de %",(((contH+contM)*100)/cantP))
print("")#Espacio
print("El porcentaje de hombres que hacen deporte es de %",((contH*100)/(contH+contM))
print("El porcentaje de mujeres que hacen deporte es de %",((contM*100)/(contH+contM))

if(contH*100)/cantP>(contM*100)/cantP:
	print("Hay un mayor porcentaje de hombres que realizan deportes")
else:
	print("Hay un mayor porcentaje de mujeres que realizan deportes")

print("")#Espacio
print("")#Espacio
print("")#Espacio

print("El porcentaje de hombres mayores de edad que hacen deporte es de %",((contMayorDeEdadH*100)/contH))
print("El porcentaje de hombres menores de edad que hacen deporte es de %",((contMenorDeEdadH*100)/contH))

print("")#Espacio

if(contMayorDeEdadH*100)/contH>(contMenorDeEdadH*100)/contH:
	print("Hay un mayor porcentaje de hombres mayores de edad que realizan deporte")
else:
	print("Hay un mayor porcentaje de hombres menores de edad que realizan deporte")


print("")#Espacio
print("")#Espacio


print("El porcentaje de mujeres mayores de edad que hacen deporte es de %",((contMayorDeEdadM*100)/contM))
print("El porcentaje de mujeres menores de edad que hacen deporte es de %",((contMenorDeEdadM*100)/contM))

print("")#Espacio

if(contMayorDeEdadM*100)/contM>(contMenorDeEdadM*100)/contM:
	print("Hay un mayor porcentaje de mujeres mayores de edad que realizan deporte")
else:
	print("Hay un mayor porcentaje de mujeres menores de edad que realizan deporte")
