# Descripcion: Implementaction de la clase List, lista simplemente 
# enlazada de pares donde cada nodo tiene guardado un string que es la 
# clave clave y un objeto ListaReproduccion de canciones
# Autores:
# 	Rubmary Rojas 13-11264
# 	Juan Ortiz    13-11021
# email:
# 	rubmaryrojas@gmail.com
# 	ortiz.juan14@gmail.com

from ListaReproduccion import *

# Descripcion: Clase que implementa el nodo de la clase List
# Atributos:
#	s: clave del nodo, de tipo string
#	canciones: ListaReproduccion que tiene las canciones asociadas la 
# 	clave s
#	next: referencia al proximo nodo
class hashEntry:
	def __init__(self, s, cancion):
		self.s = s
		self.canciones = ListaReproduccion()
		self.canciones.agregar(cancion)
		self.next  = None

class List:
	def __init__(self):
		self.head = None
		self.size = 0
	
	
	# Descripcion: Metodo que indica la longitud de la lista
	# Parametros:
	#	self: lista actual
	# Retorna: Un entero que indica la longitud de la lista
	def __len__(self):
		return self.size
	
	
	# Descripcion: Metodo que determina si una clave se encuentra en la
	# lista.
	# Parametros:
	#	self: lista actual
	#	s: clave de tipo string, para el cual se quiere determinar si 
	#	   esta o no en la lista
	# Retorna: Valor booleano que indica si la clave esta o no en la lista
	def __contains__(self, s):
		curNode = self.head
		while curNode is not None and curNode.s != s:
			curNode = curNode.next
		return curNode is not None
	

	
	# Descripcion: Metodo que encuentra el nodo correspondiente a una
	# clave dada en la lista.
	# Parametros:
	#	self: lista actual
	#	s: clave de tipo string que el quiere ser buscado en la lista
	# Retorna: El nodo asociado a la clave s o None si no exite tal nodo
	def find(self, s):
		curNode = self.head
		while curNode is not None and curNode.s != s:
			curNode = curNode.next
		return curNode
	

	# Descripcion: Metodo que dada una clave y una cancion, crea un nuevo
	# nodo con estos datos y los agrega a la lista.
	# Parametros:
	#	self: lista actual
	#	s:    clave de tipo string que sera agregada en la lista
	#	cancion: elemento de tipo Cancion que sera agregado en la lista	
	def add(self, s, cancion):
		newNode = hashEntry(s, cancion)
		newNode.next = self.head
		self.head = newNode
		self.size += 1
	
	
	# Descripcion: Metodo que elimina un nodo correspondiente a una clave
	# dada si esta se encuentra en la lista. Si la clave no se encuentra
	# la lista no sufre modificaciones.
	# Parametros:
	#	self: lista actual
	#	s:    clave de tipo string que sera eliminada de la lista
	def remove(self, s):
		preNode = None
		curNode = self.head
		while curNode is not None and curNode.s != s:
			preNode = curNode
			curNode = curNode.next
		if curNode is None:
			return
		self.size -= 1
		if curNode is self.head:
			self.head = curNode.next
		else:
			preNode.next = curNode.next
	
	# Descripcion: Metodo que muestra el contenido de la lista, desde el.
	# primer nodo. Por cada nodo muestra la clave y los atributos de la
	# cancion correspondiente.
	# Parametros:
	#	self: lista actual	
	def display(self):
		curNode = self.head
		while curNode is not None:
			print(curNode.s)
			curNode.canciones.mostrar()
			curNode = curNode.next

