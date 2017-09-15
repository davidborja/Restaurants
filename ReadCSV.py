#Algoritmo de lectura de Archivo formato csv

#importacion de libreria para expresiones regulares
import re

#importacion de los modelos
from app.models import Restaurants


#Apertura de archivo en forma de lectura
FileCSV = open('restaurantes.csv', 'r')


FileCSV.readline()

#Lectura linea a linea del archivo
for line in FileCSV:

 if re.search('".+".+',line):
  LineText=re.split('(,"|",)',line)
  ListaA=LineText[0].split(",")
  ListaB=LineText[4].split(",")  
  #Ingreso de los datos linea a linea a la base de datos

  r=Restaurants(rating=int(ListaA[1]),name=LineText[2],site=ListaB[0],email=ListaB[1],phone=ListaB[2],street=ListaB[3],city=ListaB[4],state=ListaB[5],lat=float(ListaB[6]),lng=float(ListaB[7]))
  r.save()

 else:
  LineText=line.split(",")
  lastsize=len(LineText)-1
  LineText[lastsize]=LineText[lastsize].replace("\n","")
  #Ingreso de los datos linea a linea a la base de datos

  r=Restaurants(rating=int(LineText[1]),name=LineText[2],site=LineText[3],email=LineText[4],phone=LineText[5],street=LineText[6],city=LineText[7],state=LineText[8],lat=float(LineText[9]),lng=float(LineText[10]))
  r.save()
