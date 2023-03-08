import websockets
import json
import time

async def get_spot_rates():
    url = "wss://stream.binance.com:9443/stream?streams=btcusdt@miniTicker"
    async with websockets.connect(url) as client:
        while True:
            data = json.loads(await client.recv())['data']
            return(data['c'])



