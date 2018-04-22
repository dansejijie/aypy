
# coding=utf-8
"""
市场模块
"""
from __future__ import absolute_import

from abc import ABCMeta, abstractmethod
from .AYSymbol import Symbol
from ..AYCore.AYEnv import EPeriodTargetType



class BaseMarket(object):
    
    def __init__(self,symbol,*args,**kwargs):
        """网络请求（连接10秒，接收60秒）超时时间"""
        self.K_TIME_OUT = (10, 60)
        if isinstance(symbol,Symbol):
            self.symbol=symbol
            self.init_self(**kwargs)
        else:
            raise TypeError('symbol type is error')

    @abstractmethod
    def init_self(self,**kwargs):
        pass
    def kline(self,period=EPeriodTargetType.E_PERIOD_TARGET_15_MINUTE,n_folds=2,start=None,end=None):
        """K线接口"""
        pass
    def ticker(self,symbol):
        """最新交易信息"""
        pass
    def userinfo(self):
        """用户账号信息"""
        pass
    def order(self,order_id,symbol):
        """订单信息"""
        pass
    def cancelOrder(self,order_id,symbol):
        """取消订单"""
        pass
    def trade(self,amount,price,symbol,type):
        """交易"""
        pass
    def depth(self,symbol,size=1):
        """交易深度"""
        pass
