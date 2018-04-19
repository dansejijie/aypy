
# coding=utf-8
"""
市场模块
"""
from abc import ABCMeta, abstractmethod
from .Symbol import Symbol
from ..Core.Env import EPeriodTargetType

class BaseMarket(object):
    
    def __init__(self,symbol):
        if isinstance(symbol,Symbol):
            self.symbol=symbol
        else:
            raise TypeError('symbol type is error')
    
    @abstractmethod
    def kline(self,periods=EPeriodTargetType.E_PERIOD_TARGET_15_MINUTE,n_folds=2,start=None,end=None):
        """K线接口"""
        pass
