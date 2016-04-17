n1=int(input("Ingrese un numero: "));
n2=int(input("Ingrese un numero: "));
n3=int(input("Ingrese un numero: "));

if((n1<n2)and(n2<n3)):
	print("%s < %s < %s"%(n1,n2,n3));
if((n2<n3)and(n3<n1)):
	print("%s < %s < %s"%(n2,n3,n1));
if((n3<n1)and(n1<n2)):
	print("%s < %s < %s"%(n3,n1,n2));

if(n1<n3 and n3<n2):
	print("%s < %s < %s"%(n1,n3,n2));
if(n2<n1 and n1<n3):
	print("%s < %s < %s"%(n2,n1,n3));
if(n3<n2 and n2<n1):
	print("%s < %s < %s"%(n3,n2,n1));