from cosecha import cosechas
from manejadorcamion import manejadorc
from camion import camiones
def opcion0():
    print("Adiós")

def opcion1():
    x=int(input("ingrese id de camion: "))
    x-=1
    f=l.peso(x)
    print(f)
    

def opcion2():
    h=int(input("ingrese el dia: "))
    h-=1
    l.listado(h,m)





switcher = {
    0: opcion0,
    1: opcion1,
    2: opcion2,
}

def switch(argument):
    func = switcher.get(argument, lambda: print("Opción incorrecta"))
    func()

if __name__ == '__main__':
    l=cosechas()
    m=manejadorc()
    m.crearcamion()
    l.carga(m)
    bandera = False # pongo la bandera en falso para forzar a que entre al bucle la primera vez
    while not bandera:
        print("")
        print("0 Salir")
        print("1 kilos por camion")
        print("2 listado por dia 2")
        
        opcion= int(input("Ingrese una opción: "))
        switch(opcion)
        bandera = int(opcion)==0 # Si lee el 0 cambia la bandera a true y sale del menú