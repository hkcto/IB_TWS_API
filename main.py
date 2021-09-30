import multiprocessing as mp
import threading as td
from IB_main import TWS


def IB(queue: mp.Queue):
    ib = TWS()
    td_IB = td.Thread(target=ib.ib.run)
    td_IB.start()
    td_IB.join(3)

if __name__=="__main__":
    q = mp.SimpleQueue()
    p_IB = mp.Process(target=IB, args=(q,))
    p_IB.start()
