import multiprocessing
from webs import BinanceWSS
from https import BinanceHTTPS
import asyncio

SYMBOLS = [
    "btcusdt@kline_1s", 
    "ethusdt@kline_1s", 
    "ethusdt@aggTrade", 
    "btcusdt@aggTrade",
    "btcusdt@orderBook", 
    "ethusdt@orderBook"
]

async def start(connector):
    connector.start()

if __name__ == "__main__":
    wss = BinanceWSS(
        [n for n in SYMBOLS if n.split("@")[1] != "orderBook"]
    )
    https = BinanceHTTPS(
        [n for n in SYMBOLS if n.split("@")[1] == "orderBook"]
    )
    
    t1 = multiprocessing.Process(target=asyncio.run, args=(start(wss),))
    t2 = multiprocessing.Process(target=asyncio.run, args=(start(https),))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    print("Processes joined successfully")