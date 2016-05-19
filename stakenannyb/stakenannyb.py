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
from setup import setup
from sys import exit, argv

from candiapps.utils import getconf

from os import path, getenv, mkdir, system, getcwd
from subprocess import check_output

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


startmenu = appdata + r'/Microsoft/Windows/Start Menu/Programs/Startup'
sncmd = startmenu + '/stakenammy.cmd'
snpy = r'\stakenannyb.py'


def printoutput(list):
    print('')
    print('\t', end=' ')
    for item in list:
        print(item, end=' ')
    print('\n')

def commandhelp():
    printoutput(listcommands)


def commandcoinssupported():
    printoutput(coinssupported)

def commandquit():
    exit(msgexitu)


def sncmdintegraty(contents):
    currentwd = getcwd()
    searchstrng = currentwd + snpy + ' start' 
    pydir = check_output(['where', 'python']).decode('unicode_escape').split()
    
    return search('pydir[0] ' + 'searchstrng', str(contents))

    if not appdatfilecontents['PID']==apppidstr['PID']:
        
        print('\tAnnother stakenanny session is currently running\n')
        print('\tPlease continue in the stakenanny session that is already running,\n$$')
        isappkill=input('\tOr type: [stopother] to continue with this session amd end the previous session.')
        if not isappkill:
            quit('exit at user request')
        os.system('tskill ' + appdatfilecontents['PID'])
        f.write(appidstr)

def commandstart():
    setup(appdirpath, appdatfile)
    # appfilemakeifno()
    
    while True:
        uinput = input('$$')
        
        if uinput in listcommands:
            globals()[str('command' + uinput.lower())]()
        else:
            print('\"' + uinput + '\"' + ', is not a valid command. Type help for a list of available commands.')
#check to see if the app has already been stared in this windows session
        

if __name__ == "__main__":
    globals()["command"+str(argv[1]).lower()]() 