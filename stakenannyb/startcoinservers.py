
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
from User import User
from serializer import serialize, deserialize
from getsynctime import getsynctime
import gevent
from copy import deepcopy




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

def starteachserver(coincontroller, exenames, envars, password, appdata, startupstatcheckfreqscnds):
    coinsp ={}
    cfgs={}
    coinlist = deepcopy(coincontroller.get_coinlist())
    
    for coin in coinlist:
        print(coin)
        seconds = 30
        if coin == 'hyperstake':
            startcmdstr=str(envars[coin][0] + '\\' + exenames[coin] + ' -server -listen=0 -rpcallowip=127.0.0.1 -rpcuser=stakenanny -rpcpassword=' + password)
        else:
            startcmdstr=str(envars[coin][0] + '\\' + exenames[coin] + ' -server -listen -rpcallowip=127.0.0.1 -rpcuser=stakenanny -rpcpassword=' + password)
        
        coinsp[coin]=Popen( startcmdstr )
       
        cfgfname=appdata + '\\' + coin + '\\' + coin + r'.conf'
        if path.exists(cfgfname):
            cfg=read_config_file(cfgfname)
            cfgs[coin]=cfg
            if 'rpcport' in cfg:
                rpcport = cfg['rpcport']
            else:
                rpcport = coincontroller.get_rpcport(coin)
        else:
            rpcport = coincontroller.get_rpcport(coin)
        
        wallet_finished_loading = False
        
        while not wallet_finished_loading:
            coincontroller.set_conns(coin, AuthServiceProxy("http://%s:%s@127.0.0.1:%s"%('stakenanny', password, rpcport)))            
            status = wait_for_wallet_to_finish_loading(coincontroller.get_conn(coin), startupstatcheckfreqscnds)
            if status != 'Request-sent':
                wallet_finished_loading = True
            if coincontroller.get_coinstobestakeenabled():
                gevent.sleep(0)
            else: 
                sleep(startupstatcheckfreqscnds)
        
        coincontroller.coinloaded(coin)
    
    #coincontroller.set_conns(conns)
    coincontroller.set_cfgs(cfgs)     
    #return cfgs, conns

def enablestake(coincontroller, password):
        allwalletsstakeenabled=False
        while not allwalletsstakeenabled:
            coinsloading = coincontroller.get_coinsloading()
            coinstobestakeenabled = coincontroller.get_coinstobestakeenabled()
            if coinsloading or coinstobestakeenabled:
                if coinstobestakeenabled:
                    for index in range(len(coinstobestakeenabled)):
                        coin = coinstobestakeenabled[index]
                        conn = coincontroller.get_conn(coin)
                        
                        time = getsynctime(conn)
                        while time == 'connection lost':
                            print( coin + ' connection lost, reconnecting...')
                            rpcport = coincontroller.get_rpcport(coin)
                            coincontroller.set_conns(coin, AuthServiceProxy("http://%s:%s@127.0.0.1:%s"%('stakenanny', password, rpcport)))
                            time = getsynctime(conn)
                            
 
                        if time > 0 and time < 420:
                        
                            try:
                                conn.walletpassphrase(password, 99999999, True)
                                coincontroller.coinstakeenabled(index)
                                break
                            except Exception as e:
                                timedouterror=search(r'^timed out', str(e))
                                if timedouterror:
                                    coincontroller.coinstakeenabled(index)
                                    break 
                                    #pass
                                else:
                                    print('exit 1')
                                    exit(e)
                    gevent.sleep(0)
                else:
                    gevent.sleep(0)
            else:
                allwalletsstakeenabled = True
        
  
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
            timedout=search(r'^timed out', str(e))
            requestsent=search(r'^Request-sent', str(e))
            
            if walletisstillloading or timedout:
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
            
    
    
   
def startcoinservers(coincontroller, exenames , envars, startupstatcheckfreqscnds, appdata):
    userfile = appdata + '\\' + 'stakenanny' + '\\' + 'user.sav'
    if path.exists(userfile):
        user = deserialize(userfile )
    else:
        user = User()   
        user.set_pwd(getpasswd())
        serialize(user, userfile)
    
    
    #starteachserver(coincontroller, exenames, envars, user.get_pwd(), appdata, startupstatcheckfreqscnds, rpcports)
    gevent.joinall([
    gevent.spawn(starteachserver(coincontroller, exenames, envars, user.get_pwd(), appdata, startupstatcheckfreqscnds)),
    gevent.spawn(enablestake(coincontroller, user.get_pwd())),
    ])

    
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



    
    