__author__ = 'victor'

#Fichero de texto donde guardar logs
f = None

debug = False
info = False
textTile = False

def log(cadena):
    """Metodo para mostrar los logs"""

    if(info == True):
        print("INFO: |", str(cadena))
    elif(debug == True):
        print("DEBUG: |", str(cadena))
    elif(textTile == True):
        file = getFile()
        file.write(str(cadena) + "\n")


def getFile():
    global f
    if(f == None):
        f = open('logs', 'w')
        return f
    return f