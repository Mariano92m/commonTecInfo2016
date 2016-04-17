print ("Situacion C9")

print ("-Calculador de Areas-")
print ("\nResponda con -Triangulo- o -Circulo-")
respuesta = input("Usted quiere calcular el area de un Triangulo o un Cirulo?:")

if respuesta == "Triangulo":
	base = int(input("Cual es su base?:"))
	altura = int(input("Cual es su altura?:"))
	Base_de_Triangulo = (base * altura) / 2
	print ("La Base del Triangulo es:",Base_de_Triangulo)

Pi = 3.14
if respuesta == "Circulo":
	radio = float(input("Cual es su radio?:"))
	Base_de_Circulo = (Pi * radio) ** 2
	print ("La Base del Circulo es:",Base_de_Circulo)
