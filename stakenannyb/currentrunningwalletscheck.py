
from subprocess import check_output
from ast import literal_eval
from os import path, remove

def currentrunningwalletscheck(coinlist):
    coinpid = {}
    coinsrunning = 0
    for coin in coinlist:
        
        pidstr = None
        pidstr=str(check_output(r'tasklist /fo csv /nh /fi "imagename eq ' + coin + '\"'),'utf-8').split(',')[1]
        if pidstr:
            coinsrunning+=1
            coinpid[coin] = str(pidstr).replace('\"', '')
    return coinpid, coinsrunning
        
        
        
        #for line in str(check_output("wmic process list")).replace('\'', '').replace('\"c:', '\n\"c:'):
        #    sfile = sfile + line
            #if coin in line:
            #    items = line.split()
            #    return items[2]
        #if path.exists('pidinfo.txt'):
        #    remove('pidinfo.txt')    
        #with open('pidinfo.txt', 'w+') as f:
        #    f.write(str(sfile).replace('\"', ''))
    