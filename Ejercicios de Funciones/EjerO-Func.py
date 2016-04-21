def sumeq(x,y,z):
	if x+y==z:
		print"El ultimo numero es igual a la suma de los dos primeros"
		print(" ")
	elif (y+z==x):
		print "El primer numero es igual a la suma de los ultimos dos"
		print(" ")
	elif (x+z==y):
		print "El segundo numero es igual a la suma del primero y el tercero"
	else:
		print "Ningun numero es igual a la suma de los otros dos"
