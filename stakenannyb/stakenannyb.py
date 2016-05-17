'''
The MIT License (MIT)
Copyright (c) 2016 Noe De La Cruz, Jr

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Created on Apr 16, 2016
@author: Noe De La Cruz


'''

from sys import exit, argv

from candiapps.utils import getconf

from os import path, getenv, mkdir, getpid, system

from re import sub, search
from ast import literal_eval

coinssupported =('turbostake',)
listcommands=('help', 'quit', 'coinssupported') 
envars = getconf('stakenanny')
msgexitu = 'Exited at user request!'

appdata = getenv('appdata').replace('\\', '/')
appdirpath = sub(r'[C|c]:|/$', '', appdata) + '/stakenanny'
appdatadirpath = appdirpath + '/data'
appdatfile = appdatadirpath + '/session.dat'
apppidstr = {}



def printoutput(list):
    print('')
    print('\t', end=' ')
    for item in list:
        print(item, end=' ')
    print('\n')

def readdatfile():
    with open(appdatfile, 'r') as f:
        d = f.read()
        if not 'PID' in d:
            return "{'PID': ''}"
        return d


def commandhelp():
    printoutput(listcommands)


def commandcoinssupported():
    printoutput(coinssupported)

def commandquit():
    exit(msgexitu)

def appdirmakeifno():
    # PID 1
    print('this is appdirapth: ' + appdirpath)
    if not (path.isdir(appdirpath)):
        mkdir(appdirpath)
    if not (path.isdir(appdatadirpath)):
        mkdir(appdatadirpath)
    return True

def apppid():
    return getpid()



def appfilemakeifno():
    # PID 2
    if not (path.exists(appdatfile)):

        open(appdatfile, 'w')
        

def sessionsdatintegrety(contents):
    print('This is contents : ' + str(contents))
    return search(r"\'\{PID\'\:\s\d+\}", str(contents))


def isappsessioncurrentifnodo():
    appdirmakeifno()
    appfilemakeifno()
    appdatfilecontents = {}
    #PID 3

    appdatfilecontents = literal_eval(str(readdatfile()))
    print ("This is appdatfilecontents" + str(appdatfilecontents))
    apppidstr['PID'] = apppid()
    if not sessionsdatintegrety(appdatfilecontents):
        print ('writting current pid to disk')
        with open(appdatfile, 'w+') as f:
            f.write(str(apppidstr))
    print("this is appdatfilecontents[\'PID\'] " + str(appdatfilecontents['PID']))
    print("this is apppidstr[\'PID\'] " + str(apppidstr['PID']))

    appdatfilecontents = literal_eval(str(readdatfile()))

    print (str(appdatfilecontents['PID']) + '\=\=' + str(apppidstr['PID']))


    if not appdatfilecontents['PID']==apppidstr['PID']:
        
        print('\tAnnother stakenanny session is currently running\n')
        print('\tPlease continue in the stakenanny session that is already running,\n$$')
        isappkill=input('\tOr type: [stopother] to continue with this session amd end the previous session.')
        if not isappkill:
            quit('exit at user request')
        os.system('tskill ' + appdatfilecontents['PID'])
        f.write(appidstr)

def commandstart():
    # appfilemakeifno()
    isappsessioncurrentifnodo()

    while True:
        uinput = input('$$')
        
        if uinput in listcommands:
            globals()[str('command' + uinput.lower())]()
        else:
            print('\"' + uinput + '\"' + ', is not a valid command. Type help for a list of available commands.')
#check to see if the app has already been stared in this windows session
        

if __name__ == "__main__":
    globals()["command"+str(argv[1]).lower()]() 