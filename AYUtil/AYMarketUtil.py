# coding=utf-8
from __future__ import absolute_import

from ..AYCore.AYEnv import EPeriodTargetType,EMarketTargetType


"""
市场不同，周期传值不同，在这里把统一的周期转换成市场需要的值
"""
def formatPeriod(market,period):
    if isinstance(period ,EPeriodTargetType) and isinstance (market,EMarketTargetType):
        if market==EMarketTargetType.E_MARKET_TARGET_OKEX:
            if period==EPeriodTargetType.E_PERIOD_TARGET_15_MINUTE:
                return '15min'
            elif period==EPeriodTargetType.E_PERIOD_TARGET_1_DAY:
                return '1day'
            else:
                raise NotImplementedError('{}_{} 尚未实现周期转换'.format(market.value,period.value))
        else:
            raise NotImplementedError('{}_{} 尚未实现周期转换'.format(market.value,period.value))
    else:
        raise TypeError('period or market is error type')


"""
市场不同，传回来的K线不同,在这里输出标准的K线 pands 格式
"""

def formatKLine(market,symbol,json):
    from ..AYMarket.AYDataParser import OKEXParser
    if market==EMarketTargetType.E_MARKET_TARGET_OKEX:
        return OKEXParser(symbol,json).df
    else:
        raise NotImplementedError('{}_{} 未实现 formatKLine'.format(market,symbol.base_quote))