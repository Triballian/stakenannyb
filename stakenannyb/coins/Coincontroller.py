class Coincontroller(object):
    """description of class"""
    
    
    def __init__(self, coinlist):
        self.coinlist = coinlist
        self.coinsloading = coinlist
        self.loadedwalletstobestakeenabled = coinlist
        self.conns = {} 
        self.coinstobestakeenabled = []
     
    def coinloaded(self, coin):
        self.coinsloading.remove(coin)
        self.coinstobestakeenabled.append(coin)
    
    def get_coinsloading(self):
        if len(self.coinsloading) > 0:
            return self.coinsloading
        else:
            return None

    def get_coinstobestakeenabled(self):
        if len(self.coinstobestakeenabled) > 0:
            return self.coinstobestakeenabled
        else:
            return None
            
    def coinstakeenabled(self, index):
        self.coinstobestakeenabled.pop(index)

    #def get_loadedwalletstobestakeenabled(self, coin):
    #    if self.loadedwalletstobestakeenabled > 0:
    #        return self.loadedwalletstobestakeenabled
    #    else:
    #        return None

    def set_conns(self, coin, conn):
        self.conns[coin] = conn

    def get_conn(self, coin):
        return self.conns[coin]

    def get_conns(self):
        return self.conns

    def set_cfgs(self, cfgs):
        self.cfgs = cfgs

    def get_cfgs(self):
        return self.cfgs

    def get_coinlist(self):
        return self.coinlist

        
    

    #def set_coins(coinlist):
    #    self.coinstotrack = tuple(coinlist)

    
        
    


