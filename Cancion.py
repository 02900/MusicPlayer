# Descripcion: Implementacion de la clase Cancion
# canciones que seran reproducidas
# Autores:
# 	Rubmary Rojas 13-11264
# 	Juan Ortiz    13-11021
# email:
# 	rubmaryrojas@gmail.com
# 	ortiz.juan14@gmail.com


# Descripcion: Clase que implementa la cancion a reproducir
# Atributos:
#	titulo: titulo de la cancion 
#	genero: genero de la cancion
#	artista: artista de la cancion
#	archivo: archivo de musica de formato mp3, AVI o OGG. Es la cancion
#			 que se reproducira.
class Cancion:
	def __init__(self, titulo, genero, artista, archivo):
		self.titulo  = titulo
		self.genero  = genero
		self.artista = artista
		self.archivo = archivo
	
	# Descripcion: Metodo que indica si una cancion es igual a otra. Dos
	# canciones ses consideran iguales si poseen el mismo titulo y el 
	# mismo artista
	# Parametros:
	#	self: cancion actual
	#	cancion: cancion que sera comparada con self
	# Retorna: Un valor booleano que indica si self y cancion son iguales.
	def es_igual(self, cancion):
		return self.titulo==cancion.titulo and self.artista==cancion.artista
	
	# Descripcion: Metodo que indica si una cancion cancion es menor a
	# otra, segun los artistas.
	# Parametros:
	#	self: cancion actual
	#	cancion: cancion que sera comparada con self
	# Retorna: Un valor booleano que devuelve true si el nombre del ar-
	# tista de self es menor estricto lexicograficamente que el nombre
	# del artista de cancion. Si los artistas son iguales, devuelve true
	# si self.titulo<=cancion.titulo
	def esmenor_artista(self, cancion):
		return (self.artista<cancion.artista or
		       (self.artista==cancion.artista and self.titulo<=cancion.titulo))
	
	# Descripcion: Metodo que indica si una cancion cancion es menor a
	# otra, segun los titulos.
	# Parametros:
	#	self: cancion actual
	#	cancion: cancion que sera comparada con self
	# Retorna: Un valor booleano que devuelve true si el titulo de self
	# es menor estricto lexicograficamente que el titulo de cancion. Si
	# los titulos son iguales, devuelve true si self.artista<=cancion.artista     
	def esmenor_titulo(self, cancion):
		return (self.titulo<cancion.titulo or 
		       (self.titulo==cancion.titulo and self.artista<=cancion.artista))
	
	
	# Descripcion: Metodo que devuelve el titulo de una cancion.
	# Parametros:
	#	self: cancion actual
	# Retorna: El titulo de self	      
	def get_titulo(self):
		return self.titulo
	
	# Descripcion: Metodo que devuelve el genero de una cancion.
	# Parametros:
	#	self: cancion actual
	# Retorna: El genero de self	
	def get_genero(self):
		return self.genero
	
	# Descripcion: Metodo que devuelve el artista de una cancion.
	# Parametros:
	#	self: cancion actual
	# Retorna: El artista de self
	def get_artista(self):
		return self.artista
	
	# Descripcion: Metodo que devuelve el archivo de musica de una cancion.
	# Parametros:
	#	self: cancion actual
	# Retorna: El archivo de musica correspondiente a self
	def get_archivo(self):
		return self.archivo
