## 配置化，自动生成对象


## MarketType (Enum)
    MARKET_OKEX='okex'
    MARKET_HUOBI='huobi'
    MARKET_ZB='zb'

## PeriodType (Enum):
    PERIOD_1_DAY="1day"
    PERIOD_1_MINUTE="1min"
    PERIOD_15_MINUTE="15min"

## OrderStatus (Enum)
    ORDER_STATUS_UN_DEAL="unDeal"
    ORDER_STATUS_PART_DEAL="partDeal"
    ORDER_STATUS_DEAL="deal"
    ORDER_STATUS_CANCELED="canceled"
    ORDER_STATUS_CANCELING="canceling"

## Order (Enum)
    id
    timestamp
    price
    amount
    dealPrice
    dealAmount
    status,
    symbol,
    List TradeFactors

## NetWork
    get(url, params=None, headers=None, retry=3, **kwargs):
    post(url, params=None, headers=None, retry=3, **kwargs):
  
## MarketNetWork
    userInfo(self,)
    kLine(self,symbol,period)
    depth(self,symbol)
    ticker(self,symbol)
    Order buy(self,symbol,price,amount)
    Order sell(self,symbol,price,amount)
    cancel(self,order)

## OKEXMarketNetWork
    ...


## TradeFactor
    bool fitTrade(self,cpair,**kwargs)
    float fitPosition(self,cpair,**kwargs)
    float fitSlippage(self,cpair,**kwargs)

    //订单交易成功后，判断是否需要平仓 true话则保留Order,等待平仓,
    bool fitPositionClose
    float fitDealTrade(self,cpair,**kwargs)
    float fitDealPosition(self,capir,**kwargs)
    float fitDealSlippage(self,cpair,**kwargs)
    
    //挂单时是否需要取消
    fitCancel(self,cpair,**kwargs)
    fitDealCancel(self,cpair,**kwargs)

    submitOrder(self,cpair,**kwargs)
    cancelOrder(self,cpari,**kwargs)


## HeaderWork
List Markets

fun
fit()

collectMessage()
noticeMessage()

getMarket()

## MarketWork

fun
init(self,headerWork,NetWork,**kwargs)
userInfo()
kLine()
ticker()
depth()
buy()
sell()
orders()
cancelOrder()

getHeader(self)
getCpair(self,symbol)

noticeMessage()
reportMessage()

## CPairWork
List UnDealOrders
List DealOrders
List FinishOrders

pd_kLine
period

extra=**kwargs

fun
init(self,marketWork,Symbol,TradeFactor,**kwargs)
fit()
    fitUserInfo()
    fitKLine()
    fitDepth()
    fitUserInfo()
    fitTicker()
    fitOrder()
      order.factors.fitDealTrade()
    fitTrade()
      tradeFactor.fitTrade()

userInfo()
kLine()
ticker()
depth()
buy()
sell()
orders()
cancelOrder()

getMarket(self)
getHeader(self)

reportMessage()
noticeMessage()

