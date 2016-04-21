# p) Escribir una funcion que dado el ingreso de un numero n, devuelva la suma de sus
# digitos. Por ejemplo si se ingresara el numero 34, se retorna 7.

x = int(raw_input("\nIngrese un numero :"))
def numero(n,suma=0):
	uno=n/10
	dos=n%10
	suma=uno+dos
	print " "
	print suma 
numero(x) 