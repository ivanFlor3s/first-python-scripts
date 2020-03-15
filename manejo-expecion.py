#!/usr/bin/env python3
def hacer40DivBy(unNumero):
	try:
		return 40 / unNumero
	except: #PUEDO DEFINIR DE QUE TIPO DE EXCEPCION SE TRATA PERO ASI ES MAS GENERAL ZeroDivisionError:
		print('Division invalida por 0')

print(hacer40DivBy(2))
print(hacer40DivBy(0))
print(hacer40DivBy(10))