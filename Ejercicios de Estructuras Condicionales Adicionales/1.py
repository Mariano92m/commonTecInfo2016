print ("\n#################################################")
print ("             Bienvenidos a FLIGHT")
print ("  #################################################")
respuesta=True

while respuesta==True:
	nombre = input("\nIngrese nombre del cliente :")
	numeroDoc = int(input("\nIngrese numero de Documento :"))
	
	print ("\nElija con los numeros los tipos de pasajes")
	print (" 1 - Primera Clase")
	print (" 2 - Segunda Clase")
	print (" 3 - Tercera Clase")
	tipoPasaje=int(input("Elija :"))
	

	print ("Elija con los numeros los tipos de Destinos")
	print (" 1 - Europa")
	print (" 2 - America del Norte")
	print (" 3 - America del Sur")
	print (" 4 - Islas del Caribe")
	destino= int(input("Elija :"))
	
	zona = (input("\n Es fumador S/N? ")).upper()
	
	print (" ")#Espacio
	
	print (nombre)
	
	# DESTINO EUROPA
	if(destino==1):
		
		#PRIMERA CLASE
		if(tipoPasaje==1):
			valorTotal=2500.000			
			if zona=="S":
				valorRecargo=valorTotal*1.10
			elif zona=="N":
				valorDescuento=valorTotal-valorTotal*0.08

		#SEGUNDA CLASE Y TERCERA CLASE
		elif(tipoPasaje==2 or tipoPasaje==3):
			if tipoPasaje==2:
				valorTotal=2100.000
			else:
				valorTotal=1900.000

			if zona=="N":
				valorRecargo=valorTotal*1.08

			elif zona=="S":
				valorDescuento=valorTotal-valorTotal*0.05

	#DESTINO AMERICA DEL NORTE
	elif(destino==2):
		
		#PRIMERA CLASE
		if(tipoPasaje==1):
			valorTotal=2000.000			
			if zona=="S":
				valorRecargo=valorTotal*1.10
			elif zona=="N":
				valorDescuento=valorTotal-valorTotal*0.08

		#SEGUNDA CLASE Y TERCERA CLASE
		elif(tipoPasaje==2 or tipoPasaje==3):
			if tipoPasaje==2:
				valorTotal=1700.000
			else:
				valorTotal=1400.000

			if zona=="N":
				valorRecargo=valorTotal*1.08

			elif zona=="S":
				valorDescuento=valorTotal-valorTotal*0.05

	# DESTINO AMERICA DEL SUR
	elif(destino==3):
		#PRIMERA CLASE
		if(tipoPasaje==1):
			valorTotal=1000.000			
			if zona=="S":
				valorRecargo=valorTotal*1.10
			elif zona=="N":
				valorDescuento=valorTotal-valorTotal*0.08

		#SEGUNDA CLASE Y TERCERA CLASE
		elif(tipoPasaje==2 or tipoPasaje==3):
			if tipoPasaje==2:
				valorTotal=900.000
			else:
				valorTotal=750.000

			if zona=="N":
				valorRecargo=valorTotal*1.08

			elif zona=="S":
				valorDescuento=valorTotal-valorTotal*0.05
	
	#DESTINO ISLAS CARIBE
	elif(destino==4):
		#PRIMERA CLASE
		if(tipoPasaje==1):
			valorTotal=800.000			
			if zona=="S":
				valorRecargo=valorTotal*1.10
			elif zona=="N":
				valorDescuento=valorTotal-valorTotal*0.08

		#SEGUNDA CLASE Y TERCERA CLASE
		elif(tipoPasaje==2 or tipoPasaje==3):
			if tipoPasaje==2:
				valorTotal=700.000
			else:
				valorTotal=500.000

			if zona=="N":
				valorRecargo=valorTotal*1.08

			elif zona=="S":
				valorDescuento=valorTotal-valorTotal*0.05
	

	print("\nEl valor total del boleto es : $ %s" %(valorTotal))
	
	if (tipoPasaje==1 and zona=="S") or (tipoPasaje!=1 and zona== "N"):
		print("Con el recargo quedaria: $ %s"%(valorRecargo))
	else:
		print("Con el descuento quedaria: $ %s"%(valorDescuento))
	
	#SENTENCIA PARA SEGUIR O NO INGRESANDO CLIENTES
	resp= (input("\nIngresa otro cliente S/N: ")).upper()
	if resp=="N":
		respuesta=False