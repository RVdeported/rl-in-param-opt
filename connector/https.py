import websocket
import rel
import json
import multiprocessing
import threading
import asyncio
from db_connector import FinQuestDB
from datetime import datetime as dt
import logging
import requests
import time

class BinanceHTTPS:
    def __init__(self, symbols, interval_sec=20, depth=15):
        self.db         = FinQuestDB(symbols=symbols)
        self.symbols    = symbols
        self.logger = logging.Logger("main")
        fh = logging.FileHandler("./binance_https_logs.txt")
        self.logger.addHandler(fh)
        self.interval_sec=interval_sec
        self.depth=depth
        self.max_retry=5
        
    def record_data(self, data):
        self.db.insert(data)
        return 1
    
    def call(self, url):
        tryes = 0
        while tryes < self.max_retry:
            tryes += 1
            out = requests.get(url)
            if out.status_code != 200:
                self.logger.error(f"URL {url} returned non 200 code {out.status_code}")        
                continue
            return out.json()

        self.logger.error(f"Max retries achieved with {url} url")
        return None


    def start(self):
        while True:
            for symbol in self.symbols:
                url = f"https://api.binance.com/api/v3/depth?symbol={symbol.upper()}&limit={self.depth}"
                out = self.call(url)
                if out is not None:
                    out["e"] = "orderBook"
                    out["s"] = symbol
                    self.record_data([out])
            time.sleep(self.interval_sec)
            



if __name__ == "__main__":
    http = BinanceHTTPS(["btcusdt", "ethusdt"])
    http.start()
    
