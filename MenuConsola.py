import reproductor
from Cancion import *
def parseArgs(args):
    msg = "Error en la linea de comando:\npruebaOrdenamiento <archivo de texto>"
    if len(args) != 2:
        print(msg)
        reproductor.sys.exit(1)
    return str(args[1])

def opciones(_reproductor, interfaz):
    while True:
        try:
            print("\nQue desea hacer?:\n1: importar canciones de archivo de texto\n2: eliminar cancion\n3: ordenar por titulo\n4: ordenar por artista\n5: buscar por genero\n6: buscar por artista\n7: restaurar lista de reproduccion\n0: exit")
            opcion=int(input())
            if _reproductor.curState!='playing':
                assert (opcion in [1, 2, 3, 4, 5, 6, 7, 0, -5, -6, -7, -8])            
            else:
                assert (opcion in [])
            break
        except:
            if _reproductor.curState!='playing':
                print("\nNo selecciono una opcion valida")
            else:
                print("\nMientras se esta reproduciendo una cancion no se puede usar el menu")
    return opcion
    
def acciones(interfaz, _reproductor, indice_artista, indice_genero, lista):
    while True:
        accion=opciones(_reproductor, interfaz)
        if accion==1:
            archivo=input("Escriba la ruta de la lista que desea importar: ")
            reproductor.importar(archivo, interfaz, _reproductor, indice_artista, indice_genero)
            interfaz.actualizar_lista(_reproductor)
            
        elif accion==2:        
            titulo=input("Escriba el titulo de la cancion a eliminar: ")
            artista=input("Escriba el artista de la cancion a eliminar: ")
            cancion=Cancion(titulo, '', artista, '')
            reproductor.eliminar_cancion(_reproductor, cancion)
            interfaz.actualizar_lista(_reproductor)
            
        elif accion==3:
            reproductor.ordenar_por_titulo(_reproductor)
            interfaz.actualizar_lista(_reproductor)
            
        elif accion==4:
            reproductor.ordenar_por_artista(_reproductor)
            interfaz.actualizar_lista(_reproductor)
        
        elif accion==5:
            genero=input("Escriba el genero que desea buscar: ")
            reproductor.buscar_por_genero(genero, _reproductor, indice_genero, interfaz)
            interfaz.actualizar_lista(_reproductor)
        
        elif accion==6:
            artista=input("Escriba el artista que desea buscar: ")
            reproductor.buscar_por_artista(artista, _reproductor, indice_artista, interfaz)
            interfaz.actualizar_lista(_reproductor)
            
        elif accion==7:
            reproductor.restaurar_lista_original(lista,_reproductor)
            interfaz.actualizar_lista(_reproductor)
            
        elif accion==-5:
            reproductor.mostrar_lista_actual(_reproductor)
            
        elif accion==-6:
            reproductor.mostrar_lista_original(lista)
            
        elif accion==-7:
            reproductor.mostrar_indice(indice_artista)
            
        elif accion==-8:
            reproductor.mostrar_indice(indice_genero)
                        
        else:
            reproductor.sys.exit()
