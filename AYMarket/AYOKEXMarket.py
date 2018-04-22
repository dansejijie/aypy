# coding=utf-8
from __future__ import absolute_import

from .AYSymbol import Symbol
from .AYBaseMarket import BaseMarket
from ..AYMarket import AYNetWork
from ..AYCore.AYEnv import EPeriodTargetType,EMarketTargetType
from ..AYUtil.AYMarketUtil import formatPeriod,formatKLine

ticker_url = "https://www.okex.cn/api/v1/ticker.do?symbol="
userinfo_url = "https://www.okex.cn/api/v1/userinfo.do"
order_url = "https://www.okex.cn/api/v1/order_info.do"
cancel_order_url="https://www.okex.cn/api/v1/cancel_order.do"
trade_url="https://www.okex.cn/api/v1/trade.do"
depth_url="https://www.okex.cn/api/v1/depth.do?symbol="
kline_url="https://www.okex.cn/api/v1/kline.do?symbol="

class OKEXMarket(BaseMarket):
    
    def init_self(self,**kwargs):
        self.api_key=kwargs.pop('api_key','xx')
        self.api_secret=kwargs.pop('api_secret','xx')

    def kline(self,period=EPeriodTargetType.E_PERIOD_TARGET_15_MINUTE,n_folds=2,start=None,end=None):
        type=formatPeriod(self.symbol.market,period)
        url=kline_url+self.symbol.base_quote+'&type='+type
        res=AYNetWork.get(url=url, timeout=self.K_TIME_OUT).json()
        if res is not None:
            if "error_code" in res :
                print(res['error_code'])
                return None
            else:
                pd=formatKLine(self.symbol.market,self.symbol.base_quote,res)
                return pd
        else:
            return None


if __name__ == '__main__':
    symbol=Symbol(EMarketTargetType.E_MARKET_TARGET_OKEX,'btc','ltc')
    market=OKEXMarket(symbol)
    market.kline()