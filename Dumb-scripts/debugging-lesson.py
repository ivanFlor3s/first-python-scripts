#!/usr/bin/env python3


#Assert------------------------------------------------------------------
#Podemos usar assert para luego de hacer algo usar una condicion para validar el comportamiento
#en caso de que de false va a tirar error

# Ejemplo del semaforo como diccionario
# > assert 'red' in intersection.values(), 'Ninguna luz es roja' + str(intersection)

# Raise------------------------------------------------------------------
# Podemoshacer un raise de nuestras propias excepciones 
# raise Exception('THis is the error messeage')

#==============================================================================

# Logging -----------------------------------------------------------------

import logging 

logging.basicConfig(level=logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s') 

#sI QUIERO LOGUEAR EN UN ARCHIVO
#logging.basicConfig(filename = 'logout.txt',level=logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s') 


#Pero ivan porque no podemos usar prints como antes
#Una de las ventajas es si queremos podemos desactivar los logs con la siguiente linea
logging.disable(logging.CRITICAL) #va a desactivar los que esten debajo del nivel de Critical

#ENtonces ahora sabemos que hay LOG LEVELS
# debug (low)
# info
# warning
# error
# critical (high)
# eNTNOCES Podemos crear todos los logs de la forma: logging.warning()

def factorial(n):
	logging.debug('Startof program con' + str(n))
	total = 1
	for i in range(1,n+1):
		total *= i
		logging.debug(' i is %s, total is %s' % (i,total))
	logging.debug('Return value is %s' % (total))
	return total

print(factorial(5))

logging.debug('End of program')

#-----------------------------------------------------------------------------------


