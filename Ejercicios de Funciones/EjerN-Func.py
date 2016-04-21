def convert(x):
	pulg= x*39.37
	pie= pulg/12
	return pulg, pie

x= float(input("Ingrese el valor a convertir  "))
print ("Los valores en pulgadas y pies son, respectivamente, ", convert(x))