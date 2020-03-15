#!/usr/bin/env python3

#Estructura del dictionario
#Keys y Values
#{key:value}

dic = {'color':'azul','size':'alto','dato':'esta en casa'}

print('Mi auto '+dic['dato'])
#MI AUTO ESTA EN CASA

#Comparacion entre diccionarios no tienen orden, pueden tener 
#	los mismos values y keys en distinto orden y va a devolver true la igualacion


#Chequeo si una key existe en un diccionario
'color' in dic #>>TRUE

list(dic.keys()) #>>Lista de los keys
list(dic.values())# >> Lista de los values 
list(dic.items())# >> Lista de tuplas (key,valor)


#LOOPS

for j in dic.items():
	print(j)

#GET METHOD

dic.get('color',0) #esta funcion me trae el valorde la key color 
#y en el caso de que la Key no exista en el hash me va a devolver el segundo parametre

#Opposite of get Method is SET DEFAULT()

dic.setdefault('estado','activo') #modifica el diccionario SI el key no existe

#-------------------------------------------------------------------------------------------

#PRACTICA

#regex fot phone numbers

phoneRegex = re.compile(r'''
	(((\d\d\d)|(\(\d\d\d\)))?    #Area codigo opcional
	(\s|-)              #primer separador
	\d\d\d              #3 digitos
	-					#separador
	\d\d\d\d
	(((ext(\.)?\s)|x)
	(\d{2,5})))
	''',re.VERBOSE)

#REgex fpr email address
emailREgex = re.compile(r'''
	[a-zA-Z0-9_.+]+	#Name part
	@	#@ symbol
	[a-zA-Z0-9_.+]+	#domain name part
	''',re.VERBOSE)
#GET THE TEXT OFF THE CLIPBOARD
text = pyperclip.paste()

#Extract mails y phones al clipboard
extravtedPhone = phoneRegex.findall(text) #TRAE UNA LISTA DE TUPLAS -> POngo todo en un parentesis para que lo tome como un grupo y hago un loop para traer el primer elemento de las tuplas que me devuelve

allPhoneNUmber = []
for phoneNUmber in extravtedPhone:
	allPhoneNUmber.append(phoneNUmber[0])

extractedEmail = emailREgex.findall(text)

print(allPhoneNUmber)
print(extractedEmail)

#Copio lo extraido al clipboard

resilt ='\n'.join(allPhoneNUmber) + '\n'+'\n'.join(extractedEmail)
