import random

NombreUsuario = str(raw_input("\nIngrese el nombre de su equipo : "))
partida=0
resultado=0
ResulUsuario=0
ResultadoPC=0
cont=0
print "\nEMPIEZA JUGANDO EL USUARIO"
while partida<5:
	print " "
	print "		1	2	3"
	print "				 "
	print "		4	5	6"
	print " "
	PenalUsuario = int(raw_input("\nIngrese el numero de la direccion del penal : "))
	PenalPC = random.randint(1,6)
	if(PenalUsuario>=1 and PenalUsuario<=6):
		cont+=1
		if(PenalUsuario!=PenalPC):
			ResulUsuario+=1
			print "\nGol de ",NombreUsuario," !!"
			print "\nResultado Parcial : ",NombreUsuario," ",ResulUsuario," - Algoritmos ",ResultadoPC," (",cont," penales pateados)"
		elif (PenalUsuario==PenalPC):
			print "\nEl arquero atajo su penalti con el ",PenalPC
			print "\nResultado Parcial : ",NombreUsuario," ",ResulUsuario," - Algoritmos ",ResultadoPC
		partida+=1
	else:
		print "\n La direccion de su penalti debe estar dentro de los numero 1 , 2 , 3 , 4 , 5 o 6"
partida=0
cont=0
print "\nES EL TURNO DE LA PC, LA PC PATEA Y EL USUARIO ATAJA"
while partida<5:
	print " "
	print "		1	2	3"
	print "				 "
	print "		4	5	6"
	print " "
	PenalUsuario = int(raw_input("\nIngrese el numero de la direccion en la que quiere atajar : "))
	PenalPC = random.randint(1,6)
	if(PenalUsuario>=1 and PenalUsuario<=6):
		cont+=1
		if(PenalUsuario!=PenalPC):
			ResultadoPC+=1
			print "\nGol de Algoritmos (PC) !!"
			print "\nResultado Parcial : ",NombreUsuario," ",ResulUsuario," - Algoritmos ",ResultadoPC," (",cont," penales pateados)"
		elif (PenalUsuario==PenalPC):
			print "\nUsted atajo el penalti con el ",PenalPC
			print "\nResultado Parcial : ",NombreUsuario," ",ResulUsuario," - Algoritmos ",ResultadoPC
		partida+=1



if(ResulUsuario==ResultadoPC):
	print "\nEl juego resulto en empate, se procedera" 
	print "a patear de a un penal hasta que un equipo gane"
	cont=0
	while ResulUsuario==ResultadoPC:
		print "\n TURNO DEL USUARIO DE PATEAR EL PENALTI"
		print " "
		print "		1	2	3"
		print "				 "
		print "		4	5	6"
		print " "
		PenalUsuario = int(raw_input("\nIngrese el numero de la direccion del penal : "))
		PenalPC = random.randint(1,6)
		if(PenalUsuario>=1 and PenalUsuario<=6):
			cont+=1
			if(PenalUsuario!=PenalPC):
				ResulUsuario+=1
				print "\nGol de ",NombreUsuario," !!con el ",PenalUsuario
				print "\nResultado Parcial : ",NombreUsuario," ",ResulUsuario," - Algoritmos ",ResultadoPC," (",cont," penales pateados)"
			elif(PenalUsuario==PenalPC):
				print "\n EL EQUIPO ALGORITMOS atajo el penalti con el ",PenalPC
			PenalPC = random.randint(1,6)
			print "\nTURNO DEL USUARIO DE ATAJAR"
			PenalUsuario = int(raw_input("\nIngrese el numero de la direccion que desea atajar : "))
			if(PenalUsuario>=1 and PenalUsuario<=6):
				cont+=1
				if(PenalUsuario!=PenalPC):
					ResultadoPC+=1
					print "\nGol de Algoritmos (PC) !! con el ",PenalPC
					print "\nResultado Parcial : ",NombreUsuario," ",ResulUsuario," - Algoritmos ",ResultadoPC," (",cont," penales pateados)"
				elif(PenalUsuario==PenalPC):
					print "\n EL EQUIPO ",NombreUsuario," atajo el penalti con el ",PenalUsuario
		else:
			print "\n La direccion de su penalti debe estar dentro de los numero 1 , 2 , 3 , 4 , 5 o 6"
if(ResulUsuario>ResultadoPC):
	print "\n GANO EL EQUIPO ",NombreUsuario
	print "RESULTADO FINAL : ",NombreUsuario," ",ResulUsuario," - Algoritmos ",ResultadoPC
elif(ResulUsuario<ResultadoPC):
	print "\n GANO EL EQUIPO ALGORITMOS"
	print "RESULTADO FINAL : ",NombreUsuario," ",ResulUsuario," - Algoritmos ",ResultadoPC
