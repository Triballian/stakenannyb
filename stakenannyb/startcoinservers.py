
from getpass import getpass
#from subprocess import check_output, STDOUT, TimeoutExpired
#from subprocess import call
from subprocess import Popen



def getpasswd():
        confirmation = False
        while confirmation == False:
            p1 = ''
            
            p1 = getpass('Your wallet unlock password:')
            while not p1:                
                print("Password cannot be blank")
                p1 = getpass('Your wallet unlock password:')
            p2 = getpass('Please confirm your password:')
            
                
                
            if p1 == p2:
                confirmation = True
            else:
                print("Passwords did not match. Please try again.")
        return p1

def startservers(coinlist, exenames, envars, password):
    coinsp ={}
    for coin in coinlist:
        seconds = 30
        startcmdstr=str(envars[coin][0] + '\\' + exenames[coin] + ' -server -daemon -listen -rpcallowip=127.0.0.1 -rpcuser=stakenanny -rpcpassword=' + password)
        #startcmdstr=str(envars[coin][0] + '\\' + exenames[coin] + ' -daemon -listen -rpcallowip=127.0.0.1 -rpcuser=stakenanny -rpcpassword=' + password)
        #serveroutput=call( startcmdstr )
        coinsp[coin]=Popen( startcmdstr )
        #try:
        #    serveroutput=str(check_output( startcmdstr, timeout=seconds ),'utf-8')
        #except TimeoutExpired:
        #    pass
     
def startcoinservers(coinlist,exenames,envars):
    password=getpasswd()
    startservers(coinlist, exenames, envars, password)
    #-server -daemon
    #-rpcuser=stakenanny
    #rpcallowip=127.0.0.1
    #listen=1
    #-server
    #-daemon=1
    '''
    Created on Nov 7, 2015

    @author: Noe
    '''

    import bitcoinrpc
    
    from managestake import timelapse
    from bitcoinrpc.exceptions import InsufficientFunds
    conn = bitcoinrpc.connect_to_local(filename='C:\\Users\\Noe\\AppData\\Roaming\\TurboStake\\turbostake.conf', rpcuser='stakenanny', rpcpassword=password)
    info = conn.getinfo()
    print(info)
    #blkage = timelapse.BlockAge(1446916630)
    #print(str(blkage.age()))


    #trans = conn.listtransactions
    #print("Blocks: %i" % info.blocks)
    #print("Connections: %i" % info.connections)
    #for tran in trans(): print("transactoins %s" %  tran)



    
    