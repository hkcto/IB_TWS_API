import time
import threading
from ib_class import IB_App

IB_CONFIG = {"host": "192.168.1.158", "port": 7497, "clientId": 0}
tws = IB_App()

def tws_main():

    tws.connect(**IB_CONFIG)
    
    tws.reqPositions()
    tws.reqPnL(17001, tws.account, "")
    tws.run()


#     # app.run()


if __name__=="__main__":
    thread_tws = threading.Thread(target=tws_main)
    thread_tws.start()
    time.sleep(5)

