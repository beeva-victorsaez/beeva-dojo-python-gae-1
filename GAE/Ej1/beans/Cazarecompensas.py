__author__ = 'victor'

class Cazarecompensas:
    """CAZARECOMPENSAS: Persona encargada de dar caza a todos los villanos"""

    nombre = ""
    ingresos = 0
    localizacion = [0, 0]
    list_info = []

    def __init__(self):
        self.nombre = "Cazarecompensas"
        self.ingresos = 0.0
        self.localizacion = [10, 10]

    def setIngresos(self, ingresos):
        self.ingresos = self.ingresos + ingresos

    def setLocalizacion(self, localizacion):
        self.localizacion = localizacion

    def setMapaInfo(self, list_info):
        self.list_info = list_info

def init_Cazarecompensas():
    c = Cazarecompensas()
    c.__init__()
    return c