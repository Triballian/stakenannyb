from os import path
from sys import exit
from subprocess import check_output
from re import I, M, findall





def getexenames(coinlist, envars):
    exenames = {}
    for coin in coinlist:  
        print('coin = ' + coin + '\nenvars[coin][0] = ' + str(envars[coin][0]))
              
        if path.exists(envars[coin][0]):
            filedir=envars[coin][0]
            cmdstr=r'dir /b "' + filedir + r'" '
            
            exefilesndir=str(check_output(cmdstr, shell=True), 'utf-8')
            regexstr = r'^'+ coin + r'.*\.exe'
            exenames[coin]=str(findall(regexstr, exefilesndir, I|M)[0])
        else:
            print('\n\tYou did not specify the directory for ' + coin + ' in the stakenanny.conf file. you need to add the line:' + coin + '=[your' + coin + r'coin fulldirectroy path to your executable], \n eample:turbocoin=c:\stakecoins\turbocoin 1.1')
            exit('\n\tplease add path to:' + coin + 'in your stakenanny.conf file')
            
    return exenames          