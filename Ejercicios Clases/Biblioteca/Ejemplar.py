class Ejemplar:
	"""Clase para Ejemplar"""
	def __init__(self,codigo,editorial,fechaCompra):
	
		self.codigo = codigo
		self.editorial = editorial
		self.anioCompra = fechaCompra

	def actualizarEditorial(self):
		self.editorial = input("Editorial Actual:")

	def antiguedad(self):
		anioActual = int(input("Fecha actual:"))
		self.anioCompra-=anioActual 









		