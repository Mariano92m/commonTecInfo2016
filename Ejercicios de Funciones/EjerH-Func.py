def prom(n):
	res=0
	cont=0
	for x in range (1,n+1):
		res = res + x
		cont= cont+1
	result= res/cont
	return result
x = int(input("Ingrese el numero hasta donde promediar  "))
print prom(x)