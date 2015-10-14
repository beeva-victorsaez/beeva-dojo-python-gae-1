__author__ = 'victor'

import random

class Maleante:
    """ MALEANTE: Inquilinos de una banda peligrosa a los cuales el
    cazarecompensas quiere dar caza"""

    recompensa = 0
    vida = 0
    nombre = ""
    localizacion = [0, 0]

    def __init__(self, num=0):
        self.recompensa = random.randint(0, 100)
        self.vida = random.randint(0,10)
        self.nombre = "Maleante" + str(num)
        self.localizacion = [random.randint(0,20), random.randint(0,20)]



def randomMaleantes(limit):
    """Funcion que devuelve un numero aleatorio de maleantes para iniciar el juego,
    donde el numero maximo lo limita el parametro pasado"""

    lista_maleantes = []
    num_maleantes = random.randint(1, limit)

    i = 0
    while (i < num_maleantes):
        m = Maleante()
        m.__init__(i)
        lista_maleantes.append(m)
        i = i + 1

    return lista_maleantes
