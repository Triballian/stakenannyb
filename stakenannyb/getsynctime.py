from time import time
import datetime
import calendar
from re import search

def getsynctime(coin, conn):
    print(coin)
    try:
        blockcount = conn[coin].getblockcount()
    except Exception as e:
        requestsent=search(r'^Request-sent', str(e))
        #requst-sent is basically a broken connection, this needs to be reestablished.
        if requestsent:
            return 'connection lost'    
    blockhash = conn[coin].getblockhash(blockcount)
    block = conn[coin].getblock(blockhash)
    
    crnttime = time()
    if not isinstance( block['time'], int ):
        date_text = block['time'].replace(' UTC', '')
        date = datetime.datetime.strptime(date_text, "%Y-%m-%d %H:%M:%S")
        blocktime = calendar.timegm(date.utctimetuple())
    else:
        blocktime = block['time']
    synctime = crnttime - blocktime
    m, s = divmod(synctime, 60)
    h, m = divmod(m, 60)
    return synctime, print("%d:%02d:%02d" % (h, m, s))
    #return the last time in seconds that the wallet has synced
        
    