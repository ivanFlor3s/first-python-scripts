#!/usr/bin/env python3

#Podemos decir que en la regular expresion que estamos buscando este repetido  1 o muchas veces 
#Con los operadores * + ?

# ? cero o unez
# * cero o mas
# + por lo menos una vez

import re
batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search('Batwowowowowoman and Batwowoman')
print(mo.group())

# Si busco una especifica cantidad de repeticiones

digRegex = re.compile(r'(Ha){3,5}') #DE 3 a 5 veces debe encontrar el patron
# digRegex = re.compile(r'(Ha){3,}') NO hay maximo
# digRegex = re.compile(r'(Ha){,5}') No hay minimo
# EStos 3 fueron greedy: TRaen el mayor string podsible
# digRegex = re.compile(r'(Ha){3,5}?') Non greedy matching: Va a traer el minimo posible del matcheo
#

#---------------------------------------------------------------------------------------------------

#REGEX CHARACTER CLASSES AND FINDALL METHOD

# SI el regex tiene 0 o 1 grupo findall regresa una lista de srtings
# Si el regex toeme 2 o as grupos, findall devuelve una lista de tuplas de srtings
# \d es una manera corta de (1|2|3|...) es un CHAR CLASS. \w matchea caracteres de palabras
# Uno puede hacer sus proppias clases de -> Si quiero sol vocales [aeiou]
# Con agregar ^[aeiou] va a buscar todos los que no tengan vocales
doubleVocalRegex = re.compile(r'[aeiou]{2}')

#--------------------------------------------------------------------------------------------------

# ^ quiere decir que el string debe empezar con ese patron
# $ significa que el string debe terminar con el patron
# . Matchea con cualquier caracter excepto el de endline
# re.DOTALL como segundo parametro  en re.compile(asdas,re.DOTALL) para qe el punto matchee con saltos de linea
# re.I o re.IGNORECASE va a tomar minusculas y mayusculas por igual

#--------------------------------------------------------------------------------------------------

# sub() regex method -> namesREgec.sub('REDACTED', 'TEXTO')
# Sustituye todos los strings que matcheen con la expresion regular
# Usando \1 , \2 se va a sustituir por los grupos 1 , 2 en el patron del reg
# pasando re.VERBOSE al segundo parametro en em re.compile() nos va a permitir comentarios con # y hacer saltos de linea
# podesmos combinar todos los segunds parametros
# re.DOTALL | re.IGNORECASE | re.VERBOSE

#--------------------------------------------------------------------------------------------------
