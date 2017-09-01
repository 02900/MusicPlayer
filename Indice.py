# Descripcion: Clase Indice, implementacion de un diccionario implemen-
# tado como una tabla de hash 
# Autores:
# 	Rubmary Rojas 13-11264
# 	Juan Ortiz    13-11021
# email:
# 	rubmaryrojas@gmail.com
# 	ortiz.juan14@gmail.com


from List import *
from fnvhash import fnv1a_32

# Descripcion: Metodo que implementa la funcion de hash, utilizando la 
# funcion fnv.
# Parametros:
#	s: string que es la clave para aplicar la funcion de hash
#	m: cantidad de slots en la tabla de hash
# Retorna: La funcion fnv del string s, modulo m (fnv(s) % m)
def hashing(s, m):
    k=fnv1a_32(s)
    return k%m

# Descripcion: Clase que implementa el nodo de una tabla de Hash
# Atributos:
#	size: atributo que indica la cantidad de elementos en la tabla
#	buckets: arreglo de listas, donde las nodos de las listas son pares
#			 de un string y un objeto de tipo ListaReproduccion
class Indice:
	def __init__(self):
		self.size = 0
		self.buckets = [List() for i in range(5)]
	
	# Descripcion: Metodo que agrega una cancion al Indice, con una clave
	# dada. Si ya existe dicha clave en el diccionario, se agrega la 
	# cancion a la lista correspondiente. Si no se encuentra la clave, 
	# se crea una nueva lista con una sola cancion y se agrega la lista 
	# asociada a la clave dada.
	# Parametros:
	#	self: indice actual
	#	s: string que es la clave para la cancion
	#	cancion: elemento de tipo Cancion, el cual sera agregado al indice
	def agregar(self, s, cancion):
		k = hashing(s, len(self.buckets))
		Nodo = self.buckets[k].find(s)
		if Nodo is None:
			self.size = self.size + 1
			self.buckets[k].add(s, cancion)
			if 10*self.size > 8*len(self.buckets):
				self.rehash()
		else:
			if not cancion in Nodo.canciones:
				Nodo.canciones.agregar(cancion)
	
	# Descripcion: Metodo que redimensiona la tabla de hash. Si la canti-
	# dad de buckets era m, la nueva cantidad sera 2*m+1. Todos los 
	# elementos que estaban en la tabla, seran reubicados en la nueva 
	# tabla de hash
	# Parametros:
	#	self: indice actual que sera redimensionado
	def rehash(self):
		indice = Indice()
		N = 2*len(self.buckets) + 1
		indice.buckets = [List() for i in range(N)]
		for k in range(len(self.buckets)):
			actual = self.buckets[k].head
			while actual is not None:
				cancionActual = actual.canciones.cabeza
				while True:
					indice.agregar(actual.s, cancionActual.cancion)
					cancionActual = cancionActual.next
					if cancionActual is actual.canciones.cabeza:
						break
				actual = actual.next
		self.buckets = indice.buckets
	
	# Descripcion: Metodo que busca la lista de canciones asociada a una
	# clave dada. Si la clave no se encuentra en el diccionario returna
	# None. 
	# Parametros:
	#	self: indice actual sobre el que se realiza la busqueda
	#	s: string, clave que sera buscada
	# Retorna: Una lista de canciones correspondiente a la clave dada si 
	# esta se encuentra en el diccionario. None si no se encuentra la 
	# clave
	def buscar(self, s):
		k = hashing(s,  len(self.buckets))
		Nodo = self.buckets[k].find(s)
		if Nodo is None:
			return None
		else:
			return nueva_lista(Nodo.canciones)
	'''
	def eliminar(self, s, cancion):
		k = hashing(s, len(self.buckets))
		Nodo = self.buckets[k].find(s)
		if Nodo is None:
			return
		else:
			Nodo.canciones.eliminar(cancion)
			if len(Nodo.canciones)==0:
				self.buckets[k].remove(s)
				self.size -= 1
	'''
	# Descripcion: Metodo que muestra los elementos del indice. Para cada
	# clave muestra los atributos de cada una de las canciones que  
	# corresponden a cada clave.
	# Parametros:
	#	self: indice actual que sera mostrado
	def mostrar(self):
		for k in range(len(self.buckets)):
			self.buckets[k].display()
				
