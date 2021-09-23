
from ib_class import IB_App

class TWS:
    IB_CONFIG = {"host": "192.168.1.158", "port": 7497, "clientId": 0}
    tws = IB_App()


    tws.connect(**IB_CONFIG)
        
    tws.reqPositions()
        # tws.reqPnL(17001, tws.account, "")

if __name__=="__main__":
    print("auto run")
    TWS.tws.run()