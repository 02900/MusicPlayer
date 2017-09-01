# Music Player
Reproductor de musica programado en Python

El cliente debe poder leer archivos en texto plano, donde se encontraran listados la dirección de varios archivos de audio en formato mp3, AVI o OGG. Estos archivos son leídos y cargados como una lista de reproducción para el reproductor, que deben visualizarse en un panel estático de una interfaz gráfica destinada para la lista de canciones a reproducir. El formato del archivo de texto tendría una canción por cada línea y en cada línea los campos se diferenciaran por tabulaciones a modo de columnas de la siguiente forma:
<br /> <br />< titulo > [TAB] < artista > [TAB] < genero > [TAB] < ruta al archivo de audio > <br />
<br />El usuario manejaría una parte de la aplicación por líneas de comandos y otra parte por interfaz gráfica. La ejecución de la aplicación debe hacerse con el comando
<br /><br />> python reproductor .py < archivo >


 El cual genera un menú por consola que permite interactuar al usuario con la aplicación y debe desplegar una interfaz gráfica con los botones del reproductor de música y un panel con la lista de canciones listadas en el archivo de texto plano < archivo > , Las opciones que el menú por consola debe permitir al usuario ejecutar son las siguientes: 
<br />Importar canciones de archivo de texto, 
<br />Eliminar canción, 
<br />ordenar por título, 
<br />ordenar por artista, 
<br />buscar por género, 
<br />buscar por artista, 
<br />restaurar lista de reproducción original. 

Los botones que la interfaz gráfica tiene son las siguientes: play, pause, stop, siguiente y atrás.
