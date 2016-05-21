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
    return search(r"{'PID':\s\d+}", str(contents))



def isappsessioncurrentifnodo(appdirpath, appdatfile, appdatadirpath):
    

    finddirmakeifno(appdirpath, appdatadirpath)
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
        appdatfilecontents = literal_eval(str(readdatfile(appdatfile)))
    print("this is appdatfilecontents[\'PID\'] " + str(appdatfilecontents['PID']))
    print("this is apppidstr[\'PID\'] " + str(apppidstr['PID']))
    print (str(appdatfilecontents['PID']) + '\=\=' + str(apppidstr['PID']))

    if not appdatfilecontents['PID']==apppidstr['PID']:
        
        print('\tAnnother stakenanny session is currently running\n')
        print('\tPlease continue in the stakenanny session that is already running,\n$$')
        isappkill=input('\tOr type: [stopother] to continue with this session amd end the previous session. ')
        
        
        while isappkill!='stopother':
            isappkill=input('\ttype: [stopother] to continue with this session amd end the previous session. ')

            if isappkill=='stopother':

                system('tskill ' + str(appdatfilecontents['PID']))
            elif not isappkill:
                quit('exit at user request')
            else:
                print('\tInvalid choice. Please type [stopother] or hit ENTER to quit this session')
        
        
        with open(appdatfile, 'w+') as f:
            f.write(str(apppidstr))
    return True