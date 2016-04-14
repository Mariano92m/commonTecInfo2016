print("Bienvenido usuario, hoy es primero de mayo: ")
diasTrabajados=int(input("Ingrese la cantidad de dias que trabajo el mes de abril: "))
horasDomingo=int(input("Ingrese la cantidad de horas que trabajo los domingos el mes de abril: "))

paga=int(input("Ingrese su salario regular: "));

if(diasTrabajados>21 and (horasDomingo>3 and horasDomingo<5) ):
	paga=((paga*3)/100)+paga
	print("Gracias por su arduo trabajo, aqui tiene $ %s"%(paga))

if(diasTrabajados>=21 and (horasDomingo>6 and horasDomingo<10) ):
	paga=((paga*10)/100)+paga
	print("Gracias por su arduo trabajo, aqui tiene $ %s"%(paga))

if(diasTrabajados<21 and (horasDomingo>3 and horasDomingo<10) ):
	paga=((paga*2)/100)+paga
	print("Gracias por su arduo trabajo, aqui tiene $ %s"%(paga))	