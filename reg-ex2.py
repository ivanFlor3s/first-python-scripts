#!/usr/bin/env python3

# Podemos crear grupos en los regex strings con parentesis
import re

RegExBoo = re.compile(r'(\d\d\d)-(\d\d\d-\d)')
mo = RegExBoo.search('El numero en el mensaje es: 513-213-2  Gracias')
print(mo.group(1))
# SE va a imprimir el primer grupo
# 513


#Ahora.. si queremos que se contemple el caso de encontrarse con un parentess es necesario hacer lo mismo que con los digitos: '\('
#Asi si se va a buscar que matchee el parentesis en la estructura

#Despues uso del pipeline para que matchee con cualcquiera de las opciones despues de  prefijo Bat ( en este caso)

RegExBat = re.compile(r'Bati(movil|cinto|traje|leche)')
mo2 = RegExBat.search('Yo soy un Bati porque ando en Batimovil, vamo los Batileche a  ponernos el Baritraje')
print(mo2.group())
print(RegExBat.findall('Yo soy un Bati porque ando en Batimovil, vamo los Batileche a  ponernos el Baritraje')) 