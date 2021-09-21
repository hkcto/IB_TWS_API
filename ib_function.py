def breakpoint(contract, avgCost, position):
    """# 期權打和點計算
    ## 計算方法
    ### 買入期權: 打和點 = 行使價 + 期權金
    ### 賣出期權: 打和點 = 行使價 - 期權金
    """

    數量 = position
    print(position)
    # 數量為 0 即為己平倉, 無需再計算
    if 數量 == 0:
        return 0

    行使價 = contract.strike
    # contract.multiplier 是字符串,所以要先轉為數字
    期權金 = round(avgCost/int(contract.multiplier), 2)
    

    # Long 
    if 數量 > 0:
        price = 行使價 + 期權金
        return price

    # Short 
    price = 行使價 - 期權金
    return price