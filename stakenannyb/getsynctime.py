from time import time
import datetime
import calendar

def getsynctime(coin, conn):
    blockcount = conn[coin].getblockcount()
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
        
    