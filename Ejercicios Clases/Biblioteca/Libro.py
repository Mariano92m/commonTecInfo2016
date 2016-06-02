class Libro: 
	def __init__(self, isbn, titulo, autor):
		self.isbn= isbn
		self.titulo=titulo
		self.autor= autor
	def modificarTitulo(self):
		newTit= raw_input("Ingrese el nuevo titulo")
		self.titulo=newTit