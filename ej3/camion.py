class camiones:
    __id=0
    __nomc=""
    __patente=""
    __marca=""
    __tara=0
    def __init__(self,id,nom,pat,marc,tara):
        self.__id=id
        self.__nomc=nom
        self.__patente=pat
        self.__marca=marc
        self.__tara=tara
    def gettara(self):
        return self.__tara
    def getpat(self):
        return self.__patente
    def getnom(self):
        return self.__nomc



        

    
