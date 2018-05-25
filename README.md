# 设计思路

  ## 总思路
    1、一个系统运行里以 Market 为单位，多个 Market 可以信息共享，
    2、一个Market里包含多个交易对，交易对之间信息可共享，
    3、一个交易对的处理受仓位、资金、其他交易对，滑点等影响。
    

  ## 扩展思路
    1、支持网络异常的处理
      1、行情的假数据创造-多 Market 的时候可以从另一个 Market 里获取数据
      2、订单交易的处理
    2、Market支持最新行情数据的 K 线拼接

  ## 实现方法
    1、Market 之间、交易对之间的信息共享：
      1、Market 只作为交易对处理的容器，含有交易对的数组，每个交易对都具有自主处理网络交互能力（由装饰器提供）
      2、Market 提供其他市场（更高层容器提供方法），及内部的交易对信息（实例）的方法。 不提供修改方法
    2、一个交易对包含信息：
      1、附庸的Market、Position、Captial、buyfactory、sellfactory、Slippage,Order,KLine变量
      2、网络请求方法。
      3、检验是否购买的标准。
    3、网络异常（多半不能访问）
      1、错误信息提交，由系统来接受管理。
      2、K线添加上一个相同数据，并标记为假数据。
    4、



1、支持针对订单的买入卖出
2、支持针对仓位的买入卖出 
3、支持订单撤销因子
4、market 具有跟交易所交互功能，K线+ticker 深度，资金， 获取订单，下订单，取消订单等。
具有 kl_pd,capital 等。

## Utils
提供 日志功能（mongodb(release)+console(debug)） logging

## Market 市场
具有 Market 信息
具有 获取内部 CPairWork 功能（主要为了orders）
具有 K、ticker、deepth、capital、order、cancelOrder 方法 参数由 CPairWork 提供

## CPairWork 货币对管理
具有 kl_pd,capital,deepth,orders,
具有 buyFactor,sellFactor cancelFactor,其中sellFactor可以存在于buyFactor,cancelFactor存在于buyFactor和sellFactor,
具有 K、ticker、deepth、capital、order、cancelOrder 方法，调用Market的网络请求方法

## CPair 货币对

## TradeFactor 
具有 PositionFactor , SlippageFactor ,CancelFactor , TradeFactor

## PositionFactor 
具有 fit_position(self,**kwargs) 方法，返回购买或出售数量

## SlippageFactor
具有 fit_price(self,**kwargs) 方法，返回购买或出售价格

## CancelFactor
具有 fit_cancel(self,**kwargs) 方法，返回是否取消单子的

## Order

具有 Market 信息
具有 CPair 信息
订单是否可用 isValid fit_buy_order 会生成对应参数，有时会因仓位等原因无法生成
具有状态信息 0：未提交订单 1：未生成订单 2：部分成交订单 3：全部成交订单 4：撤销中订单 5：已撤销订单
具有 status,price,amount,deal_price,deal_amount 参数
具有 fit_buy_order,fit_sell_order,fit_cancel_order 功能，最终的order,cancelOrder 调用的是 CPairWork

fit_buy_order 用于构造买单，参数

## 配置化，自动生成对象