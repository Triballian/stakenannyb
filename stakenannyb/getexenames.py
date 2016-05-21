from os import path
from subprocess import check_output
from re import I, M, findall





def getexenames(coinlist, envars):
    exename = {}
    for coin in coinlist:  
        print('coin = ' + coin + '\nenvars[coin][0] = ' + str(envars[coin][0]))
              
        if path.exists(envars[coin][0]):
            fildedir=envars[coin][0]
            cmdstr=r'dir /b "' + fildedir + r'" '
            
            exefilesndir=str(check_output(cmdstr, shell=True), 'utf-8')
            regexstr = r'^'+ coin + r'.*\.exe'
            exename[coin]=str(findall(regexstr, exefilesndir, I|M)[0])
            
            pass