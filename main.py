import multiprocessing as mp
import threading as td

def IB(queue: mp.Queue):
    from IB_main import TWS
    ib = TWS()
    td_IB = td.Thread(target=ib.tws.run)
    td_IB.start()
    td_IB.join(3)
    queue.put(ib.tws.positions_options)

def webService():
    from web_server import WebService
    
    WebService.web.run()

if __name__=="__main__":
    q = mp.SimpleQueue()
    p_IB = mp.Process(target=IB, args=(q,))
    p_web = mp.Process(target=webService)
    p_IB.start()
    p_IB.join(3)
    p_web.start()
    p_web.join(3)
    message = q.get()
    print(message)