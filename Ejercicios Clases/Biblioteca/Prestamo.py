class Prestamo(object):
	"""Clase:Prestamo"""
	def __init__(self,fechaDesde,fechaHasta,Estado):
		
		self.fechaDesde = fechaDesde
		self.fechaHasta = fechaHasta
		self.Estado = Estado

	def calcularVencimiento(self):
		vencimiento = fechaDesde - fechaHasta
		print(vencimiento)