from ib_class import IB_App
from ibapi.contract import Contract

class TWS:
    
    def __init__(self) -> None:
        self.IB_CONFIG = {"host": "192.168.1.158", "port": 7497, "clientId": 0}
        self.ib = IB_App()
        self.ib.connect(**self.IB_CONFIG)
        
    # Requests real-time position data for all accounts.
    def requests(self):
        self.ib.reqPositions()
        
        
        
    
    def run(self):
        self.requests()
        self.ib.run()

if __name__=="__main__":
    import threading as td
    print("auto run")
    app = TWS()
    ib_td = td.Thread(target=app.run)
    ib_td.start()
    ib_td.join(3)

    # reqMktData() 請求市場數據, 注要用於串流報價
    for contract in app.ib.positions_contractList:
        contract: Contract

        if contract.secType == "OPT":   # 請求期權市場數據
            app.ib.reqMktData(app.ib.reqTable[contract.localSymbol], contract, "", False, False, [])