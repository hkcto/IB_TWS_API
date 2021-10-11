import asyncio
import websockets
from queue import Queue
import json

with open("templates/positions.json", "r", encoding="utf-8") as f:
    data:str = f.read()

class WS:

    def __init__(self, queue) -> None:
        self.queue: Queue = queue

    async def positions(self, ws: websockets, path):
        msg = await ws.recv()
        await ws.send(data)
        # print(data)
        while True:

            if not self.queue.empty():
                await ws.send(json.dumps(self.queue.get()))
            else:
                await asyncio.sleep(2)
                # print("sleep: 1S")

        # if msg == "positions":
        #     # await ws.send(json.dumps(data).encode("utf-8"))
        #     await ws.send(data)

        # while True:
        #     if not self.queue.empty():
        #         response = self.queue.get()
        #         await ws.send(str(response))

    async def main(self):
        async with websockets.serve(self.positions, "localhost", 8765):
            await asyncio.Future()  # run forever

    def run(self):
        print("WebSocket Service Running")
        asyncio.run(self.main())

if __name__=="__main__":
    priceList = [
        {'price': [{'reqId': 1000, 'localsymbol': 'QQQ   211011C00364000', 'tickType': 1, 'price': -1.0}]},
        {'price': [{'reqId': 1000, 'localsymbol': 'QQQ   211011C00364000', 'tickType': 2, 'price': -1.0}]},
        {'price': [{'reqId': 1000, 'localsymbol': 'QQQ   211011C00364000', 'tickType': 9, 'price': 0.5}]},
        {'price': [{'reqId': 1001, 'localsymbol': 'SPY   211029P00462500', 'tickType': 1, 'price': -1.0}]},
        {'price': [{'reqId': 1001, 'localsymbol': 'SPY   211029P00462500', 'tickType': 2, 'price': -1.0}]},
        {'price': [{'reqId': 1001, 'localsymbol': 'SPY   211029P00462500', 'tickType': 9, 'price': 24.85}]},
        {'price': [{'reqId': 1002, 'localsymbol': 'QQQ   211015C00363000', 'tickType': 1, 'price': -1.0}]},
        {'price': [{'reqId': 1002, 'localsymbol': 'QQQ   211015C00363000', 'tickType': 2, 'price': -1.0}]},
        {'price': [{'reqId': 1002, 'localsymbol': 'QQQ   211015C00363000', 'tickType': 9, 'price': 2.58}]},
        {'price': [{'reqId': 1003, 'localsymbol': 'QQQ   211029P00399000', 'tickType': 1, 'price': -1.0}]},
        {'price': [{'reqId': 1003, 'localsymbol': 'QQQ   211029P00399000', 'tickType': 2, 'price': -1.0}]},
        {'price': [{'reqId': 1003, 'localsymbol': 'QQQ   211029P00399000', 'tickType': 9, 'price': 38.03}]},
        {'price': [{'reqId': 1004, 'localsymbol': 'KO    220121C00052500', 'tickType': 1, 'price': -1.0}]},
        {'price': [{'reqId': 1004, 'localsymbol': 'KO    220121C00052500', 'tickType': 2, 'price': -1.0}]},
        {'price': [{'reqId': 1004, 'localsymbol': 'KO    220121C00052500', 'tickType': 9, 'price': 2.81}]},
        {'price': [{'reqId': 1005, 'localsymbol': 'XPEV  211022C00038000', 'tickType': 1, 'price': -1.0}]},
        {'price': [{'reqId': 1005, 'localsymbol': 'XPEV  211022C00038000', 'tickType': 2, 'price': -1.0}]},
        {'price': [{'reqId': 1005, 'localsymbol': 'XPEV  211022C00038000', 'tickType': 9, 'price': 1.46}]},
        {'price': [{'reqId': 1006, 'localsymbol': 'SPY   211011C00441000', 'tickType': 1, 'price': -1.0}]},
        {'price': [{'reqId': 1006, 'localsymbol': 'SPY   211011C00441000', 'tickType': 2, 'price': -1.0}]},
        {'price': [{'reqId': 1006, 'localsymbol': 'SPY   211011C00441000', 'tickType': 9, 'price': 0.41}]}]


    
    queue = Queue()
    for i in priceList:
        queue.put(i)
    WS(queue).run()

