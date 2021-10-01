import multiprocessing as mp
import threading as td
from IB_main import TWS
from ws_service import WS


def IB():
    ib = TWS()
    td_IB = td.Thread(target=ib.ib.run)
    td_IB.start()
    td_IB.join(3)

if __name__=="__main__":
    q = mp.SimpleQueue()
    p_IB = mp.Process(target=IB)
    websocketProcess = mp.Process(target=WS.run, name="websocket")
    p_IB.start()
    websocketProcess.start()

