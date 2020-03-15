#!/usr/bin/env python3
#LOOP WHILE

index = 0
while index < 5:
	print('SOY UN MENSAJE EN LOOP')
	index += 1
print('Deje el index en ' + str(index))

#TRolerino

print('A ver gaston... Escribime tu direccion')
resp = input()
while(resp != 'tu direccion'):
	print('Dale man no seas trolo pasamelo')
	resp = input()
print('VIste que no costaba nada rinoceronte!!!!')



#LOOP FOR

print('Ahora estamos con FOR papa!!!!!')
print('Sabalero')
for i in range(3):
	print('sabale')
print('roooooooo')

print('Ahora....')
print('Sumemos todos los numeros del 1 al 100 con FOR Padre')
contador = 0
for p in range(101):
	contador += p 
print('El resultado es:' + contador)