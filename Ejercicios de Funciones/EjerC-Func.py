def impvals(m):
	if (m%2==0):
		for x in range (1,m+1):
			print x
	else:
		for x in range (m,0,-1):
			print x

x=int(input("Ingrese el numero para probar la funcion  "))
impvals(x)