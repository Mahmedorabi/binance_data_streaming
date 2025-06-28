import json
from app import config
import websockets
from app.database import insert_candle

symbol = config.BINANCE_SYMBOL.lower()
interval = config.BINANCE_INTERVAL
streming_url = f"wss://stream.binance.com:9443/ws/{symbol}@kline_{interval}"

async def stream_data():
    async with websockets.connect(streming_url, ping_interval=20) as ws:
        async for message in ws:
            data = json.loads(message)
            kline = data["k"]
            if kline["x"]: 
                candle = {
                    "t": kline["t"],
                    "o": float(kline["o"]),
                    "h": float(kline["h"]),
                    "l": float(kline["l"]),
                    "c": float(kline["c"]),
                    "v": float(kline["v"])
                }
                await insert_candle(candle)
                print("Saved candle:", candle)

