# Descripcion: Clase ListaReproduccion, lista circular que almacena las
# canciones que seran reproducidas
# Autores:
# 	Rubmary Rojas 13-11264
# 	Juan Ortiz    13-11021
# email:
# 	rubmaryrojas@gmail.com
# 	ortiz.juan14@gmail.com

from mergesort import *
from Cancion   import *
from NodoLista import *



# Descripcion: Clase que implementa el nodo de una lista
# Atributos:
#	cabeza: atributo que referencia a la primera cancion de la lista
#	size: atributo que indica el tamano de la lista
class ListaReproduccion:
	
	def __init__(self):
		self.cabeza = None
		self.size   = 0
	
	# Descripcion: Metodo que indica la longitud de la lista
	# Parametros:
	#	self: lista actual
	# Retorna: Un entero que indica la longitud de la lista
	def __len__(self):
		return self.size
	
	# Descripcion: Metodo que verifica si una cancion se encuentra en la
	# lista.
	# Parametros:
	#	self: lista actual
	#	cancion: elemento de tipo Cancion, el cual sera buscado en la lista
	# Retorna: Valor booleano que indica si cancion esta o no en la lista
	def __contains__(self, cancion):
		actual = self.cabeza
		if actual is None:
			return False
		while True:
			if actual.cancion.es_igual(cancion):
				return True
			actual = actual.next
			if actual is self.cabeza:
				return False
	
	# Descripcion: Metodo que agrega un elemento a la lista
	# Parametros:
	#	self: lista actual
	#	cancion: elemento de tipo Cancion que sera agregado en la lista	
	def agregar(self, cancion): 
		actual = self.cabeza
		while actual is not None and True:
			if actual.cancion.es_igual(cancion):
				return
			actual = actual.next
			if actual is self.cabeza:
				break
		 
		nodo = NodoLista(cancion)
		self.size += 1
		if self.size==1:
			nodo.next = nodo
			nodo.prev = nodo
			self.cabeza = nodo
		else:
			nodo.next = self.cabeza
			nodo.prev = self.cabeza.prev
			self.cabeza.prev.next = nodo
			self.cabeza.prev = nodo
			self.cabeza = nodo
	
	# Descripcion: Metodo que elimina una cancion si se encuentra en la 
	# lista. Si no se encuentra la cancion, la lista no es modificada
	# Parametros:
	#	self: lista actual
	#	cancion: elemento de tipo Cancion, el cual sera eliminado
	def eliminar(self, cancion):
		actual = self.cabeza
		if actual is None:
			return
		while True:
			if actual.cancion.es_igual(cancion):
				break
			actual = actual.next
			if actual is self.cabeza:
				return
			
		self.size = self.size-1
		if self.size == 0:
			self.cabeza = None
		else:
			actual.prev.next = actual.next
			actual.next.prev = actual.prev
			if actual is self.cabeza:
				self.cabeza = actual.next
	
	# Descripcion: Metodo que ordena una lista segun el orden lexicogra-
	# fico de los titulos de sus canciones. Si dos canciones tienen el
	# mismo titulo, se considera menor aquella cuyo artista tenga un nom-
	# bre menor lexicograficamente.
	# Parametros:
	#	self: lista actual
	def ordenar_titulo(self):
		mergesort_titulo(self)
	
	# Descripcion: Metodo que ordena una lista segun el orden lexicogra-
	# fico de los artista de sus canciones. Si dos canciones tienen el
	# mismo artista, se considera menor aquella cuyo titulo tenga un nom-
	# bre menor lexicograficamente.
	# Parametros:
	#	self: lista actual
	def ordenar_artista(self):
		mergesort_artista(self)

	# Descripcion: Metodo que muestra el contenido de la lista, desde la
	# primera cancion. Por cada cancion muestra el titulo, genero y ar-
	# tista en ese orden.
	# Parametros:
	#	self: lista actual	
	def mostrar(self):
		actual = self.cabeza
		if len(self)==0:
			return
		while True:
			print("Titulo: "  + actual.cancion.get_titulo())
			print("Genero: "  + actual.cancion.get_genero())
			print("Artista: " + actual.cancion.get_artista())
			print
			actual = actual.next
			if actual is self.cabeza:
				return

# Descripcion: Metodo que crea una lista con las mismas canciones de otra
# lista dada
# Parametros:
#	lista: objeto de tipo ListaReproduccion el cual se quiere duplicar
# Retorna: Una instancia de la clase ListaReproduccion con las mismas can-
# ciones y en el mismo orden que el objeto lista
def nueva_lista(lista):
	L = ListaReproduccion()
	nodo = lista.cabeza
	while nodo is not None:
		nodo = nodo.prev
		C = nodo.cancion
		cancion = Cancion(C.titulo, C.genero, C.artista, C.archivo)
		L.agregar(cancion)
		if nodo is lista.cabeza:
			break
	return L
