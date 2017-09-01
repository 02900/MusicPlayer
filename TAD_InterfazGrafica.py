# Descripcion: Clase con los metodos y atributos para el manejo de la 
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
from PyQt4.phonon import Phonon
import reproductor

# Descripcion: clase que permite el manejo de la interfaz grafica del 
# reproductor.
class InterfazGrafica(QWidget):
    def __init__(self, repro):
        super(InterfazGrafica, self).__init__()
        self.setWindowTitle(self.tr("Reproductor De Musica"))
        self.setMinimumSize(550, 250)
        self.repro=repro
        
        vbox=QVBoxLayout(self)
        hboxA=QHBoxLayout(self)
        hboxB=QHBoxLayout(self)
        
        #initiate table
        self.table=QTableWidget()
        self.tableItem=QTableWidgetItem()
        self.table.setRowCount(10)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(QString("Titulo;Artista;Genero;").split(";"))
        self.table.show()
        vbox.addWidget(self.table)    

        # Create textbox
        self.textbox = QLabel(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280,40)
        self.textbox.setStyleSheet('color: orangered') #teal #crimson
        vbox.addWidget(self.textbox)
        
        self.phonon=self.repro.phonon
        self.slide=Phonon.SeekSlider(self.phonon, self)
        hboxA.addWidget(self.slide)
        hboxA.addWidget(self.repro.timeLcd)
        
        self.volumeSlider = Phonon.VolumeSlider(self)
        self.volumeSlider.setAudioOutput(self.repro.audioOutput)
        self.volumeSlider.setSizePolicy(QSizePolicy.Maximum,
                QSizePolicy.Maximum)
  
        volumeLabel = QLabel()
        volumeLabel.setPixmap(QPixmap('images/volume.png'))
        
        vbox.addLayout(hboxA)
        #Botones
        self.rep=QPushButton(self.style().standardIcon(QStyle.SP_MediaPlay), '')
        self.pausar=QPushButton(self.style().standardIcon(QStyle.SP_MediaPause), '')
        self.parar=QPushButton(self.style().standardIcon(QStyle.SP_MediaStop), '')       
        self.prev=QPushButton(self.style().standardIcon(QStyle.SP_MediaSkipBackward), '')
        self.next=QPushButton(self.style().standardIcon(QStyle.SP_MediaSkipForward), '')

        hboxB.addWidget(self.rep)
        hboxB.addWidget(self.pausar)
        hboxB.addWidget(self.parar)
        hboxB.addWidget(self.prev)
        hboxB.addWidget(self.next)
        hboxB.addWidget(self.volumeSlider)
        vbox.addLayout(hboxB)    

        self.connect(self.rep, SIGNAL("clicked()"), self.play)
        self.connect(self.pausar, SIGNAL("clicked()"), self.pause)
        self.connect(self.parar, SIGNAL("clicked()"), self.stop)
        self.connect(self.prev, SIGNAL("clicked()"), self.atras)
        self.connect(self.next, SIGNAL("clicked()"), self.siguiente)
        self.phonon.finished.connect(self.siguiente)
        
    def play(self):
        reproductor.play(self.repro)

    def stop(self):
        reproductor.stop(self.repro)
        
    def pause(self):
        reproductor.pause(self.repro)
        
    def atras(self):
        reproductor.atras(self, self.repro)
    
    def siguiente(self):
        reproductor.siguiente(self, self.repro)
    
    def agregar_cancion(self, cancion):
        self.i=self.i+1
        self.table.setRowCount(self.i+1)
        self.table.setItem(self.i,0,QTableWidgetItem(cancion.titulo))
        self.table.setItem(self.i,1,QTableWidgetItem(cancion.artista))
        self.table.setItem(self.i,2,QTableWidgetItem(cancion.genero))
        self.table.item(self.i,0).setBackground(QColor(255,255,224))
        self.table.item(self.i,1).setBackground(QColor(255,255,224))
        self.table.item(self.i,2).setBackground(QColor(255,255,224))

    def actualizar_lista(self, new_repro):
        self.repro=new_repro
        self.i=-1
        c_actual = self.repro.cancion_actual
        self.textbox.setText(c_actual.cancion.titulo + ' - ' + c_actual.cancion.artista)
        if self.repro.lista is None:
            return
        else:
            if len(self.repro.lista)==0:
                return
            while True:
                self.agregar_cancion(c_actual.cancion)
                c_actual = c_actual.next
                self.table.resizeColumnsToContents()
                if c_actual is self.repro.cancion_actual:
                    return
                    
    def ActualizarCancion(self, cancion):
        self.textbox.setText(cancion.titulo + ' - ' + cancion.artista)
