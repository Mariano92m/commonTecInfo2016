año=int(input("Ingrese un año: "))
if(año % 4 == 0 and año % 100 != 0 or año % 400 == 0):  
 print("El año "+ año +" Si es bisiesto ")  
else:  
 print("El año "+ año +" No es bisiesto ") 