
#Bolubot: pretende facilitar la busqueda de asignaciones de roles que fallaron y asi eliminar posibles errores humanos.
#version: 1.0
#Bolubot recibe dos nombres de archivos y devuelve un archivo con la diferencia.
#Bolubot existe para que ¡Emiliano y Brian me brinden una birra para celebrar los 40min que les devolvi
# cada vez que tenian que relanzar un ticket de estos!
# Colaboración: Emiliano Quinto y Axel Labruna
import sys
import os
file1 = ''
file2 = ''
file3 = ''
# Ask for the Query file and open it
while True:
    try:
        file1 = open(input("Nombre del archivo Query: "),"r")
        break
    except FileNotFoundError:
        print ("¡ATENCION! - El archivo no existe, por favor intenta nuevamente")
# Ask for the JSON file and open it
while True:
    try:
        file2 = open(input("Nombre del archivo JSON: "),"r")
        break
    except FileNotFoundError:
        print ("¡ATENCION! - El archivo no existe, por favor intenta nuevamente")
# Ask for the name of the output file
while True:
    filename = input ("Nombre del archivo solución con su extensión: ")
    if os.path.isfile(filename) or filename == 'filetemp.txt':
       print ("¡ATENCION! - El archivo ya existe, por favor intenta nuevamente")
    else:
        file3 = open(filename,"x")
        break

#filetemp = open('filetemp.txt',"w")

json = file2.readline()
file2.close()

# función que extrae la transacción del Query
def searchquerytran (line):
    tranpfinal=line.find("¬")-2
    tranpinic=line.find("a")+2
    line = line[tranpinic:tranpfinal]
    return line.strip()

# función que extrae el rol del Query
def searchqueryrol (line):
    rolpfinal=line.find(".")
    rolpinic=line.find("¬")+2
    return line[rolpinic:rolpfinal]

pinic=0
pfin=0
# loop que recorre el archivo del query linea por linea
for line in file1:
    pinic = json.find("{") # busco el inicio de un elemento del json
    pfin = json.find("}")+2 # busco el final del elemento del json sumo 2 para posicionarme en la coma ","
    jsonlen=json.__len__() # calculo la longitud del json
    rol=searchqueryrol(line) # asigno el rol a la variable sin caracteres adicionales
    tran=searchquerytran(line) # asigno la transacción sin caracteres adicionales
    while pinic < jsonlen: # loop para buscar en el json el elemento que tiene el rol y la transacción.
        p= json[pinic:pfin].find(rol) # busca si dentro de un unico elemento del json esta 
                                      #presente el rol, si lo encuentra devuelve la posicion 
                                      # de la primera letra, sino devuelve -1
        q= json[pinic:pfin].find(tran) # busca si dentro de un unico elemento del json esta 
                                       # presente el transacción, si lo encuentra devuelve la 
                                       # posicion de la primera letra, sino devuelve -1
        if p > 0 and q > 0: # si ambos valores son mayores que cero, estoy en el elemento a eliminar
            json=json.replace(json[pinic:pfin],"",1) # elimino el elemento desde el "{" que abre hasta la  
                                                     # coma "," que cierra
            pinic = 0 # inicializo para asegurarme que el siguiente query lo busco desde el inicio
            pfin = 0 # inicializo para asegurarme que el siguiente query lo busco desde el inicio
            break # rompo el loop del while puesto que ya elimine la entrada del query
        else:
            pinic = pfin # avanzo el indice del string hasta el siguiente inicio del proximo elemento  
            pfin = json.find("}",pfin)+2 # avanzo el indice hasta el siguiente fin del proximo elemento
            if pfin == "]": # comparo si el fin es igual al fin del json
                pfin = pfin - 1
file2.close()
file3.write(json)
file3.close()