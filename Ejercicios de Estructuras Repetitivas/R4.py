cantCorreos=15
cont=0

while cont<cantCorreos:
	pasw=False

	idU= input("Ingrese la id de usuario: ")
	dominioU= input("Ingrese el dominio: ")

	print("")#Espacio

	while pasw!=True:
		pas1=input("Ingrese su pass: ")
		pas2=input("Confirme su pass: ")

		print("")#Espacio

		if(pas1==pas2):
			pasw=True
		else:
			print("Contraseña incorrecta")

			print("")#Espacio

	print(idU + dominioU)

	print("")#Espacio
	print("")#Espacio

	cont= cont +1