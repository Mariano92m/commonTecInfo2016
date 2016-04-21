def fact(x):
	res=1
	for i in range (x,0,-1):
		res= res *i
	print "El resultado del factorial es   ",res

x=int(input("Ingrese el numero para aplicar el factorial   "))
fact(x)