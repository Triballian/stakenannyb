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
import ptvsd

from setup import setup
from startcoinservers import startcoinservers
from getexenames import getexenames
from getsynctime import getsynctime
from coins.Coincontroller import Coincontroller


from sys import exit, argv

from candiapps.utils import getconf

from os import path, getenv, mkdir, system


from re import sub, search
from ast import literal_eval
from nt import remove

from coins.Coincontroller import Coincontroller



coinssupported =('turbostake',)
rpcports = {'turbostake': '8454', 'truckcoin': '18776', 'paycon': '9456', 'tekcoin': '18514', 'bottlecaps': '8385', 'stronghands': '6902', 'hyperstake': '18777', '1337': '13372', 'sprouts': '9902', 'pulse': '29996'}
listcommands=('help', 'quit', 'coinssupported', 'coinlist', 'getsynctime')
paramslist={} 
envars = getconf('stakenanny')


    
msgexitu = 'Exited at user request!'

appdata = getenv('appdata')
appdirpath = sub(r'[C|c]:|/$', '', appdata) + '\\stakenanny'
appdatadirpath = appdirpath + '\\data'
appdatfile = appdatadirpath + '\\session.dat'
snpy = 'stakenannyb.py'
startupstatcheckfreqscnds=1

#coinlist = envars['coinlist'].split(',')
#coinlist = str(set(envars['coinlist'])).split()


coinlist = []
try:
    confcoinlist = envars['coinlist']
except KeyError:
    exit('Misssing "coinlist" entry in stakeynanny.conf!')
    
    
for coin in set(confcoinlist):
    coinlist.append(str(coin).lower())
exenames=getexenames(coinlist, envars)


#if len(coinlist)==1:
#    coinlist.append('')

#coinlist = [envars['coinlist'],] 


#def getlist(envarcoinlist):
#    if len(envarcoinlist) == 2:
#        return envarcoinlist
#    elif len(envars['coinlist']) > 2:
#        return set(envarcoinlist)
#    else:
#        return ''
#def getlist(list):
#    used = []
#    return [x for x in list if x not in used and (used.append(x) or True)]


#def getlist2(list):
#    x=0
#    while x < len(list):
#        print(str(list[x].replace(r"' ", r"'")))
#        x+=1

#getlist2(coinlist)
    
def printoutput(list):
    print('')
    print('\t', end=' ')
    for item in list:
        print(item, end=' ')
    print('\n')

def commandhelp():
    printoutput(listcommands)
    return True


def commandcoinssupported():
    printoutput(coinssupported)
    return True

def commandcoinlist():
	printoutput(coinlist)

def commandquit():
    remove(appdatfile)        
    exit(msgexitu)

def commandgetsynctime(getsynctime):
    pass

 
#coinlist = getlist((envars['coinlist'],))
#coinlist = getlist((envars['coinlist'] + ('tek',)))
#coinlist = getlist(map(set,envars['coinlist']))
#list = envars['coinlist'].split(',')
#coinlist = getlist(list)
#your coin turbo stake you have in the coinslist of stakenanny.conf is currently not being run by stakenannb and can't be managed automatically.
#please shut this wallet down then type retry. [killwallet|retry|ignore]
#ignore, currently ignoreing turbostake

def commandstart():
    print(coinlist[0])
    setup(appdirpath, appdatfile, appdatadirpath, appdata, snpy, coinlist, exenames)
    coincontroller = Coincontroller(coinlist, rpcports)
    startcoinservers(coincontroller, exenames, envars, startupstatcheckfreqscnds, appdata)
    conn = coincontroller
    paramslist['getsynctime'] = conn
    
        
    
    # appfilemakeifno()
    
    while True:
        uinput = str(input('$$')).split()
        if len(uinput) > 0:
            if uinput[0].lower() in listcommands:
                if len(uinput) > 1:
                    if uinput[0].lower() in paramslist:
                        globals()[str('command' + uinput[0].lower())](paramslist[uinput[0]](uinput[1].lower()))
                        #globals()[str('command' + uinput[0].lower())](uinput[1].lower())
                    else:
                        print('\"' + uinput[1] + '\"' + ', is not a valid parameter. Type help for a list of available commands and parameters wrapped with bracket example: getsynctime [coin] is typed:/ngetsynctime turbostake')
                        
                else:
                    globals()[str('command' + uinput[0].lower())]()               
            
            else:
                print('\"' + uinput[0] + '\"' + ', is not a valid command. Type help for a list of available commands.')
        else:
            print('invalid command. Type help for a list of available commands.')
            
    
#check to see if the app has already been stared in this windows session
        

if __name__ == "__main__":
    globals()["command"+str(argv[1]).lower()]() 