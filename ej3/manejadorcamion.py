import csv
from camion import camiones
class manejadorc:
    __lista=[]
    def __init__(self):
        self.__lista=[]

    def crearcamion(self):
        
        archivo=open("camiones.csv")
        reader=csv.reader(archivo,delimiter=',')
        for fila in reader:
            cam=camiones(fila[0],fila[1],fila[2],fila[3],fila[4])
            self.__lista.append(cam)
        return self.__lista
    def tara(self,id):
        return self.__lista[id].gettara()
    def patente(self,i):
        return self.__lista[i].getpat()
    def conductor(self,i):
        return self.__lista[i].getnom()


   