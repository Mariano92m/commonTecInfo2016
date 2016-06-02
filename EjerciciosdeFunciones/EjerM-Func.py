def rango(L1,L2,x):
	if(L1<=x and x<=L2):
		print("Se encuentra dentro del rango")
	elif(L1>x):
		print("Se encuentra a la izquierda")
	else:
		print("Se encuentra a la derecha")