import random
def ronda(j1):
	print(" ")
	j2= random.randint(1,3)
	if j2==1:
		j2="A"
	elif j2==2:
		j2="C"
	else:
		j2="D"
	if j1=="A":
		if j2=="A":
			print("Empate!")
			contpc== contpc +1
			contusu=contusu+1
		elif j2=="C":
			print ("Perdiste! La computadora te ha contragolpeado")
			contpc=contpc+5
			contusu=contusu-5
		elif j2=="D":
			print("Ganaste! Tu enemigo no ha podido defenderse")
			contusu=contusu+5
			contpc=contpc-5
	elif j1=="C":
		if j2=="A":
			print("Ganaste! Tu enemigo no ha podido atacarte")
			contusu=contusu+5
			contpc=contpc-5
		elif j2=="C":
			print("Empate!")
			contusu=contusu+1
			contpc=contpc+1
		elif j2=="D":
			print ("Perdiste! El enemigo se ha defendido de tu ataque")
			contpc=contpc +5
			contusu=contusu-5
	elif j1=="D":
		if j2=="C":
			print("Ganaste! El enemigo no ha podido atacarte")
			contusu=contusu+5
			contpc=contpc-5
		elif j2=="D":
			print("Empate!")
			contusu=contusu+1
			contpc=contpc+1
		elif j2=="A":
			print ("Perdiste! El enemigo te ha atacado")
	print(" ")


print ("*********************************************************************")
print ("                       Juego de tronos                                        designed by /commonTec: real game engineering/")
print ("*********************************************************************")
print(" ")
print(" ")
print ("Bienvenido a Juego de tronos!")
print ("El juego de rol que no deja de atraparte")
contusu=0
contpc=0
nom=input("Ingrese el nombre de su personaje:  ")
for i in range (3):
	print(" ")
	print("Ingrese el movimiento que desea hacer")
	print("--Atacar con espada (A)")
	print("--Contragolpear con espada(C)")
	print("--Defenderse con escudo (D)")
	j1=input
	ronda(j1)
while contusu==contpc:
	print(" ")
	print("Ingrese el movimiento que desea hacer")
	print("--Atacar con espada (A)")
	print("--Contragolpear con espada(C)")
	print("--Defenderse con escudo (D)")
	j1=input.upper()
	ronda(j1)
	print(" ")
print(" ")
if contusu>contpc:
	print("Has ganado el juego!")
else:
	print("Lo siento: has perdido el juego")
