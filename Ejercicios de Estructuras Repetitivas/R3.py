
i=0
j=1
ventaTotal=0
salir=False

while salir!=True:

	usuarios= int(input("Ingrese la cantidad de usuarios: "))

	for i in range(usuarios):
		
		print("") #Espacio
		
		nombreEmpleado=input("Ingrese el nombre del vendedor: ")
		for j in range(1, 13):
			ventaPorMes= int(input(("Ingrese la venta del mes %s: ")%(j)))
			ventaTotal=ventaTotal+ventaPorMes

	print("") #Espacio
	print("") #Espacio

	print("Si desea continuar prisione 1, sino presione 2")
	s=int(input("Desea continuar? "))

	if(s==2):
		salir=True


	print("") #Espacio
	print("") #Espacio
	print("") #Espacio

print("El total de ventas registrado es %s"%(ventaTotal))