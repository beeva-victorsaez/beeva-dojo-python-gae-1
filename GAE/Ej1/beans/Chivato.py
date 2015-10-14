__author__ = 'victor'

from utils import ClassUtils

import random


class Chivato:
    """CHIVATO: es la figura que ayuda al Cazarecompensas a
    localizar a los maleantes"""

    nombre = ""
    isMaleante = False
    localizacion = [0, 0]
    list_maleantes = []

    def __init__(self, maleantes=[], i=0):
        self.nombre = "Chivato" + str(i)
        self.isMaleante = randomBoolean()
        self.localizacion = [random.randint(0,20), random.randint(0,20)]
        self.list_maleantes = getMaleantes(maleantes)



def randomChivatos(limit, maleantes):
    """Funcion que devuelve un numero aleatorio de maleantes para iniciar el juego,
    donde el numero maximo lo limita el parametro pasado"""

    lista_chivatos = []
    num_chivatos = random.randint(1, limit)

    i = 0;
    while(i < num_chivatos):
        c = Chivato()
        c.__init__(maleantes, i)
        lista_chivatos.append(c)
        i = i + 1
    return lista_chivatos

def randomBoolean():
    """Funcion que devuelve aleatoriamente SI o NO"""

    aleatorio =  random.randint(0, 1)
    if(0 == aleatorio):
        return True
    else:
        return False


def getPosition(total, list_posiciones_guardadas):
    """Devuelve aleatoriamente un maleante de  la lista, sin que pueda esta ya almacenado"""

    posicion = random.randint(0, total - 1)
    for p in list_posiciones_guardadas:
        if(p == posicion):
            return getPosition(total, list_posiciones_guardadas)

    return posicion


def getMaleantes(maleantes):
    """Funcion que te devuelve un numero aleatorio de maleantes, entre los existentes"""

    num_maleantes = random.randint(0, len(maleantes))
    list_maleantes = []
    list_posiciones_guardadas = []

    i = 0;
    while(i < num_maleantes):
        posicion = getPosition(len(maleantes), list_posiciones_guardadas)
        list_posiciones_guardadas.append(posicion)

        list_maleantes.append(maleantes[posicion])
        i = i + 1
    return list_maleantes


def localizar_chivatos(chivatos, cazarecompensas):
    """Devuelve un mapa de la localizacion de los chivatos
    como key   -> el nombre del chivato
    como valor -> la distancia"""

    info_chivato = {}
    for c in chivatos:
        chivato = c
        distancia = ClassUtils.getDistancia(chivato, cazarecompensas.localizacion)
        info_chivato.update({chivato : distancia})
        #print(info_chivato)
    return info_chivato

def chivatoToString(chivato):
    Logger.log("     Chivato: |", chivato.nombre, " |", chivato.localizacion," |", chivato.isMaleante)


