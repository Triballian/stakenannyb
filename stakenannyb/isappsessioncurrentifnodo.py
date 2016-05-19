from finddirmakeifno import finddirmakeifno
from getfilecontents import readdatfile

from filemakeifno import filemakeifno

from ast import literal_eval
from os import getpid, system
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

    if not appdatfilecontents['PID']==apppidstr['PID']:
        
        print('\tAnnother stakenanny session is currently running\n')
        print('\tPlease continue in the stakenanny session that is already running,\n$$')
        isappkill=input('\tOr type: [stopother] to continue with this session amd end the previous session.')
        if not isappkill:
            quit('exit at user request')
        os.system('tskill ' + appdatfilecontents['PID'])
        f.write(appidstr)
    return True