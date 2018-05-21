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