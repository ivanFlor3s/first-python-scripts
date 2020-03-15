#!/usr/bin/env python3

spam = 'Hello World'

print('Todo en MAYUSCULA \n' + spam.upper()) #Pasa todo a mayusculas

print('Todo en minuscula \n' +spam.lower())


otroString = 'SOY UN STRING'
otroString.islower() # FALSE
otroString.isupper() # TRUE

# isalpha >> dice si solo tiene letras
# isalnum >> True si tiene numeros y letras
# isspace() >> si tiene ful espacios caracter
# istitle() >> todas las palabras empiezaen en Mayuscula
#

spam.startswith('Hello') # retorna True si e string comienza con el string parametro
spam.endswith('World')


#JOIN cuando tenemos muchos strings y necesitamos unirlos con algo

','.join(['cats','rats','bats'])

#SPLIT lo contrario: usa el parametro para separar el String
#'HOla mundo y su buena madre ma mo me mi'.split('m')
#['HOla ', 'undo y su buena ', 'adre ', 'a ', 'o ', 'e ', 'i']


# ljust(int) y rjust(int): Ajusta el string agreando espacios (o el segundo parametro 
# que le pase)para que llegue al length qe paso por parametro

print('hello'.rjust(10))
print('hello'.rjust(10,'@'))
print('hello'.center(20,'-')) #El mejor para mi

#strip() remueve los espacios en blanco (o lo que pasemos por parametro), no modifica el string
#tambien tenemos lstrip() y rstrip()

#replace(lo que se va a reemplazar, por lo que vamos a remplazar) 


#Podemos usar los %d %s %f para poner las variables dentro del string como lo haciamos en C 
#stirng %(parametros)