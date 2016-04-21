def impval (n):
	tot=0
	for x in range (n+1):
		tot +=x
	return tot
x=int(input("Ingrese el numero para probar la funcion   "))
print impval(x)