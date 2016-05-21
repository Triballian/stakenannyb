
from subprocess import check_output
from ast import literal_eval
from os import path, remove



def iscoinrunning(coinlist):

    coinpid = {}
    coinsrunning = 0

    for coin in coinlist:
        
        pidstr = None
        print(coin)
        pidstr=str(check_output(r'tasklist /fo csv /nh /fi "imagename eq ' + coin + '-qt.exe\"'),'utf-8').split(',')
        
        if pdirstr=='-qt.exe':
            pass
        else:
            #pidstr=str(check_output(r'tasklist /fo csv /nh /fi "imagename eq ' + coin + '.exe\"'),'utf-8').split(',')
            pidstr=str(check_output(r'tasklist /fo csv /nh /fi "imagename eq ' + coin + '\"'),'utf-8').split(',')
            print(pidstr[1])
        
        #print(str(check_output(r'tasklist /fo csv /nh /fi "imagename eq ' + coin + '\"'),'utf-8').split(',')[1])
        if pidstr:
            #if 'INFO: No tasks' in pidstr[1]:
            #    pidstr=None
            #    pidstr=str(check_output(r'tasklist /fo csv /nh /fi "imagename eq ' + coin + '-qt.exe\"'),'utf-8').split(',')
            
            coinsrunning+=1
            coinpid[str(coin)] = str(pidstr).replace('\"', '').split(',')[1]
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
    

def currentrunningwalletscheck(coinlist):
    iscoinrunning(coinlist)
    
        
        
        
       
    