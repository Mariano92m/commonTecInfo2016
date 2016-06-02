class Sector:
	def __init__(self,codigo,capacidad):
		self.codigo codigo
		self.capacidad capacidad

	def actualizarCapacidad(self):
		self.capacidad=input("Ingrese la nueva capacidad")