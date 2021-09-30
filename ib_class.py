
from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from datetime import datetime
import ib_function as ibfnc


class IB_App(EWrapper, EClient):


    def __init__(self):
        EClient.__init__(self, self)
        
        self.account = "U3821703"
        print(datetime.now())
        self.account = ""
        self.positions_options = []
        self.positions_contractList = []



    def error(self, reqId: int, errorCode: int, errorString: str):
        print(reqId, errorCode, errorString)

    def managedAccounts(self, accountsList: str):
        self.account = accountsList
        # return super().managedAccounts(accountsList)
        
    def position(self, account: str, contract, position: float, avgCost: float):

        if contract.secType == "OPT" and position != 0:
            self.positions_contractList.append(contract)
            self.positions_options.append({'合約類型':contract.secType,
                '合約代碼':contract.localSymbol,
                '頭寸': position,
                '行駛價': contract.strike,
                '成本價': round(avgCost/int(contract.multiplier), 2),
                '打和點': ibfnc.breakpoint(contract, avgCost, position),
                '合約方向': contract.right,
                '最後交易日': contract.lastTradeDateOrContractMonth,
                '剩餘天數': ibfnc.remaining_day(contract.lastTradeDateOrContractMonth),
                '底層證券': contract.symbol,
                '合約ID': contract.conId,
                '合約貨幣':contract.currency,
                'contract.comboLegs': contract.comboLegs,
                'contract.comboLegsDescrip': contract.comboLegsDescrip,
                'contract.deltaNeutralContract': contract.deltaNeutralContract,
                'contract.exchange': contract.exchange,
                'contract.includeExpired':contract.includeExpired,
                'contract.multiplier': contract.multiplier,
                'contract.primaryExchange': contract.primaryExchange,
                'contract.secId': contract.secId,
                'contract.secIdType': contract.secIdType,
                'contract.tradingClass': contract.tradingClass})

    def positionEnd(self):
        import json
        with open("templates/positions.json", "w", encoding="utf-8") as j:
            j.write(json.dumps(self.positions_options, indent=1, ensure_ascii=False,))
        # for i in self.positions_options:
        #     print(i)
        print("positionEnd")

    def tickPrice(self, reqId, tickType, price: float, attrib):
        print({'reqId': reqId, 'tickType': tickType, 'price': price, 'attrib': attrib})
        # return super().tickPrice(reqId, tickType, price, attrib)

    # def pnl(self, reqId: int, dailyPnL: float, unrealizedPnL: float, realizedPnL: float):
    #     print(reqId, dailyPnL, unrealizedPnL, realizedPnL)
    #     # return super().pnl(reqId, dailyPnL, unrealizedPnL, realizedPnL)
    
