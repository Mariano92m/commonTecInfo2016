def ArTot  (g,R):
	ArLat=3.14*R*g
	ArTotal= ArLat + (3.14*R*R)
	return ArTotal

x=float(input("Ingrese la generatriz del cono  "))
y=float(input("Ingrese el radio del cono  "))

print ArTot(x,y)
