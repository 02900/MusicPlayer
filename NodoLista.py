# Descripcion: Clase NodoLista, elementos de la clase ListaReproduccion
# canciones que seran reproducidas
# Autores:
# 	Rubmary Rojas 13-11264
# 	Juan Ortiz    13-11021
# email:
# 	rubmaryrojas@gmail.com
# 	ortiz.juan14@gmail.com


# Descripcion: Clase que implementa el nodo de ListaReproduccion
# Atributos:
#	cancion: instancia de la clase Cancion
#	prev: referencia al nodo anterior
#	next: referencia al proximo nodo
class NodoLista:
	def __init__(self, cancion):
		self.cancion = cancion
		self.prev    = None
		self.next    = None
