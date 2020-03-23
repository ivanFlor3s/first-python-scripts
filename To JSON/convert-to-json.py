# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
from tkinter import *
import json
import logging
import pyperclip as pp

HEIGHT = 700
WIDTH = 800

def convert(string):
    lista = string.split('\n')
    #Hago un sgrint de mierda y ya fue
    jsonString = '['
    for numero in lista:
        jsonString + r'{"attrs":[],"refnum":"'+ numero + r'"},\n' 
        logging.debug(r'Se agrega: {"attrs":[],"refnum":"'+ numero + r'"}')
    jsonString +']'
    return jsonString

def updateLabel():
    texto.set(pp.paste())


root = Tk()

#root.config(width='650',height='400')

canvas = Canvas(root,height = HEIGHT, width = WIDTH)
canvas.pack()

inputTextLabel = Label(root, text='Input')
inputTextLabel.place(relx = 0.01, y = 0.1)

convertButton = Button(root, text = 'Cargar')
convertButton.place(x=200, y =20)

resetButton = Button(root, text = 'Limpiar')
resetButton.place(x=300, y =20)

# Mostrar el JSON copiade desde portapapeles
texto=StringVar()
texto.set('Esperando...')
inputLabel = Label(root, text ='')
inputLabel.config(textvariable=texto)
inputLabel.place(x=10,y=30)


outTextLabel = Label(root, text='Output JSON')
outTextLabel.place(x = 10, y = 80)

outLabel = Frame(root)
outLabel.place(x =10,y=100)


root.mainloop()



