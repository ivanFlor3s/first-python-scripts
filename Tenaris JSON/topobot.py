#!/usr/bin/env python3

# Este programa va a remplazar el bolubot. Su objetivo es identificar los roles faltantes en el JSON 

# 1 - Gestion de los archivos JSON Y QUERY . TXT (mas adelante ver como hacer la consulta en el servidor)

import re
import os

try:
	jsonFile = open(os.path.join(os.getcwd(),'J.txt'),encoding = 'utf-8-sig')
	queryFile = open(os.path.join(os.getcwd(),'Q.txt'),encoding = 'utf-8-sig')
except:
	print(r'No se encontraron los archivos, recorda que deben tener de nombres: \nJSON: J.txt\n Query: Q.txt')

jsonString = jsonFile.read()
queryString = queryFile.read()

#1.1 Eliminar el caracter Â  del jsonString
Aregex = re.compile(r'Â')

#Remplazo A por caracter blaco
jsonString = Aregex.sub('',jsonString)

#--VER ambos strigns
#print(jsonString)
#print(queryString)

#2 - Parseo de Roles en ambos archivos 

#2.1 - Obtengo Ambas listas
jsonRolesRegex = re.compile(r'roleName\"\:\"(\w* . \w*)')
listRolesJson = jsonRolesRegex.findall(jsonString)

queryString = re.compile(r'Acceso a ').sub('',queryString)
listRolesQuery = queryString.split('\n')

#--VER como estan generandose la lista de ROles
#print(listRolesJson)
#print(listRolesQuery)

#2.2 - Comparo la lista de json con la de los roles para obtener los roles faltantes
#for rol in listRolesJson

def filterRoles(elemento):
	if elemento in listRolesQuery:
		return True
	else:
		return False


#rolesFaltantes = list(set(listRolesJson).symmetric_difference(set(listRolesQuery)))

rolesFaltantes = list(filter(filterRoles,listRolesJson))
# for rol in listRolesJson:
# 	if filterRoles(rol,listRolesQuery):
# 		rolesFaltantes.append(rol)


for r in rolesFaltantes:
	print(r)

print('SIgo vivaracho')
#3 - GEneracion del nuevo JSON

