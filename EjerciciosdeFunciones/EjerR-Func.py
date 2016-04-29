def prime (x):
	prim=True
	res=1
	for y in range (2, x-1):
		if x%y==0:
			prim=False
	if (prim==True):
		for y in range (1, x+1):
			res= res * y
		print res
	else:
		for y in range (1, x):
			if y < 1000:
				if x%y==0:
					print y
	Seg=(raw_input("Desea ingresar otro numero? S/N   ")).upper()
	if Seg == "S":
		x=int(input("Ingrese el numero que desea evaluar  "))
		prime (x)