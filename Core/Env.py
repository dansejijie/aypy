# -*- encoding:utf-8 -*-
from enum import Enum

class EMarketTargetType(Enum):
    """
    市场类型
    eg.okex,huobi,zb,aex
    """
    E_MARKET_TARGET_OKEX='okex'
    E_MARKET_TARGET_HUOBI='huobi'
    E_MARKET_TARGET_ZB='zb'

class EPeriodTargetType(Enum):
    """
    K线的周期
    """
    E_PERIOD_TARGET_1_DAY="1day"
    E_PERIOD_TARGET_1_MINUTE="1min"
    E_PERIOD_TARGET_15_MINUTE="15min"
