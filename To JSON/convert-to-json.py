# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
from tkinter import *
import json
import logging
import pyperclip as pp

HEIGHT =300
WIDTH = 150

logging.basicConfig(filename ='logout.txt',level=logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s') 


root = Tk()
root.geometry('800x800')
root.config(bg='#46b1e0')
def convert():
    lista = texto.get().split('\n')
    logging.debug('Lista antes de convertir: ')
    jsonString = '['
    for numero in lista:
        jsonString + r'{"attrs":[],"refnum":"'+ numero + r'"},\n' 
        logging.debug(r'Se agrega: {"attrs":[],"refnum":"'+ numero + r'"}')
    jsonString +']'
    outLabel.insert(INSERT,jsonString)


def updateLabel():
    inputJsonString = pp.paste()
    texto.set(pp.paste())
    logging.debug(texto.get())

def delContent():
    texto.set('')


inputTextLabel = Label(root, text='Input')
#inputTextLabel.place(relx = 0.01, y = 0.1)
inputTextLabel.grid(row =1,column=1,padx=10,pady=10)

chargeButton = Button(root, text = 'Cargar',command=updateLabel)
#convertButton.place(x=200, y =20)
chargeButton.grid(row =1, column=2,pady=10)

resetButton = Button(root, text = 'Limpiar',command = delContent)
#resetButton.place(x=300, y =20)
resetButton.grid(row=1,column=3,pady=10)

# Mostrar el JSON copiade desde portapapeles
texto=StringVar()
texto.set('Esperando...')

inputLabel = Label(root, text ='')
inputLabel.config(textvariable=texto)
#inputLabel.place(x=10,y=30)
inputLabel.grid(row =2,column=1)
inputLabel.config(bg="#46e091")


#outTextLabel = Label(canvas, text='Output JSON')
#outTextLabel.grid(row=5,column=1)

outLabel = Text(root,height=2,width=60)
#outLabel.place(x =10,y=400)
outLabel.grid(row = 6, column=2,padx=10,pady=10)

convertBotton=Button(root,text='Convertir',command=convert)
convertBotton.grid(row=7,column=1)


root.mainloop()



