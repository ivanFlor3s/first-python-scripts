#!/usr/bin/env python3
#THE GAME

def frioCaliente(unNumero, elPosta):
	if unNumero > elPosta:
		print('Te juiste bestia')
	elif unNumero < elPosta:
		print('Te quedaste corto')
	else : print('Le pegaste')
#Descarto la funcion porque no se como hacer el break en el for -> Podria ser con  uy  flag pero seria ninuna re cagada\

import random
print('NA NANANA Clave el juegardo que vamos a juegar... Como te llamas pibe?')
nombre = input()
#while(type(nombre) !=)
secretNum = random.randint(1,20)
print('OK, ' + nombre + ' intenta adivinar cual es el numero que estoy pensando entre 1 y 20')

for i in range(6):
	print('Dale pa estoy listo. A ver...')
	respuesta = input()
	if int(respuesta) > secretNum:
		print('Te juiste bestia')
	elif int(respuesta) < secretNum:
		print('Te quedaste corto')
	else : 
		break
if int(respuesta) == secretNum:
	print('GRANDEEEE')
else: 
	print('La proxima padre')




