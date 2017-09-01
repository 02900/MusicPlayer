# Descripcion: Implementacion de mergesort para listas circulares
# canciones que seran reproducidas
# Autores:
# 	Rubmary Rojas 13-11264
# 	Juan Ortiz    13-11021
# email:
# 	rubmaryrojas@gmail.com
# 	ortiz.juan14@gmail.com


from Cancion   import *
from NodoLista import *

# Descripcion: Metodo que divide una lista circular en dos listas donde
# de forma balanceada 
# Parametros:
#	subList: apuntador a la cabeza de la lista
# Retorna: Un apuntador a la cabeza de la segunda lista, la primera lista
# tiene como cabeza a subList
def _splitList(subList):
	
	midPoint = subList
	tail = subList.prev
	tail.next = None
	curNode = midPoint.next
	
	while curNode is not None:
		curNode = curNode.next
		
		if curNode is not None:
			midPoint = midPoint.next
			curNode = curNode.next
		
	rightList = midPoint.next
	tail.next = rightList
	rightList.prev = tail
	midPoint.next = subList
	subList.prev = midPoint
	
	return rightList

# Descripcion: Implementacion de mergesort para ordenar una lista circular
# segun el comparador esmenor_artista
#	theList: apuntador a la cabeza de la lista que quiere ser ordenada
# Retorna: Un apuntador a la cabeza de una lista que contiene los 
# elementos de la lista de theList pero de forma ordenada segun el compa-
# rador esmenor_artista
def llistMergeSort_artista(theList):	
	if theList is None:
		return None
	if theList is theList.next:
		return theList
	rightList = _splitList(theList)
	leftList  = theList	
	leftList  = llistMergeSort_artista(leftList)
	rightList = llistMergeSort_artista(rightList)
	theList = _mergeLists_artista(leftList, rightList)	
	return theList

# Descripcion: Metodo que implementa el "merge" de dos listas ya ordenadas
# segun el comparador esmenor_artista
# Parametros:
#	subListA: apuntador a la cabeza de la primera lista ordenada
#	subListB: apuntador a la cabeza de la seguna lista ordenada
# Retorna: Un apuntador a la cabeza de una lista que contiene los 
# elementos de subListA y subListB de forma ordenada segun el comparador 
# esmenor_artista
def _mergeLists_artista(subListA, subListB):
	
	tailA = subListA.prev
	tailA.next = None
	tailB = subListB.prev
	tailB.next = None
	newList = NodoLista(None)
	newTail = newList
	
	while subListA is not None and subListB is not None:
		if subListA.cancion.esmenor_artista(subListB.cancion):
			newTail.next = subListA
			subListA.prev = newTail
			subListA = subListA.next
		else:
			newTail.next = subListB
			subListB.prev = newTail
			subListB = subListB.next
		newTail = newTail.next
		newTail.next = None
	
	if subListA is not None:
		newTail.next = subListA
		subListA.prev = newTail
		newTail = tailA
	elif subListB  is not None:
		newTail.next = subListB
		subListB.prev = newTail
		newTail = tailB
		
	head = newList.next
	newTail.next = head
	head.prev = newTail
	return head

# Descripcion: Implementacion de mergesort para ordenar una lista circular
# segun el comparador esmenor_titulo
#	theList: apuntador a la cabeza de la lista que quiere ser ordenada
# Retorna: Un apuntador a la cabeza de una lista que contiene los 
# elementos de la lista de theList pero de forma ordenada segun el compa-
# rador esmenor_titulo
def llistMergeSort_titulo(theList):
	if theList is None:
		return None
	if theList is theList.next:
		return theList
	rightList = _splitList(theList)
	leftList  = theList	
	leftList  = llistMergeSort_titulo(leftList)
	rightList = llistMergeSort_titulo(rightList)
	theList = _mergeLists_titulo(leftList, rightList)	
	return theList


# Descripcion: Metodo que implementa el "merge" de dos listas ya ordenadas
# segun el comparador esmenor_titulo
# Parametros:
#	subListA: apuntador a la cabeza de la primera lista ordenada
#	subListB: apuntador a la cabeza de la seguna lista ordenada
# Retorna: Un apuntador a la cabeza de una lista que contiene los 
# elementos de subListA y subListB de forma ordenada segun el comparador 
# esmenor_titulo
def _mergeLists_titulo(subListA, subListB):
	
	tailA = subListA.prev
	tailA.next = None
	tailB = subListB.prev
	tailB.next = None
	newList = NodoLista(None)
	newTail = newList
	
	while subListA is not None and subListB is not None:
		if subListA.cancion.esmenor_titulo(subListB.cancion):
			newTail.next = subListA
			subListA.prev = newTail
			subListA = subListA.next
		else:
			newTail.next = subListB
			subListB.prev = newTail
			subListB = subListB.next
		newTail = newTail.next
		newTail.next = None
	
	if subListA is not None:
		newTail.next = subListA
		subListA.prev = newTail
		newTail = tailA
	elif subListB  is not None:
		newTail.next = subListB
		subListB.prev = newTail
		newTail = tailB
		
	head = newList.next
	newTail.next = head
	head.prev = newTail
	return head
	

# Descripcion: Metodo que ordena una lista circular segun el comparador 
# esmenor_artista utilizando el algoritmo mergesort
# Parametros:
#	Lista: objeto de tipo ListaReproduccion que sera ordenado
# Retorna: Una lista circular con los elementos de Lista de forma 
# ordenada segun el comparador esmenor_artista
def mergesort_artista(Lista):
	cabeza = Lista.cabeza
	Lista.cabeza = llistMergeSort_artista(cabeza)

# Descripcion: Metodo que ordena una lista circular segun el comparador 
# esmenor_titulo utilizando el algoritmo mergesort
# Parametros:
#	Lista: objeto de tipo ListaReproduccion que sera ordenado
# Retorna: Una lista circular con los elementos de Lista de forma 
# ordenada segun el comparador esmenor_titulo
def mergesort_titulo(Lista):
	cabeza = Lista.cabeza
	Lista.cabeza = llistMergeSort_titulo(cabeza)
	
	
	
