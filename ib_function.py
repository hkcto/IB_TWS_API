from ibapi.contract import Contract


def breakpoint(contract, avgCost, position) -> int:
    """期權打和點計算.

    計算方法:
    買入期權: 打和點 = 行使價 + 期權金
    賣出期權: 打和點 = 行使價 - 期權金
    
    Args:
        contract: Contract class
        avgCost: 平均成本價
        position: 持有頭寸數量
    
    Returns:
        int(price)
    """

    數量 = position
    # print(position)
    # 數量為 0 即為己平倉, 無需再計算
    if 數量 == 0:
        return 0

    行使價 = contract.strike
    # contract.multiplier 是字符串,所以要先轉為數字
    期權金 = round(avgCost/int(contract.multiplier), 2)
    

    # Long 
    if 數量 > 0:
        price = 行使價 + 期權金
        return round(price, 2)

    # Short 
    price = 行使價 - 期權金
    return round(price, 2)

def remaining_day(day: str):
    """計算期權剩餘天數
    day: 為一個字字符串.
    格式: 20220121"""

    from datetime import datetime
    
    today = datetime.today()
    day = datetime.strptime(day, "%Y%m%d")
    return (day - today).days + 1

def exchangeSmart(exchange):
    """exchange 交易所是否為空
    空:傳回  SMART"""
    if exchange != "":
        return exchange
    return "SMART"




# def contractList(c: Contract):
#     contract = Contract()
#     contract.symbol = c.symbol
#     contract.secType = c.secType
#     contract.exchange = "SMART"
#     contract.currency = 'USD'
#     # contract.primaryExchange = "NASDAQ"

#     return contract
    