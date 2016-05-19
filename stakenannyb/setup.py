from issncmdfileinstartupifnodo import issncmdfileinstartupifnodo
from isappsessioncurrentifnodo import isappsessioncurrentifnodo

def setup(appdirpath, appdatfile, appdatadirpath, appdata, snpy):
    isappsessioncurrentifnodo(appdirpath, appdatfile, appdatadirpath)
    issncmdfileinstartupifnodo(appdata, snpy)
    return True