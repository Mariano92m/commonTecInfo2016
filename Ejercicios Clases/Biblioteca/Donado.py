from Libro import *
class Donado(Libro):
	def __init__(self,propietario,anio,isbn, titulo, autor):
		Libro.__init__(self, isbn, titulo, autor)
		self.propietario=propietario
		self.anio=anio
	def calcularAntig(self,anioAct):
		result= anioAct - self.anio
		print (result)