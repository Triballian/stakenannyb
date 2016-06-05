
from getpass import getpass
#from subprocess import check_output, STDOUT, TimeoutExpired
#from subprocess import call
from subprocess import Popen
from re import search
from sys import exit
from os import path
from time import sleep
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
    
from managestake import timelapse
#from bitcoinrpc.exceptions import InsufficientFunds
from bitcoinrpc.config import read_config_file




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

def starteachserver(coinlist, exenames, envars, password, appdata, startupstatcheckfreqscnds, rpcports):
    coinsp ={}
    cfgs={}
    
    for coin in coinlist:
        seconds = 30
        startcmdstr=str(envars[coin][0] + '\\' + exenames[coin] + ' -server -listen -rpcallowip=127.0.0.1 -rpcuser=stakenanny -rpcpassword=' + password)
        #startcmdstr=str(envars[coin][0] + '\\' + exenames[coin] + ' -daemon -listen -rpcallowip=127.0.0.1 -rpcuser=stakenanny -rpcpassword=' + password)
        #serveroutput=call( startcmdstr )
        coinsp[coin]=Popen( startcmdstr )
        #try:
        #    serveroutput=str(check_output( startcmdstr, timeout=seconds ),'utf-8')
        #except TimeoutExpired:
        #    pass
        #return cfg for each coin
        cfgfname=appdata + '\\' + coin + '\\' + coin + r'.conf'
        if path.exists(cfgfname):
            cfg=read_config_file(cfgfname)
            cfgs[coin]=cfg
            if 'rpcport' in cfg:
                rpcport = cfg['rpcport']
            else:
                rpcport = rpcports[coin]
        else:
            rpcport = rpcports[coin]
            
        #    if 'rpcport' in cfg:
        #        conns[coin] = AuthServiceProxy("http://%s:%s@127.0.0.1:%s"%('stakenanny', password, cfg['rpcport']))
        #    else:
        #        conns[coin] = AuthServiceProxy("http://%s:%s@127.0.0.1:%s"%('stakenanny', password, rpcports[coin]))
        #else:
        #    conns[coin] = AuthServiceProxy("http://%s:%s@127.0.0.1:%s"%('stakenanny', password, rpcports[coin]))
        
        conns={}
        wallet_finished_loading = False
        
        while not wallet_finished_loading:
            #conns[coin] = AuthServiceProxy("http://%s:%s@127.0.0.1:%s"%('stakenanny', password, rpcport))
            conns[coin] = AuthServiceProxy("http://%s:%s@127.0.0.1:%s"%('stakenanny', password, rpcport))            
            status = wait_for_wallet_to_finish_loading(conns[coin], startupstatcheckfreqscnds)
            if status != 'Request-sent':
                wallet_finished_loading = True
            
            
    return cfgs, conns
        
  
def wait_for_wallet_to_finish_loading(rpc_connection, startupstatcheckfreqscnds):
    walletisstillloading='yes'
    status = None
    sendcount=0
    while walletisstillloading:
        sendcount += 1
        try:
            rpc_connection.getinfo()
            walletisstillloading=None
        except Exception as e:
            walletisstillloading=search(r'^\[WinError 10061\]', str(e))
            requestsent=search(r'^Request-sent', str(e))
            if walletisstillloading:
                sleep(startupstatcheckfreqscnds)
            elif requestsent:
                status=requestsent.group(0)
                walletisstillloading=None
            else:
                print('exit 1')
                exit(e)
             #print(e.error.values)
        else:
            walletisstillloading=None
    return status
            
    
    
   
def startcoinservers(coinlist, exenames ,envars, startupstatcheckfreqscnds, appdata, rpcports):
    password=getpasswd()
    cfgs, conns=starteachserver(coinlist, exenames, envars, password, appdata, startupstatcheckfreqscnds, rpcports)
    return conns
    #continuekey=input('press a key to continue:')
    #-server -daemon
    #-rpcuser=stakenanny
    #rpcallowip=127.0.0.1
    #listen=1
    #-server
    #-daemon=1
   

    
    
    
    #conn = bitcoinrpc.connect_to_local(filename='C:\\Users\\Noe\\AppData\\Roaming\\TurboStake\\turbostake.conf', rpcuser='stakenanny', rpcpassword=password)
    #conn = bitcoinrpc.connect_to_local(filename='C:\\Users\\Noe\\AppData\\Roaming\\TurboStake\\turbostake.conf')
    
    #best_block_hash = rpc_connection.getbestblockhash()
    #print(rpc_connection.getblock(best_block_hash))
    #best_block_hash = rpc_connection.getinfo()
    
    
    
    
   
       

    #Checking the wallet status every halfsecond would be reasonable
    #the connectino error happens at the print line

    #info = conn.getinfo()
    #print(info)
    #blkage = timelapse.BlockAge(1446916630)
    #print(str(blkage.age()))


    #trans = conn.listtransactions
    #print("Blocks: %i" % info.blocks)
    #print("Connections: %i" % info.connections)
    #for tran in trans(): print("transactoins %s" %  tran)



    
    