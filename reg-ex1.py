#!/usr/bin/env python3

#Asi como cuando hacemos CTRL + F en un Word buscamos algo, lo que hace word por detras es buuscar 
#por (Pattern Mathing) un string que matchee con la busqueda

import re
#Importtamos la bibliteca de regular expresions
phoneNunRex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#Digo como es el pattern de un numero de telefono
print(phoneNunRex.findall('Estas llamando al numero 555-213-1234 estaremos al tanto de tu llamad y te comunicaremos con el nmero \
123-213-5431'))
# Se va a imprimir una lista del estilo con todos los resultados ['555-213-1234', '123-213-5431']

#tambien podemos hacer con un match object mo que entiende el metodo group

mo = phoneNunRex.search('Estas llamando al numero 555-213-1234 estaremos al tanto de tu llamad y te comunicaremos con el nmero \
123-213-5431')
print(mo.group())
# devuelve 555-213-1234

