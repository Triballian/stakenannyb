
from subprocess import check_output

from os import path, system
from re import search





def listedcoinsrunning(coinlist, exenames):


    coinpid = {}
    coinsrunning = 0

    for coin in coinlist:
        
        
        
        #pidstr=str(check_output(r'tasklist /fo csv /nh /fi "imagename eq ' + coin + '-qt.exe\"'),'utf-8').split(',')
        pidstr=str(check_output(r'tasklist /fo csv /nh /fi "imagename eq ' + exenames[coin]),'utf-8').split(',')
        #pidstr=check_output(r'tasklist /fo csv /nh /fi "imagename eq ' + exenames[coin])

        #pidstr=str(check_output(r'tasklist /fo csv /nh /fi "imagename eq ' + exenames[coin]),'utf-8')
        
        
        if len(pidstr)>1:
            #if 'INFO: No tasks' in pidstr[1]:
            #    pidstr=None
            #    pidstr=str(check_output(r'tasklist /fo csv /nh /fi "imagename eq ' + coin + '-qt.exe\"'),'utf-8').split(',')
            
            coinsrunning+=1
            coinpid[coin] = str(pidstr[1]).replace('\"', '')
            #coinpid[coin] = pidstr[1]
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
    

def currentrunningwalletscheck(coinlist, exenames):
    coinspid, numberofrunningcoins=listedcoinsrunning(coinlist, exenames)
    
    while coinspid:
        print('\tThere are\\is ' + str(numberofrunningcoins) + ' listed coin[s] currently running.\n')
        print('\tPlease shutdown these\\this coin[s] and type: [retry]\n')
        iswalletkill=input('\tOr type: [stopwallets] to allow stakenanny to shutdown these\\this listed coin[s].\n$$ ')
        if iswalletkill=='retry':
                
                coinspid, numberofrunningcoins=listedcoinsrunning(coinlist, exenames)
        elif iswalletkill=='stopwallets':
            for coin in coinspid:
                system('tskill ' + coinspid[coin])
            
            coinspid, numberofrunningcoins=listedcoinsrunning(coinlist, exenames)
            while coinspid:           
                iswalletkill=input('\tStakenanny was unable to kill these\\this wallet[s], please shut them down manually and type: [retry]\n$$')   
                
                coinspid, numberofrunningcoins=listedcoinsrunning(coinlist, exenames)
        else:
            print('Invalid command, please try again.\n\n\n')            
                      
            
            
        
    
        
        
        
       
    