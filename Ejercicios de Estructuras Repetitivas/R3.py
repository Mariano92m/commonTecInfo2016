
i=0
j=1
ventaTotal=0
salir=False

usuarios= int(input("Ingrese la cantidad de usuarios: "))



while (i<usuarios) and (salir!=True):
	
	print("") #Espacio
	
	nombreEmpleado=input("Ingrese el nombre del vendedor: ")
	while j<=12:
		ventaPorMes= int(input(("Ingrese la venta del mes %s: ")%(j)))
		ventaTotal=ventaTotal+ventaPorMes
		j=j+1
	i=i+1

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