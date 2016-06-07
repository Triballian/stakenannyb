class Coin(object):
    """Manages all coins and tracks thier progress"""
    stakeenabled=False
    def set_stake(self, boolean):
        self.stakeenabled=boolean
    
    def get_stake(self):
        return self.stakeenabled
    


