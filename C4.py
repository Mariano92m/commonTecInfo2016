print ("\nSituacion C4")
print ("\n A F I P")
print ("-Sistema de Facturacion Electronica-")

Importe_Total = int(input("\nIngrese el importe total:"))
if Importe_Total >= 5000:
	print ("Monto Superado para consumidor final")

Importes_Aplicados = int(input("Ingrese los importes aplicados:"))
Importe_Neto = Importe_Total - Importes_Aplicados
print ("Importe Neto:",Importe_Neto)

if Importe_Neto == 0:
 	print ("error")
if Importes_Aplicados >= Importe_Neto:
 	print ("error")
if Importe_Neto >= 0:
 	print ("Monto Superado para consumidor final")


 