from ibapi.contract import Contract
from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.ticktype import TickType
import ib_function as ibfnc
import json
from threading import Thread
import pandas as pd

class IB_App(EWrapper, EClient):


    def __init__(self, queue):
        Thread.__init__(self)
        EClient.__init__(self, self)

        ### pandas 測試 Start ###
        column = ["ID", "ContractID", "Contract", "SecType",
                    "LocalSymbol", "Symbol", "Position", "Strike", 
                    "avgCost", "LastPrice", "BreakPoint", "內在價值", 
                    "TimeValue", "Call|Put", "LastTradeDate", "剩餘天數"]
        self.df = pd.DataFrame(columns=column)
        ### pandas 測試 End ###



        
        self.ACCOUNT = "U3821703" # IB Account
        self.positions_options: list = [] # 持倉期權頭寸
        self.positions_opt_contractList = [] # 持倉所有合約頭寸
        
        
        self.reqTableId = 1000
        # reqTable -> reqMktData()
        self.reqTable: dict = {}
        # reqTable -> queue.get(), tickPrice()
        self.reqTableValue: dict = {}

        self.queue = queue

    def error(self, reqId: int, errorCode: int, errorString: str):
        print(reqId, errorCode, errorString)

    def managedAccounts(self, accountsList: str):
        self.account = accountsList
        # return super().managedAccounts(accountsList)
        
    def position(self, account: str, contract: Contract, position: float, avgCost: float):

        # 檢查合約的交易所是否為空,空設置為: SMART, reqMktdata()需要交易的值,不能為空.
        contract.exchange = ibfnc.exchangeSmart(contract.exchange)


        ### pandas 數據格式測試 Start ###
        series = {"ID":len(self.df) +1000, "Contract": contract,
                    "LocalSymbol": contract.localSymbol,
                    "Symbol": contract.symbol, "Strike": contract.strike,
                    "avgCost": avgCost,
                    "SecType": contract.secType}
        self.df = self.df.append(series, ignore_index=True)  
        ### pandas 數據格式測試 End ###

        if contract.secType == "OPT" and position != 0:
            # 添加所有持倉合約頭寸
            self.positions_opt_contractList.append(contract)

            # 生成 reqId 對應表, dict 類型保存
            # self.reqTable[contract.localSymbol] = self.reqTableId
            # self.reqTableValue[self.reqTableId] = contract.localSymbol
            # self.reqTableId = self.reqTableId + 1

            
            # 持倉選擇,這裡是期權頭寸
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
        # print("reqTable", self.reqTable)
        # print("reqTableValue", self.reqTableValue)      
        with open("templates/positions.json", "w", encoding="utf-8") as j:
            options: dict= {"positions": self.positions_options}
            j.write(json.dumps(options, indent=1, ensure_ascii=False,))

        ### pandas 測試 Start ###
        # print(self.df[self.df["SecType"]=="OPT"])
        ### pandas 測試 End ###
        

        

    def tickPrice(self, reqId, tickType: TickType, price: float, attrib):
        """
        tickType:
        4 = LastPrice
        
        all tickType:
        https://interactivebrokers.github.io/tws-api/tick_types.html
        """
        if tickType == 4:
            data =self.df[self.df["ID"]==int(reqId)].to_dict("records")[0]
            
            
            # dict value find key
            # localSymbol = list(self.reqTable.keys())[list(self.reqTable.values()).index(reqId)]
            # print({"localSymbol": reqId, 'tickType': tickType, 'price': price, 'attrib': attrib})

            # print({"price": [{"reqId": reqId, "localsymbol": data['LocalSymbol'],
            #       "price": price}]})
            self.queue.put({
                "price": [{"reqId": reqId,
                        "localsymbol": data['LocalSymbol'], "tickType": tickType, "price": price}]})



        # return super().tickPrice(reqId, tickType, price, attrib)
    
    # def tickGeneric(self, reqId, tickType: TickType, value: float):
    #     print("tickGeneric", {"reqId":reqId, "tickType":tickType, "value":value})
    #     # return super().tickGeneric(reqId, tickType, value)

    # def pnl(self, reqId: int, dailyPnL: float, unrealizedPnL: float, realizedPnL: float):
    #     print(reqId, dailyPnL, unrealizedPnL, realizedPnL)
    #     # return super().pnl(reqId, dailyPnL, unrealizedPnL, realizedPnL)
