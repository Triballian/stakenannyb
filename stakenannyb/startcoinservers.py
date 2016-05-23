from getpass import getpass
from subprocess import check_output

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
    for coin in coinlist:
        startcmdstr=str(envars[coin][0] + exenames[coin] + '-server -daemon -listen -rpcallowip=127.0.0.1 -rpcuser=stakenanny -rpcpassword=' + password)
        serveroutput=str(check_output( startcmdstr ),'utf-8')
     
def startcoinservers(coinlist,exenames,envars):
    password=getpasswd()
    startservers(coinlist, exenames, envars, password)
    #-server -daemon
    #-rpcuser=stakenanny
    #rpcallowip=127.0.0.1
    #listen=1
    #-server
    #-daemon=1
    
    