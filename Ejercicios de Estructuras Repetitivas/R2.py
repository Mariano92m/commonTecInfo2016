contEmpleados=int(input("Ingrese la cantidad de empleados que hay en la empresa: "))
i=0
sumSueld=0
cobranMas=0
cobranMenos=0

for i in range(contEmpleados):
	sueldo=int(input("Ingrese su sueldo, recuerde que cobra entre 100 y 500: "))

	if(sueldo<300):
		cobranMenos=cobranMenos+1
	elif(sueldo>=300):
		cobranMas=cobranMas+1

	sumSueld=sumSueld+sueldo

print("%s empleados cobran menos y %s cobran mas"%(cobranMenos, cobranMas))
print("La empresa gastara $ %s para saldar los sueldos del personal"%(sumSueld))
