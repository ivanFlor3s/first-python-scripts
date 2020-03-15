#!/usr/bin/env python3

#CONTADOR DE CARACTERES EN UN MENSAJE
import pprint #Para un print mas lindo

mensaje = 'QUE QUE QUE ESTAS HACIENDO BAKA NO ME PARSEES WACHO-KUN'
count = {}

for char in mensaje:
	count.setdefault(char,0)
	count[char] += 1

pprint.pprint(count)