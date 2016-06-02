from Libro import *
class Ebook(Libro):
	def __init__(self,eisbn,url,isbn, titulo, autor):
		Libro.__init__(self, isbn, titulo, autor)
		self.eisbn=eisbn
		self.url=url
	def actualizarURL(self):
		newURL= raw_input("Ingrese la nueva URL")
		self.url=newURL