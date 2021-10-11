import pandas as pd

column = ["ID","ContractID", "Contract", "LocalSymbol", "Symbol",
          "Position", "Strike", "avgCost", "LastPrice",
          "BreakPoint", "內在價值", "TimeValue", "Call|Put", "LastTradeDate"]

df = pd.DataFrame(columns=column)
df = df.append([{"ID":len(df) + 1000, "LocalSymbol": "QQQ", "SecType": "OPT"}], ignore_index=True)
df = df.append([{"ID":len(df) + 1000, "LocalSymbol": "SPY", "SecType": "STK"}], ignore_index=True)
# print(df[df["ID"]==1000])
# dfDict = df.to_dict("records")
# for i in dfDict:
#     print(i)
# print(df)
# print(df[df["SecType"]=="OPT"])
print(df[df['ID']==1000].to_dict("recoders")[0])

            # self.positions_options.append({'合約類型':contract.secType,
            #     '合約代碼':contract.localSymbol,
            #     '頭寸': position,
            #     '行駛價': contract.strike,
            #     '成本價': round(avgCost/int(contract.multiplier), 2),
            #     '打和點': ibfnc.breakpoint(contract, avgCost, position),
            #     '合約方向': contract.right,
            #     '最後交易日': contract.lastTradeDateOrContractMonth,
            #     '剩餘天數': ibfnc.remaining_day(contract.lastTradeDateOrContractMonth),
            #     '底層證券': contract.symbol,
            #     '合約ID': contract.conId,
            #     '合約貨幣':contract.currency,
            #     'contract.comboLegs': contract.comboLegs,
            #     'contract.comboLegsDescrip': contract.comboLegsDescrip,
            #     'contract.deltaNeutralContract': contract.deltaNeutralContract,
            #     'contract.exchange': contract.exchange,
            #     'contract.includeExpired':contract.includeExpired,
            #     'contract.multiplier': contract.multiplier,
            #     'contract.primaryExchange': contract.primaryExchange,
            #     'contract.secId': contract.secId,
            #     'contract.secIdType': contract.secIdType,
            #     'contract.tradingClass': contract.tradingClass})
