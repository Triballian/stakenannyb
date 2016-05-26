'''
Created on Nov 8, 2015

@author: Noe
'''
import time
class BlockAge(object):
    '''
    takes timestamp integer of block, ex. BlockAge(blockstamp=1446916630)
    returns float, current age of the block
    '''


    def __init__(self, blockstamp=1):
        '''
        Constructor
        '''
        self.blockstamp = blockstamp
    
    def age(self):
        #=======================================================================
        # subract block time  from local time, divide a day(measured in seconds) and the whole thing by 60
        #=======================================================================
        ltimestamp = int(time.time())
        return (ltimestamp - self.blockstamp)/1440/60.0