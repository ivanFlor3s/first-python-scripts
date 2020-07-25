# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 22:49:32 2020

@author: Ivan
"""

import tkinter as tk
import logging

logging.basicConfig(level=logging.DEBUG, 
                    format = '%(asctime)s - %(message)s', 
                    datefmt='%Y-%m-%d %H:%M:%S')

ventana = tk.Tk()
ventana.geometry("600x200")


#Logger
def logger(*args):
    
    stringTask = ''
    
    stringTask = inputLabel.get()
    
    #No se loguean tareas en Blanco
    if(len(stringTask) > 0):
        #Logueo de la tarea
        logging.debug(stringTask)
        #Clean box label
        inputLabel.delete(0, tk.END)
    

#Success Logueo
        
        
#LabelS de input
        
inputLabelText = tk.Label(ventana, text="Ingrese la tarea realizada", bg = "yellow")

inputLabelText.pack( fill = tk.X)

btnLoad = tk.Button(ventana, text = "Cargar tarea", command = logger)

btnLoad.pack(side = tk.LEFT)

inputLabel = tk.Entry(ventana, font = "Helvetica 20")

inputLabel.pack(side = tk.RIGHT)
#Enter Key para cargar las tareas
inputLabel.bind("<Return>", logger)
#Logueo de ese imput en un txt

#Creacion de estrutura de carpetas

ventana.mainloop()