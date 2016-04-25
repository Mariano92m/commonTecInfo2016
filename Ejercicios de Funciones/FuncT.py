def entBill(pesos):
	p=pesos
	moneda=0
	b2=0
	b5=0
	b10=0
	b20=0
	b50=0
	b100=0

	if (type(pesos) == int):
		while p>0:
			if(p>=100):
				b100+=1
				p-=100
			
			elif(p>=50):
				b50+=1
				p-=50
			
			elif(p>=20):
				b20+=1
				p-=20
			
			elif(p>=10):
				b10+=1
				p-=10
			
			elif(p>=5):
				b5+=1
				p-=5
			
			elif(p>=2):
				b2+=1
				p-=2
			
			elif(p==1):
				moneda+=1
				p-=1
		print("Se necesita %s billetes de 100, %s billetes de 50, %s billetes de 20"%(b100,b50,b20))
		print("Se necesita %s billetes de 10, %s billetes de 5, %s billetes de 2"%(b10,b5,b2))
		print("Y %s monedas, para completar %s pesos"%(moneda,pesos))
	else:
		print("Ingreso un valor con decimal")