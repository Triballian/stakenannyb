
from subprocess import check_output
from ast import literal_eval
from os import path, remove

def currentrunningwalletscheck(coinlist):
    for coin in coinlist:
        sfile = str(check_output(r'tasklist /fo csv /nh /fi "imagename eq turbostake.exe"'))
        
        #for line in str(check_output("wmic process list")).replace('\'', '').replace('\"c:', '\n\"c:'):
        #    sfile = sfile + line
            #if coin in line:
            #    items = line.split()
            #    return items[2]
        if path.exists('pidinfo.txt'):
            remove('pidinfo.txt')    
        with open('pidinfo.txt', 'w+') as f:
            f.write(str(sfile[1]))
    