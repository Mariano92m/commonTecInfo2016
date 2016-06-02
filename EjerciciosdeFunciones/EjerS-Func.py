def Edades(e1, e2):
	mayor=0
	menor=0
	if(e1!=e2):
		if(e1>e2):
			mayor=e1
			menor=e2
			falta=mayor-menor
		elif(e2>e1):
			mayor=e2
			menor=e1
			falta=mayor-menor
		print("%s es mayor que %s, al menor le faltan %s anios para ser como el mayor"%(mayor,menor,falta))
	else:
		print("Tienen la misma edad")