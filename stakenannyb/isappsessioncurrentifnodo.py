from finddirmakeifno import finddirmakeifno
from getfilecontents import readdatfile
from filemakeifno import filemakeifno
from ast import literal_eval
from os import getpid
from re import search


def apppid():
    return getpid()

def sessionsdatintegrety(contents):
    print('This is contents : ' + str(contents))
    return search(r"\'\{PID\'\:\s\d+\}", str(contents))



def isappsessioncurrentifnodo(appdirpath, appdatfile):
    

    finddirmakeifno(appdirpath)
    filemakeifno(appdatfile)
    appdatfilecontents = {}
    apppidstr = {}

    #PID 3

    appdatfilecontents = literal_eval(str(readdatfile(appdatfile)))
    print ("This is appdatfilecontents" + str(appdatfilecontents))
    apppidstr['PID'] = apppid()
    if not sessionsdatintegrety(appdatfilecontents):
        print ('writting current pid to disk')
        with open(appdatfile, 'w+') as f:
            f.write(str(apppidstr))
    print("this is appdatfilecontents[\'PID\'] " + str(appdatfilecontents['PID']))
    print("this is apppidstr[\'PID\'] " + str(apppidstr['PID']))

    appdatfilecontents = literal_eval(str(readdatfile(appdatfile)))

    print (str(appdatfilecontents['PID']) + '\=\=' + str(apppidstr['PID']))
    return True