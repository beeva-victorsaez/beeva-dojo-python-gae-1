__author__ = 'victor'

from utils import Logger

class Informe():

    tiempo = 0
    localizacion = [0, 0]
    nombre = ""
    recompensa = 0

    def __init__(self, tiempo, localizacion, nombre, recompensa):
        self.tiempo = tiempo
        self.localizacion = localizacion
        self.nombre = nombre
        self.recompensa = recompensa

def dia_semana(day):
    switcher = {
        7: "Lunes",
        6: "Martes",
        5: "Miercoles",
        4: "Jueves",
        3: "Viernes",
        2: "Sabado",
        1: "Domingo"
    }
    return switcher.get(day)


def getDay(time):
    """Metodo que devuelve el dia de la semana, en funcion del tiempo"""

    dia = "indefinido"
    if(time <= 24):
        dia = dia_semana(1)
    elif(time > 24 and time <= 48):
         dia = dia_semana(2)
    elif (time > 48 and time <= 72):
        dia = dia_semana(3)
    elif (time > 72 and time <= 96):
        dia = dia_semana(4)
    elif (time > 94 and time <= 120):
        dia = dia_semana(5)
    elif (time > 120 and time <= 144):
        dia = dia_semana(6)
    elif (time <= 168):
        dia = dia_semana(7)

    return dia

def informeToString(informe):
    """Metodo toString del objeto Informe"""

    print("Dia: " + str(getDay(informe.tiempo)))
    print(str(24 - informe.tiempo%24) + " H - " + str(informe.nombre) + " " + str(informe.recompensa) + "pv")

def nuevo_informe(tiempo, localizacion, nombre, recompensa):
    """Metodo que genera un nuevo objeto 'Informe' con la informacion pasada como parametro"""

    informe = Informe(tiempo, nombre, localizacion, recompensa)
    return informe




