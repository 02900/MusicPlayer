# Descripcion: Cliente que ejecuta el reproductor
# Autores:
# 	Rubmary Rojas 13-11264
# 	Juan Ortiz    13-11021
# email:
# 	rubmaryrojas@gmail.com
# 	ortiz.juan14@gmail.com

from ListaReproduccion import *
from Indice import *
from TAD_Reproductor import *
from TAD_InterfazGrafica import *
from MenuConsola import *

def importar(archivo, interfaz, reproductor, indice_artista, indice_genero):
    with open(archivo, 'r') as f:
        for i in f:
            C_info=i.split('\t')
            C_info[-1]=C_info[-1].strip()
            if '.mp3' or '.avi' or '.ogg' in C_info[3]:
                cancion=Cancion(C_info[0], C_info[2], C_info[1], C_info[3])
                #Si el reproductor ha sido inicializado agrega las canciones al reproductor
                if reproductor is not None:
                    reproductor.lista.agregar(cancion)
                    indice_artista.agregar(cancion.artista, cancion)
                    indice_genero.agregar(cancion.genero, cancion)
                else:
                    lista.agregar(cancion)
            else:
                print '\nAlgunas canciones no se han podido importar. Las canciones deben estar en formato mp3, avi o ogg'
    f.closed
    return reproductor

def restaurar_lista_original(lista, reproductor):
    reproductor.set_lista(lista)

def eliminar_cancion(reproductor, c):
    reproductor.lista.eliminar(c)
    if c.es_igual(reproductor.cancion_actual.cancion):
         reproductor.cancion_actual = reproductor.lista.cabeza

def ordenar_por_titulo(reproductor):
    reproductor.lista.ordenar_titulo()
    reproductor.cancion_actual=reproductor.lista.cabeza

def ordenar_por_artista(reproductor):
    reproductor.lista.ordenar_artista()
    reproductor.cancion_actual=reproductor.lista.cabeza
    
def buscar_por_genero(genero, reproductor, indice_genero, interfaz):
    reproductor.lista=indice_genero.buscar(genero)
    if reproductor.lista is not None:
        reproductor.cancion_actual=reproductor.lista.cabeza
    
def buscar_por_artista(artista, reproductor, indice_artista, interfaz):
    reproductor.lista=indice_artista.buscar(artista)
    if reproductor.lista is not None:
        reproductor.cancion_actual=reproductor.lista.cabeza

def play(reproductor):
    reproductor.play()

def seleccionar(reproductor):
    reproductor.seleccionar()

def stop(reproductor):
    reproductor.stop()
    
def pause(reproductor):
    reproductor.pause()
    
def siguiente(interfaz, reproductor):
    reproductor.siguiente()
    interfaz.ActualizarCancion(reproductor.cancion_actual.cancion)
    
def atras(interfaz, reproductor):
    reproductor.atras()
    interfaz.ActualizarCancion(reproductor.cancion_actual.cancion)
    
def mostrar_lista_original(lista):
    if lista is not None:
        lista.mostrar()
    
def mostrar_lista_actual(reproductor):
    if reproductor.lista is not None:
        reproductor.lista.mostrar()
        
def mostrar_indice(indice):
    if indice is not None:
        indice.mostrar()

def actualizar_indice_artista(indice_artista, reproductor):
    c_actual = reproductor.cancion_actual
    if len(reproductor.lista)==0:
        return
    while True:
        indice_artista.agregar(c_actual.cancion.artista, c_actual.cancion)
        c_actual = c_actual.next
        if c_actual is reproductor.cancion_actual:
            return

def actualizar_indice_genero(indice_genero, reproductor):
    c_actual = reproductor.cancion_actual
    if len(reproductor.lista)==0:
        return
    while True:
        indice_genero.agregar(c_actual.cancion.genero, c_actual.cancion)
        c_actual = c_actual.next
        if c_actual is reproductor.cancion_actual:
            return

def inicializar_cliente(lista):
    app=QApplication([])
    reproductor=Reproductor(lista)
    indice_artista=Indice()
    actualizar_indice_artista(indice_artista, reproductor)
    indice_genero=Indice()
    actualizar_indice_genero(indice_genero, reproductor)
    return app, reproductor, indice_artista, indice_genero

if __name__=="__main__":
    lista=ListaReproduccion()
    archivo = parseArgs(sys.argv)
    importar(archivo, None, None, None, None)
    
    app, reproductor, indice_artista, indice_genero=inicializar_cliente(lista)
    interfaz=InterfazGrafica(reproductor)
    interfaz.show()
    interfaz.actualizar_lista(reproductor)
    
    acciones(interfaz, reproductor, indice_artista, indice_genero, lista)
