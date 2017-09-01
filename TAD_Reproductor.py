# Descripcion: Implementaction de la clase Reproductor abstrayendo la 
# interfaz grafica
# Autores:
# 	Rubmary Rojas 13-11264
# 	Juan Ortiz    13-11021
# email:
# 	rubmaryrojas@gmail.com
# 	ortiz.juan14@gmail.com

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import reproductor

try:
    from PyQt4.phonon import Phonon
except ImportError:
    app = QtGui.QApplication(sys.argv)
    QtGui.QMessageBox.critical(None, "Music Player",
            "Your Qt installation does not have Phonon support.",
            QtGui.QMessageBox.Ok | QtGui.QMessageBox.Default,
            QtGui.QMessageBox.NoButton)
    sys.exit(1)


# Descripcion: Clase que implementa el reproductor
# Atributos:
#	lista: atributo del tipo ListaReproduccion que contiene las canciones
#		   que se reproduciran
#	cancion_actual: atributo que indica la cancion que se reproduce ac-
#					actualmente
class Reproductor(QWidget):
    def __init__(self, lista):
        self.lista=reproductor.nueva_lista(lista)
        self.cancion_actual=self.lista.cabeza
        self.app=QApplication([])
        super(Reproductor, self).__init__()
        self.phonon=Phonon.MediaObject(self)
        self.phonon.setTickInterval(1000)
        self.phonon.tick.connect(self.tick)
        self.path = unicode(self.cancion_actual.cancion.archivo)
        self.phonon.setCurrentSource(Phonon.MediaSource(self.path))
        self.audioOutput = Phonon.AudioOutput(Phonon.MusicCategory, self)
        Phonon.createPath(self.phonon, self.audioOutput)
        self.curState='stopped'
        
        palette = QPalette()
        palette.setBrush(QPalette.Light, Qt.darkGray)
        self.timeLcd = QLCDNumber()
        self.timeLcd.setPalette(palette)
        self.timeLcd.display("00:00") 

    # Descripcion: Metodo que reproduce la cancion actual del reproductor
    # Parametros: 
    #	self: reproductor actual     
    def play(self):
        if self.curState!='playing':
            if self.path != self.cancion_actual.cancion.archivo:
                self.path = self.cancion_actual.cancion.archivo
                self.phonon.setCurrentSource(Phonon.MediaSource(self.path))
            self.phonon.play()
            self.curState='playing'
    
    # Descripcion: Metodo que para la cancion actual del reproductor
    # Parametros: 
    #	self: reproductor actual          
    def stop(self):
        self.phonon.stop()
        self.curState='stopped'
   
    # Descripcion: Metodo que pone en pausa la reproduccion de la 
    # cancion actual del reproductor
    # Parametros: 
    #	self: reproductor actual   
    def pause(self):
        self.phonon.pause()
        self.curState='paused'
   
    # Descripcion: Metodo que actualiza la cancion actual del reproductor
    # en la siguiente en el orden circular de la lista de canciones
    # Parametros: 
    #	self: reproductor actual   
    def siguiente(self):
        if self.curState!='paused':
            self.stop()
            self.cancion_actual=self.cancion_actual.next
            self.path = self.cancion_actual.cancion.archivo
            self.phonon.setCurrentSource(Phonon.MediaSource(self.path))
            self.curState='next'
            self.play()
    
    # Descripcion: Metodo que actualiza la cancion actual del reproductor
    # en la anterior en el orden circular de la lista de canciones
    # Parametros: 
    #	self: reproductor actual       
    def atras(self):
        if self.curState!='paused':
            self.stop()
            self.cancion_actual=self.cancion_actual.prev
            self.path = self.cancion_actual.cancion.archivo
            self.phonon.setCurrentSource(Phonon.MediaSource(self.path))
            self.play()
    
    # Descripcion: Metodo que actualiza el valor de la lista de reproduc-
    # cion por la nueva lista que se da por parametros y se coloca a can-
    # cion actual como la cabeza de lista
    # Parametros: 
    #	self: reproductor actual
    def set_lista(self, lista):
        self.lista = reproductor.nueva_lista(lista)
        self.cancion_actual = self.lista.cabeza
     
    # Descripcion: Metodo que actualiza el tiempo de la cancion
    # Parametros: 
    #	self: reproductor actual
    #	time
    def tick(self, time):
        displayTime = QTime(0, (time / 60000) % 60, (time / 1000) % 60)
        self.timeLcd.display(displayTime.toString('mm:ss'))
