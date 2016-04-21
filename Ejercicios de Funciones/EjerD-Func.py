def pot(j,h):
	eq=1
	for x in range (h):
	    eq=eq*j
	print "El resultado de la potencia es: ",eq

x=int(input("Ingrese primero el numero base  "))
y=int(input("Ingrese el numero potencia  "))
pot(x,y)
