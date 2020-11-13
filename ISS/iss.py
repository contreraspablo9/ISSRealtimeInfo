#Esta aplicación permite observar la posición de la ISS en tiempo real

import tkinter as tk
from PIL import Image, ImageTk 
import sys,math
import json
import urllib.request


"""Interfaz gráfica"""
ventana = tk.Tk() #definimos la ventana de la aplicacion
ventana.title("Realtime ISS Location by @contreraspablo9") #titulo de la ventana
ventana.resizable(width=False, height=False) #tamaño de ventana fijo
ventana.geometry("617x490")
mapa = Image.open("/Users/contr/Desktop/ISS/mapa.gif") #Importar imagen
fondo = ImageTk.PhotoImage(mapa) # declarar el fondo

lienzo = tk.Canvas(ventana, width = "617", height = "490") #creamos un lienzo sobre la imagen
lienzo.create_image(0,0,image = fondo, anchor = "nw")
lienzo.pack(side='top', fill='both', expand = "yes")

#texto fijo:
texto = lienzo.create_text(500,420,text = "Numero de Ocupantes: ", font=("arial", 12),fill = "darkblue")


#crear icono ISS

def actualizar_ubicacion():
    rojo = "#f50505"
    
    #extraer infomacion
    info_iss = urllib.request.urlopen("http://api.open-notify.org/iss-now.json")
    tripulacion = urllib.request.urlopen("http://api.open-notify.org/astros.json")


    ocupantes = json.load(tripulacion)
    posicion = json.load(info_iss)

    numero = ocupantes["number"]
    texto_1 = lienzo.create_text(600,420,text = numero, font=("arial", 20),fill = "darkblue")
    print(posicion["iss_position"])
    x=float(posicion["iss_position"]["longitude"])
    y=float(posicion["iss_position"]["latitude"])

    #convertir unidades 
    x = 1.51 * x + 272 #grados a pixeles
    y = -2.67 * y + 240 #grados a pixeles

    #dibujar icono
    x1, y1 = (x - 5), (y - 5)
    x2, y2 = (x + 5),(y + 5)
    lienzo.create_oval(x1, y1, x2, y2, fill=rojo)
    lienzo.update()

while(1):
    actualizar_ubicacion()

ventana.mainloop() #aplicacion principal