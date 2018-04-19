
# coding=utf-8

from ..Core.Env import EMarketTargetType

class Symbol(object):

    def __init__(self,market,base,target):
        if isinstance(market,EMarketTargetType):
            self.market=market
            self.base=base
            self.target=target
        else:
            raise TypeError('market type error')
    
    def __str__(self):
        return '{}_{}_{}'.format(self.market,self.base,self.target)
    
    __repr__=__str__


