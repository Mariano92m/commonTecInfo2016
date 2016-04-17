sIni=0;
transaccion=True
while transaccion==True:
	print("----------------------0---------------------")
	print("Bienvenido señor!")

	print("Si desea realizar un deposito presione 1")
	print("Si desea realizar un retiro presione 2")
	pedido=int(input("Presione uno de los numeros y luego enter: "))

	if(pedido==1):
		aDep=int(input("Cuanto desea depositar? "))
		sIni=sIni+aDep
	elif(pedido==2):
		aRet=int(input("Cuanto desea retirar? "))
		if(aRet>sIni):
			print("No puede retirar ese monto por que no tiene los fondos necesarios")
		else:
			sIni=sIni-aRet
	else:
		print("El numero ingresado es incorrecto");

	print("Si desea continuar con la transaccion pulse 1, sino puse 2, y luego enter: ")
	
	aux=int(input("aux= "))

	if(aux==1):
		transaccion=True
	elif(aux==2):
		transaccion=False


print(sIni)