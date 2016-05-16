from Libro import *
class Donado(Libro):
	def __init__(self,propietario,anio):
		self.propietario=propietario
		self.anio=anio
	def calcularAntig(self,anioAct):
		result= anioAct - self.anio
		print (result)