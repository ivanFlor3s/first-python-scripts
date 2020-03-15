#!/usr/bin/env python3

print('A ver vamos a ver que podemos hacer con los if...')
print('Para empezar dame tu edad wachin')
edadString = input()
edadInt = int(edadString)
print('Ok pebete a ver que onda')
if (edadInt > 18):
	print('Te felicito sos mayor, cuidado con la CANA')
	mayor = True

else:
	print('TE felicito no tenes preocupacions mas que quien le va a adar laike a tus posts lil SHIT')
	mayor = False

if mayor: apodo = 'Boober de mierda'
else: apodo = 'Pendejo boludo'
print('DAME ALGO MAS DIFICIL ' + apodo + 'A ver... Decime si tenes auto con 1 o 0')
auto = input()
boolAuto = int(auto)
if (mayor and boolAuto) : print('Sos groso man')
elif not(mayor) : print('ESta bien Kiddo no pasa naranja, cuando seas grando lo comparmo y no vamo de pu')
else: print('NOOOOO Fracasadito')