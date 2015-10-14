__author__ = 'victor'

def getNatural(param):
    """Devuelve el numero natural de un numero(las distancias no pueden ser negativas)"""

    if(param < 0):
        return param * -1
    return param


def getDistancia(chivato, localizacion):
    """Determina la distancia que hay desde el Cazarecompensas
    hasta el chivato pasado como parametro"""

    x = getNatural(chivato.localizacion[0] - localizacion[0])
    y = getNatural(chivato.localizacion[1] - localizacion[1])
    return x + y


def getCercano(info):
    """Funcion que devuelve el Chivato mas cercano del Cazarecompensas"""

    menor = 0
    keys = info.keys()
    for k in keys:
        value = info[k]
        if(menor == 0 or value < menor):
            menor = value
            object = k

    if(menor != 0):
        return object
    return None


def getCercanoMaleante(lista, cazarecompensas):
    """Funcion que devuelve el Maleante mas cercano del Cazarecompensas"""

    if(isEmpty(lista)):
        return None
    menor = lista[0]
    for i in lista:
        if(getDistancia(i, cazarecompensas.localizacion) < getDistancia(menor, cazarecompensas.localizacion)):
            menor = i
    return menor

def isEmpty(mapa_info):
    """Metodo que devuelve si un mapa esta vacio(True) o no(False)"""
    for f in mapa_info:
        if f:
            return False
    return True



