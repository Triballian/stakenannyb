from issncmdfileinstartupifnodo import issncmdfileinstartupifnodo
from isappsessioncurrentifnodo import isappsessioncurrentifnodo
from currentrunningwalletscheck import currentrunningwalletscheck

def setup(appdirpath, appdatfile, appdatadirpath, appdata, snpy, coinlist):
    isappsessioncurrentifnodo(appdirpath, appdatfile, appdatadirpath)
    issncmdfileinstartupifnodo(appdata, snpy)
    currentrunningwalletscheck(coinlist)
    return True