numerito=int(input("Ingresa un numero: "))
cont=1

while cont<=9:
	if(numerito+cont)%10==0:
		print("%s es el digito correspondiente"%(cont))
	cont=cont+1