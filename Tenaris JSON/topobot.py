#!/usr/bin/env python3

# Este programa va a remplazar el bolubot. Su objetivo es identificar los roles faltantes en el JSON 

# 1 - Gestion de los archivos JSON Y QUERY . TXT (mas adelante ver como hacer la consulta en el servidor)

import re
import os
import json
import logging

logging.basicConfig(level=logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s') 
#Desactivo logueos, en caso de querer verlos 
logging.disable(logging.CRITICAL)

try:
	jsonFile = open(os.path.join(os.getcwd(),'J.txt'),encoding = 'utf-8-sig')
	queryFile = open(os.path.join(os.getcwd(),'Q.txt'),encoding = 'utf-8-sig')
except:
	print(r'No se encontraron los archivos, recorda que deben tener de nombres: \nJSON: J.txt\n Query: Q.txt')



jsonString = jsonFile.read()
queryString = queryFile.read()


jsonFile.close()
queryFile.close()

#1.1 Eliminar el caracter Â  del jsonString
Aregex = re.compile(r'Â')

#Remplazo A por caracter blaco
jsonString = Aregex.sub('',jsonString)

#--VER ambos strigns
logging.debug('Ambos STRINGS:')
logging.debug('JSON: \n' + jsonString)
logging.debug('Query: \n' + queryString)

# tempJsonFile = open('temp.txt','w')
# tempJsonFile.write(jsonString)
# tempJsonFile.close()


#2 - Parseo de Roles en ambos archivos ---------------------------------------------------------------------------------------------

#2.1 - Obtengo Ambas listas
jsonRolesRegex = re.compile(r'roleName\"\:\"(\w* . \w*)')
listRolesJson = jsonRolesRegex.findall(jsonString)

queryString = re.compile(r'Acceso a ').sub('',queryString)
queryString = re.compile(r'\.').sub('',queryString)
listRolesQuery = queryString.split('\n')

#--VER como estan generandose la lista de ROles
logging.debug('Lista de Roles')
logging.debug('Json roles: \n' + str(listRolesJson))
logging.debug('Query roles: \n' + str(listRolesQuery))


#2.2 - Comparo la lista de json con la de los roles para obtener los roles faltantes
#for rol in listRolesJson

def filterRoles(elemento):
	if elemento in listRolesQuery:
		return True
	else:
		return False

cantRolesJson = len(listRolesJson)
cantRolesQuery = len(listRolesQuery)

print('Roles en JSON: ' + str(cantRolesJson))
print('Roles en Query: ' + str(cantRolesQuery))


rolesFaltantes = list(set(listRolesJson) ^ (set(listRolesQuery)))
cantRolesFaltantes = len(rolesFaltantes)

if(cantRolesFaltantes != abs(cantRolesJson - cantRolesQuery)):
	raise Exception ('Algo salio mal: La cantidad de roles faltantes no coincide')

#rolesFaltantes = list(filter(filterRoles,listRolesJson))
# for rol in listRolesJson:
# 	if filterRoles(rol,listRolesQuery):
# 		rolesFaltantes.append(rol)

if cantRolesFaltantes == 0 :
	print('Se generaron todos los roles')
else: 
	print('Roles faltantes: ')
	for r in rolesFaltantes:
		print(r)

#Dejo en rolesFaltantes los roles a generar

#3 - GEneracion del nuevo JSON-----------------------------------------------------
#Deberia poder filtrar en el JSON solo aquellos que tengan los roles faltantes

inputJson = json.loads(jsonString)

outputJson = [x for x in inputJson if (x['roleName'] in rolesFaltantes)]

outputJson = json.dumps(outputJson, ensure_ascii = False).encode('utf-8')
#print(outputJson.decode())
newJsonString = outputJson.decode()


os.makedirs('temp',exist_ok = True)

newJsonFile = open(os.path.join(os.getcwd(),'temp','JSON.txt'),'w',encoding = 'utf-8-sig')
newJsonFile.write(newJsonString)
newJsonFile.close()


#TO DO - Hacer la consulta con la base SQL sin que sea necesario copiar desde la query
#TO DO - Estructura de Logs en carpetas segun Hora