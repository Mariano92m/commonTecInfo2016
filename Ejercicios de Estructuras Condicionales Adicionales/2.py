A=int(input("\nIngrese el primero numero : "))
B=int(input("\nIngrese el segundo numero : "))
igual=0 
unoAA=False
dosAA=False
tresAA=False
cuatroAA=False



unoA=A/1000
dosA=(A-(unoA*1000))/100
tresA=(A/10)%10
cuatroA=A%10

print " "
print unoA,dosA,tresA,cuatroA


unoB=B/1000
dosB=(B-(unoB*1000))/100
tresB=(B/10)%10
cuatroB=B%10

print " "
print unoB,dosB,tresB,cuatroB
print " "

if (unoA==unoB):
	igual=igual+1
	unoAA=True

if(dosA==dosB):
	igual=igual+1
	dosAA=True

if(tresA==tresB):
	igual=igual+1
	tresAA=True

if(cuatroA==cuatroB):
	igual=igual+1
	cuatroAA=True

print " Hay ",igual,"digitos coincidentes "
print "\n Los numeros que se repiten son :" 

if(unoAA==True):
	print unoA

if(dosAA==True):
	print dosA

if(tresAA==True):
	print tresA

if(cuatroAA==True):
	print cuatroA
if (unoAA==False and dosAA==False and tresAA==False and cuatroAA==False):
	print " ninguno "