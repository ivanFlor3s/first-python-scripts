#!/usr/bin/env python3
#Manejo de Lista
miLista = ['primero','segundo','ULTIMO']
print(miLista[0])

#Listas en las listas

otraLista = [[10,2,32,310],['cadena','string','hola']]
#accedo al primer elemento de la segunda lista
print(otraLista[1][0])

#Puedo acceder con un index negativo -> Se invierte el sentido en que se recorre la Lista
print(miLista[-1])

#Slice : algunaLIsta[indice donde emppieza:indice que se quita] Devuelve una nueva lista

#Los strings se comportan como las listas (Lista de caracteres CHAR)

# elemento in Lista > Me devuelve True si el elemento esta en la lista
# elemento not in hace lo contrario

#--------------------------------------------------------------------------------

# Loops + Listas

for i in [0,1,2,3]:
	print(i)

#es igual a 
for i in range(4):
	print(i)
#Hacemos la lista 0,1,2,3 mas facil
list(range(4))
list(range(0,100,2)) #lista hasta el 99 con los multiplos de 2


#EL FAMOSO: for i in range(len(someList)) es muy usado para recorrer una lista y asignar nuevos valores o imprimir

#MULTIPLY ASIGNMENT TRICK Python

dog = ['alto','negro','hambiento','saludable']
altura,color,hambre,salud=dog 
#Se asignaron los atrbutos del perro a las variables 

#----------------------------------------------------------------------------------------

#Swap variables en Python

a='aaa'
b='bbb'

a,b = b,a #Aca hago el SWAPPEO

#----------------------------------------------------------------------------------------

#LIST METHODS

dog.index('alto') #REturn el indice donde se encuentra el elemento en la lista en este caso es>0
#Devuelve lel primer indice donde encuentra el elemento

dog.append('algo') #agrega el string al final de la lista

dog.insert(1,'algo') # agrega el elemento en el indice que le pasemos por paramertro

dog.remove('alto') #elimina el primer elmento que encuentre con ese string

#tambien podemos hacer
del dog[0]

numeros = [1,5,3,98,2,325]
numeros.sort() #ORDENA LA LISTA tanto para strigs como para numeros 
#Si  le paso como parametro sort(reverse=True) lo hace en sentido contrario
#Solo ordena listas con todos los elementos del mismo tipo
#CUando se ordena por strings se hace diferencia entre MAYUSCULAS y minusculas-> LOS ORDENA POR SU VALOR EN Ascii


#----------------------------------------------------------------------------------------

#Strings comportamiento similar al de una lista Diferencias String inmutable lista mutable 
#REferencias: Psa algo parecido que con los punteros digamos que tengo una Lista lista1 y 
#hago que lista2 sea igual a lista 1 , lo que estoy haciendo es que ambas tapunten al mismo 
#lugar en memoria es decir que cuando modifico cualquiera de las listas la otra tambien se va a ver afectada (VARIABLES EL TIPO MUTABLES)

#SOLUCION

import copy
lista1 = ['A','B','C']
#lista2 = lista 1 MALLL
lista2 = copy.deepcopy(lista1) #Se va a crear la lista en un lugar distinto de memoria

