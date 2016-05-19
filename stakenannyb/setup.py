from issncmdfileinstartupifnodo import issncmdfileinstartupifnodo
from isappsessioncurrentifnodo import isappsessioncurrentifnodo

def setup(appdirpath, appdatfile, appdata, snpy):
    isappsessioncurrentifnodo(appdirpath, appdatfile)
    issncmdfileinstartupifnodo(appdata, appdatfile, snpy)
    return True