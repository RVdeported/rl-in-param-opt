import websocket
import _thread
import time
import rel
import json
import multiprocessing
import threading
import asyncio
from db_connector import FinQuestDB
from datetime import datetime as dt
import logging

class BinanceWSS:
    def __init__(self, params, batch_size=10):
        self.db         = FinQuestDB(symbols=set([n.split("@")[0] for n in params]))
        self.params     = params
        self.batch_size = batch_size
        self.buffer     = {}
        self.logger = logging.Logger("main")
        fh = logging.FileHandler("./binance_wss_logs.txt")
        self.logger.addHandler(fh)

    def on_message(self, ws, message):
        t = threading.Thread(
            target=asyncio.run, 
            args=[self.write_message(message)])
        t.start()

    async def write_message(self, message):
        self.logger.info(message)
    async def write_error(self, message):
        self.logger.error(message)
            
    def on_error(self, ws, error):
        t = threading.Thread(
            target=asyncio.run, 
            args=[self.write_error(error)])
        t.start()

    def on_close(self, ws, close_status_code, close_msg):
        # JOIN ALL CHILDREN!
        print("### closed ###")

    def on_open(self, ws):
        print("Opened connection")
        
    def on_data(self, ws, message, opcode_text, opcode_binary):
        message = json.loads(message)
        key = message["s"] + "@" + message["e"]
        if key not in self.buffer.keys():
            self.buffer[key] = []

        self.buffer[key].append(message)
        if len(self.buffer[key]) < self.batch_size:
            return
        print("recording " + key)
        t = multiprocessing.Process(target=asyncio.run, args=[self.record_data(self.buffer[key])])
        t.start()
        self.buffer[key] = []
        
    async def record_data(self, data):
        self.db.insert(data)
        return 1
    
    def start(self):

        websocket.enableTrace(True)
        ws = websocket.WebSocketApp("wss://data-stream.binance.vision/ws/BUSDT@trade",
                                on_open=self.on_open,
                                on_message=self.on_message,
                                on_error=self.on_error,
                                on_close=self.on_close,
                                on_data=self.on_data
                                )


        ws.run_forever(dispatcher=rel, reconnect=5)  # Set dispatcher to automatic reconnection, 5 second reconnect delay if connection closed unexpectedly
        ws.send(json.dumps({
            "method": "SUBSCRIBE",
            "params": self.params,
            "id": 1
            }))
        # res = ws.recv()
        # print(json.loads(res))
        
        rel.signal(2, rel.abort)  # Keyboard Interrupt
        rel.dispatch()

if __name__ == "__main__":
    wss = BinanceWSS(["btcusdt@kline_1s","btcusdt@depth@100ms"], batch_size=10)
    wss.start()

