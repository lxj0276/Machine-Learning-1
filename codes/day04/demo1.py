# 可以自己import我们平台支持的第三方python模块，比如pandas、numpy等。

# 在这个方法中编写任何的初始化逻辑。context对象将会在你的算法策略的任何方法之间做传递。
def init(context):
    # 在context中保存全局变量
    # context.s1 = "000001.XSHE"
    # 实时打印日志
    # logger.info("RunInfo: {}".format(context.run_info))
    
    # 只运行一次的init
    logger.info('只运行一次的init')

# before_trading此函数会在每天策略交易开始前被调用，当天只会被调用一次
def before_trading(context):
    logger.info('在每天开盘的时候会运行一次 before_trading')


# 你选择的证券的数据更新将会触发此段逻辑，例如日或分钟历史数据切片或者是实时数据切片更新
def handle_bar(context, bar_dict):
    # 开始编写你的主要的算法逻辑

    # bar_dict[order_book_id] 可以拿到某个证券的bar信息
    # context.portfolio 可以拿到现在的投资组合信息

    # 使用order_shares(id_or_ins, amount)方法进行落单

    # TODO: 开始编写你的算法吧！
    # order_shares(context.s1, 1000)
    logger.info('根据频率来运行的次数 handle_bar')

# after_trading函数会在每天交易结束后被调用，当天只会被调用一次
def after_trading(context):
    logger.info('在每天收盘的时候会运行一次 after_trading')