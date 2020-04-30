import csv
from manejadorcamion import manejadorc
class cosechas:
    __lista=[]
    def __init__(self):
        for i in range (20):
            self.__lista.append([])
            for j in range (45):
                self.__lista[i].append(0)
    def carga(self,lcamion):
        archi=open('cosechas.csv')
        reader=csv.reader(archi,delimiter=',')
        for fila in reader:
            
            i=int(fila[0])-1
            j=int(fila[1])-1
            total=int(fila[2])-int(lcamion.tara(i))
            self.__lista[i][j]=int(total)

    def mostrar(self):
        print(self.__lista)
    def peso(self,id):
        total=0
        for i in range (45):
            total+=self.__lista[id][i]
        return total
    def listado(self,dia,m):
        print("PATENTE      CONDUCTOR     CANT.KILOS")
        for i in range (20):
            print(m.patente(i).ljust(2," "),m.conductor(i).center(20," "),self.__lista[i][dia])
            

