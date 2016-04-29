def Argumeto(entero,letras):
	
	cont=0
	for i in letras:
		cont=cont+1
	
	if(entero==cont):
		print "\nEl String que ingreso tiene la misma cantidad (",cont,")" 
		print "de letras que se indica en el numero entero (",entero,")"
	elif(entero!=cont):
		print "\nEl string que ingreso no tiene la misma cantidad(",cont,")"
		print "de letras que se indica en el numero entero(",entero,")"