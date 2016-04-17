# C5...ANSES...Tres tipos de Jubilacion (Por Edad,Joven o Adulta)
Edad=int(input("\nIngrese edad: "))
Antiguedad=int(input("\nIngrese la antiguedad: "))

if(Edad>=60 and Antiguedad<25):
	print("\nSe le otorgora una JUBILACION POR EDAD ")
elif(Edad<60 and Antiguedad>=25):
	print("\nSe le otorgara una JUBILACION JOVEN")
elif(Edad>=60 and Antiguedad>=25):
	print("\nSe le otorgara una JUBILACION ADULTA")
else:
	print("\nNO CUMPLIQUE CON LOS REQUISITOS PARA JUBILARSE")