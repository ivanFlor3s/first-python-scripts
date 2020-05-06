# -*- coding: utf-8 -*-
"""
Created on Tue May  5 21:08:46 2020

@author: Ivan
"""

import PyPDF2 as pdf
import re

#Abro el archivo
file = open('catalogo.pdf','rb')

#Cuento paginas
reader = pdf.PdfFileReader(file)
paginas = reader.numPages

# Obtengo de una pagina
page = reader.getPage(1)
string =page.extractText()

reTalle = re.compile(r'\d\d?')
numerosList = reTalle.findall(string)

reNombre = re.compile(r'(.*)\n')
listNombre = reNombre.search(string).group()

talles = []
nombres = []


# loop en paginas para extract
for pageNum in range(1,paginas):
   texto = reader.getPage(pageNum).extractText()
   talles.append(reTalle.findall(texto))
   nombres.append(reNombre.search(texto).group())
    
