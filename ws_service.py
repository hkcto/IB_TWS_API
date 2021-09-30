import asyncio
import websockets

with open("templates/positions.json", "r", encoding="utf-8") as f:
    data = f.read()

class WS:


    def __init__(self) -> None:
        pass

    async def positions(self, ws: websockets, path):
        msg = await ws.recv()

        if msg == "positions":
            # await ws.send(json.dumps(data).encode("utf-8"))
            await ws.send(data)


    async def main(self):
        async with websockets.serve(self.positions, "localhost", 8765):
            await asyncio.Future()  # run forever

    def run(self):
        asyncio.run(self.main())

if __name__=="__main__":
    WS().run()

