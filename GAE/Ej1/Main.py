__author__ = 'victor'

from beans import Maleante
from beans import Chivato
from beans import Cazarecompensas
from beans import Informe
from utils import ClassUtils
from Constants import Constants
from utils import Logger

tiempo = 168                # Tiempo total de la semana (7dias x 24horas)
lista_total_maleantes = []  # Lista inicial de maleantes
lista_total_chivatos = []   # Lista inicial de chivatos
lista_informe = []          # Lista de informes para mostrar el horario

cazarecompensas = ""  # Objeto Cazarecompensas


def setTime(t):
    """ Metodo que setea el tiempo"""

    global tiempo
    tiempo = tiempo - t


def getTime():
    """Metodo que devuelve el tiempo"""

    return tiempo


def init_game():
    """Funcion que genera los datos necesario para realizar el juego. (Todos los datos se generan de forma aleatoria)"""

    global lista_total_maleantes
    global lista_total_chivatos
    global cazarecompensas
    global lista_informe

    # Generamos los listados de Chivatos y Maleantes aleatoriamente.
    lista_total_maleantes = Maleante.randomMaleantes(Constants.NUM_MAX_MALEANTES)
    lista_total_chivatos = Chivato.randomChivatos(Constants.NUM_MAX_CHIVATOS, lista_total_maleantes)


    # ------- Log datos del CAZARECOMPENSAS --------------------------------------------------
    cazarecompensas = Cazarecompensas.init_Cazarecompensas()
    print("______________________________________________________________________________")
    print(" |Nombre:" + str(cazarecompensas.nombre) + "| ingresos:" + str(cazarecompensas.ingresos) +
               "| localizacion:" + str(cazarecompensas.localizacion) + "|")
    # -------------------------------------------------------------------------------------


    # -------- Log datos de los MALEANTES (aleatorios) ---------------------------------------
    Logger.log("- Los maleantes son:" + str(len(lista_total_maleantes)))
    for maleante in lista_total_maleantes:
        print("       |Nombre:" + str(maleante.nombre) + "|  Recompensa:" + str(maleante.recompensa) +
                   "|  Vida:" + str(maleante.vida) + "|  Localizacion:" + str(maleante.localizacion) + "|")
    # -------------------------------------------------------------------------------------


    # --------- Log datos de los CHIVATOS (aleatorios) ----------------------------------------
    print("- Los chivatos son:" + str(len(lista_total_chivatos)))
    for chivato in lista_total_chivatos:
        info_chivato = "       |Nombre:" + chivato.nombre, "| es Maleantes:" + str(chivato.isMaleante) \
                       + "| Localizacion:" + str(chivato.localizacion) + "| situacion maleantes:"
        for maleante in chivato.list_maleantes:
            info_maleante = "   " + maleante.nombre
            info_chivato = str(info_chivato) + str(info_maleante)

        print(str(info_chivato) + "|")
    # ----------------------------------------------------------------------------------------------------
    print("______________________________________________________________________________")
    print("")
    print("El tiempo total que tiene el cazarecompensas es " + str(tiempo))


# ****** RESTO DE METODOS ******************************************************************************

def get_horario():
    """Metodo principal para obtener el resultado del ejercicio, el horario"""

    # Para obtener informacion de los maleantes, lo primero es atrapar un chivato y obtener su informacion.
    global info
    info = Chivato.localizar_chivatos(lista_total_chivatos, cazarecompensas)

    obtener_informacion_1()
    Logger.log('Informacion obtenida: ' + str(info))


    # Mientras no tengamos informacion, consultamos al siguiente chivato
    while ((ClassUtils.isEmpty(cazarecompensas.list_info) == True) and (ClassUtils.isEmpty(info) == False)):
        obtener_informacion_1()
        Logger.log('Informacion obtenida: ' + str(info))

    # Recorrer los maleantes con la informacion obtenida, mientras exista informacion y haya tiempo
    while (ClassUtils.isEmpty(cazarecompensas.list_info) == False and (getTime() > 0)):

        # Buscamos al Maleante mas cercano, de la lista de informacion
        villano = ClassUtils.getCercanoMaleante(cazarecompensas.list_info, cazarecompensas)
        Logger.log("Villano mas cercano: " + str(villano.nombre))

        # Si no se puede atrapar, salimos de la iteracion y obtenemos el informe final
        seguir = atrapar_maleante(villano)
        if (seguir == False):
            return

        # Si la lista con informacion del Cazarecompensas esta vacia, buscamos a otro chivato.
        if (ClassUtils.isEmpty(cazarecompensas.list_info) and
                (not ClassUtils.isEmpty(lista_total_maleantes))):
            obtener_informacion_1()

    Logger.log("Generar informe final")
    generarInforme()


def obtener_informacion_1():
    """ Obtenemos la informacion necesaria de los chivatos, los cuales
    nos daran los datos de los maleantes que ellos conozcan."""

    if (ClassUtils.isEmpty(info)):
        return False
    else:
        # Obtenemos el Chivato mas cercano
        chivato_cercano = ClassUtils.getCercano(info)
        if (chivato_cercano == None):
            return False

        Logger.log("El chivato mas cercano es: " + str(chivato_cercano))
        # Eliminamos el chivato de la lista total de Chivatos.
        del info[chivato_cercano]

        boolean_info = obtener_informacion_2(chivato_cercano)
        if (boolean_info == False):
            obtener_informacion_1()
        else:
            return True


def obtener_informacion_2(chivato_cercano):
    """Metodo que atrapa chivatos para obtener informacion acerca de los maleantes"""

    atrapado = atrapar_chivato(chivato_cercano)
    if (atrapado == True):
        return True
    else:
        return False


def atrapar_chivato(chivato):
    """Metodo que situa al Cazarecompensas en la localizacion del chivato y obtiene su informacion."""

    # Calcula la distancia entre el Cararecompensas y el chivato
    distancia = ClassUtils.getDistancia(chivato, cazarecompensas.localizacion)
    Logger.log("Distancia al chivato mas cercano es: " + str(distancia))

    # Si aun hay tiempo, le da caza para obtener su informacion(solo en caso de que no sea a su vez Maleante)
    if ((getTime() - distancia) < 0):
        info = {}
        return False
    else:
        setTime(distancia)
        lista_total_chivatos.remove(chivato)
        cazarecompensas.localizacion = chivato.localizacion
        Logger.log("La nueva localizacion del Cazarecompensas es: " + str(cazarecompensas.localizacion))

        # Se genera un nuevo informe registrando la informacion de la caza
        nuevo_informe(getTime(), chivato.nombre, chivato.localizacion, 0)
        if (chivato.isMaleante == False):
            setList(chivato.list_maleantes, cazarecompensas.list_info)
            return True

        return False


def setList(listInfo_chivato, listInfo_cararecompensas):
    """Metodo que determina si la informacion aportada por el chivato ya la conoce el Cazarecompensas."""

    for i in listInfo_chivato:
        if (contains(i)):
            listInfo_cararecompensas.append(i)


def contains(maleante):
    """Metodo que comprueba si el maleante pasado como paramtro, se encuentra en la lista de maleantes por atrapar."""

    for m in lista_total_maleantes:
        if (m == maleante):
            return True
    return False


def atrapar_maleante(maleante):
    """Metodo que situa al Cazarecompensas en la localizacion del chivato"""

    # Obtenemos la distancia al maleante pasado como parametro
    distancia = ClassUtils.getDistancia(maleante, cazarecompensas.localizacion)

    # Si hay, tiempo se le da caza, si no se finaliza la caza y se genera el informe.
    if ((getTime() - distancia) < 0):
        return False
    else:
        setTime(distancia)
        cazarecompensas.localizacion = maleante.localizacion

        # Se captura al maleante, se le quita la vida.
        captura = capturarMaleante(maleante)
        if (captura == False):
            return False

        # Finalmente se genera un nuevo informe con los datos de la caza
        nuevo_informe(getTime(), maleante.nombre, maleante.localizacion, maleante.recompensa)
        cazarecompensas.list_info.remove(maleante)
        lista_total_maleantes.remove(maleante)

        return True


def capturarMaleante(maleante):
    """Metodo que se encarga de capturar a un maleante, es decir, de quitarle la vida"""

    if (getTime() - maleante.vida < 0):
        return False

    setTime(maleante.vida)


def nuevo_informe(tiempo, nombre, localizacion, recompensa):
    """Funcion que genera un nueva entidad de tipo Informe y lo aniade a una lista."""

    informe = Informe.nuevo_informe(tiempo, nombre, localizacion, recompensa)
    lista_informe.append(informe)


def generarInforme():
    """Metodo que genera el informe con el resultado del ejercicio."""

    print("###################################################")
    print("INFORME FINAL")
    print("###################################################")
    recompensa = 0

    for inf in lista_informe:
        recompensa = recompensa + inf.recompensa
        Informe.informeToString(inf)
    print("Recompnsa total: " + str(recompensa))

    print("Time sobrante: " + str(getTime()))
    print("###################################################")


# ****** RESTO DE METODOS ******************************************************************************



# //// INICIO: MAIN PRINCIPAL ////////////////////////////////////////

def main():
    # Carga de datos aleatorios para iniciar el juego
    init_game()

    # Funcion principal para resolver el ejericicio.
    get_horario()


if __name__ == "__main__":
    main()
# ////  FIN: MAIN PRINCIPAL ////////////////////////////////////////
