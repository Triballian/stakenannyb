from issncmdfileinstartupifnodo import issncmdfileinstartupifnodo
from isappsessioncurrentifnodo import isappsessioncurrentifnodo
def setup(appdirpath, appdatfile):
    isappsessioncurrentifnodo(appdirpath, appdatfile)
    issncmdfileinstartupifnodo()
    return True