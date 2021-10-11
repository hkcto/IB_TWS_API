from ibapi.contract import Contract
from ib_class import IB_App
from threading import Thread
from ws_service import WS
import time
from queue import Queue
import pandas as pd

q = Queue()

ib = IB_App(q)
websocket = WS(q)


ib.connect("192.168.1.158", 7497, 0)

# 多進在這裡配置
ibTd = Thread(target=ib.run)
# wsTd = Thread(target=webstock.run)
ibTd.start()
ibTd.join(2)
ib.reqPositions()
time.sleep(2)


# for contract in ib.positions_opt_contractList:
#     contract: Contract
#     ib.reqMktData(ib.reqTable[contract.localSymbol], contract, "", False, False, [])
    

df: pd.DataFrame = ib.df
options = df[df["SecType"] == "OPT"]
options = options.to_dict("records")
for contract in options:
    ib.reqMktData(contract['ID'], contract['Contract'], "", False, False, [])

# while True:
#     if not q.empty():
#         print("q.get(): ", q.get())
#     else:
#         time.sleep(2)

websocket.run()