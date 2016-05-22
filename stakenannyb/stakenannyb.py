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
from sys import exit, argv

from candiapps.utils import getconf

from os import path, getenv, mkdir, system


from re import sub, search
from ast import literal_eval
from nt import remove
from getexenames import getexenames

coinssupported =('turbostake',)
listcommands=('help', 'quit', 'coinssupported', 'coinlist') 
envars = getconf('stakenanny')


    
msgexitu = 'Exited at user request!'

appdata = getenv('appdata').replace('\\', '/')
appdirpath = sub(r'[C|c]:|/$', '', appdata) + '/stakenanny'
appdatadirpath = appdirpath + '/data'
appdatfile = appdatadirpath + '/session.dat'
snpy = 'stakenannyb.py'
#coinlist = envars['coinlist'].split(',')
#coinlist = str(set(envars['coinlist'])).split()

coinlist = []
for coin in set(envars['coinlist']):
    coinlist.append(coin)
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