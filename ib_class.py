
from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from datetime import datetime
from ib_function import *


class IB_App(EWrapper, EClient):


    def __init__(self):
        EClient.__init__(self, self)
        
        self.account = "U3821703"
        print(datetime.now())
        self.account = ""
        self.positions_options = []


    def error(self, reqId: int, errorCode: int, errorString: str):
        print(reqId, errorCode, errorString)

    def managedAccounts(self, accountsList: str):
        self.account = accountsList
        # return super().managedAccounts(accountsList)
        

    def position(self, account: str, contract, position: float, avgCost: float):

        if contract.secType == "OPT":
            self.positions_options.append({'合約類型':contract.secType,
                '合約代碼':contract.localSymbol,
                '頭寸': position,
                '行駛價': contract.strike,
                '成本價': round(avgCost/int(contract.multiplier), 2),
                '打和點': breakpoint(contract, avgCost, position),
                '合約方向': contract.right,
                '底層證券': contract.symbol,
                '合約ID': contract.conId,
                '合約貨幣':contract.currency,
                'contract.comboLegs': contract.comboLegs,
                'contract.comboLegsDescrip': contract.comboLegsDescrip,
                'contract.deltaNeutralContract': contract.deltaNeutralContract,
                'contract.exchange': contract.exchange,
                'contract.includeExpired':contract.includeExpired,
                'contract.lastTradeDateOrContractMonth': contract.lastTradeDateOrContractMonth,
                'contract.multiplier': contract.multiplier,
                'contract.primaryExchange': contract.primaryExchange,
                'contract.secId': contract.secId,
                'contract.secIdType': contract.secIdType,
                'contract.tradingClass': contract.tradingClass})


    def positionEnd(self):
        for i in self.positions_options:
            print(i)
        
    def pnl(self, reqId: int, dailyPnL: float, unrealizedPnL: float, realizedPnL: float):
        print(reqId, dailyPnL, unrealizedPnL, realizedPnL)
        # return super().pnl(reqId, dailyPnL, unrealizedPnL, realizedPnL)
    
