#!/usr/bin/env python3
import os 
os.path.join('folder','folder2','folder3') #Va a devolver la ruta uniendo ocn el / o \ segun el OS

os.sep() #devuelve el separador en las rutas segun el OS

#REcorda que para hacer un / es necesario \/ para meter el caracter especial
os.getcwd()#TRae la direccion donde estoy parado
os.chdir('c://') # Cambio de carpeta

os.path.abspath('unArchivo.txt') #Devuelve la ruta relativa en absoluta
os.path.isabs('una ruta') #RETORNA SI EL PATH ES ABSOLUTO TRUE O FALSE

os.path.relpath(ruta1, ruta2) #Devuelve a relative path de la ruta2 en referencia  la ruta2

os.path.dirname() #REtorna la parte de la ruta que no incluye al archivo o al ultimo carpeta
os.path.basename() #REtrna la ultima carpeta / archivo

os.path.exists('unaRuta') #me dice si la ruta existe

os.path.isfile() #Dice si la ruta es para un archivo 
os.path.isdir() #DIce si la ruta es para una carpeta

os.path.getsize(unaARHCIVO) # devuelve el tamanio del archivo en bytes
os.listdir(unaDIreccionDeCarpeta) #devuelve lo que esta en ese directorio

# >>> for file in os.listdir(os.getcwd()):
# ...     if not os.path.isfile(os.path.join('/home/ivan/python-tuto',file)):
# ...             continue
# ...     size += os.path.getsize(os.path.join('/home/ivan/python-tuto',file))
# ... 
# >>> size
# 14094

os.makedirs('/newCarpeta/newCarpeta2') #python crea todas las carpetas que no encuentre dentro de la otra


#-------------------------------------------------------------------------------------------------\

#Files

helloFile = open('c:\\ruta\\ruta2\\hola,undo.txt') # VA A ABRIR EL ARCHIVO EN MODO LECTURA esto es por default en pyhton no voy a podermodificarlo
helloFile.read() # Me va a devolver un string del contenido
helloFile.close()#DEspues de leer cerramos  para volver a leerlo es necesario volver a abrirlo

#READLINES METHODS

helloFile.readlines() #Trae una lista de strings, las separa por los saltos de linea?

#abrir en write mode

helloFile= open('RUTA','w') #Sobreescribe el archivo 
#Append, agrega a en lugar de a  helloFile= open('RUTA','a') agregy no sobreescribe lo que ya esta
# si en abos modos el archivo no existe, python los crea!!!

helloFile = open('nuevo archivo','w')
helloFile.write('holaaaa!')
helloFile.write('holaaaa!')
helloFile.close() #Abri en modo escritura, EScribi y lo cerre

import shelve #para arvhivos binarios


#===========================================================================================================

import shutil
shutil.copy('ruta + archivo', 'otra ruta') #Copia el archivo en la segunda ruta
shutil.copytree('Ruta + Carpeta a copiar','Ruta2') #Copio carpeta 1 y el abol que tiene debajo
shutil.move('ruta + archivo', 'otra ruta') #Muevpo el archivo, tambien puedo usar move para cambiar de nombre algun archivo

#Delete archivos y carpetas

os.unlink('bacon.txt') 
os.rmdir('RUta + carpeta') #Solo las carpetas vacias
shutil.rmtree('ruta + carpeta') #Va a borrar todo lo que esta demtro de la carpeta
#BORRAR es que no lo deja en la bandeja de reciclaje sino que permanentemente lo borra
