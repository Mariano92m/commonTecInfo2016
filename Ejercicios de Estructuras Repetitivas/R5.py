Tipo= (raw_input("Ingrese el tipo de animal a estudiar: E/C/J ")).upper()
men1=0
men3=0
mas3=0

if (Tipo=="E"): 
	cant=20
elif (Tipo=="C"):
	cant=40
elif (Tipo=="J"):
	cant=15
else:
	print ("Error: debe elegir entre E/C/J")

for x in range (1,cant):
	Edad= int(input("Ingrese la edad del animal en numeros"))
	if Edad <= 1:
		men1= men1 +1
	elif Edad<3:
		men3= men3 +1
	else:
		mas3= mas3 + 1

print ("Del animal seleccionado, se obtuvieron los siguientes porcentajes: ")
print ("0-1 anio", ((men1*100)/cant))
print ("1-3 anios", ((men3*100)/cant))
print ("mas de 3 anios", ((mas3*100)/cant))