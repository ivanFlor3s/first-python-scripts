# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 22:49:32 2020

@author: Ivan
"""

import tkinter as tk
import logging
from logging.handlers import TimedRotatingFileHandler


#https://docs.python.org/3/howto/logging.html
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)



handler = TimedRotatingFileHandler('WIFD.log', when="midnight", interval = 1)
handler.suffix = "%Y%m%d"
handler.setLevel(10)


formatter = logging.Formatter("%(asctime)s - %(message)s")
handler.setFormatter(formatter)



logger.addHandler(handler)




ventana = tk.Tk()
ventana.geometry("600x200")


#Creacion de estrutura de carpetas --------------------------------------------------
def crearLog():
    #pwd = os.getcwd()
    #Test folder
    print('Listo')




#Metodo Logger ---------------------------------------------------------------------
def toLog(*args):

    stringTask = ''

    stringTask = inputLabel.get()

    #No se loguean tareas en Blanco
    if(len(stringTask) > 0):
        #Logueo de la tarea
        logger.debug(stringTask)
        #Clean box label
        inputLabel.delete(0, tk.END)


#Success Logueo


#LabelS de input ---------------------------------------------------------------------

inputLabelText = tk.Label(ventana, text="Ingrese la tarea realizada seguido de Enter", bg = "yellow")

inputLabelText.pack( fill = tk.X)

btnLoad = tk.Button(ventana, text = "Cargar tarea", command = toLog)

btnLoad.pack(side = tk.LEFT)

inputLabel = tk.Entry(ventana, font = "Helvetica 20")

inputLabel.pack(side = tk.RIGHT)
#Enter Key para cargar las tareas
inputLabel.bind("<Return>", toLog)



#Logueo de ese imput en un txt



ventana.mainloop()
