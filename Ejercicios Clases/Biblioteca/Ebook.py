from Libro import *
class Ebook(Libro):
	def __init__(self,eisbn,url):
		self.eisbn=eisbn
		self.url=url
	def actualizarURL(self):
		newURL= raw_input("Ingrese la nueva URL")
		self.url=newURL