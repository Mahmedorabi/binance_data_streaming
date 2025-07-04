import json
from src import config
import websockets
from src.database import insert_candle
from src.data_validation import DataValidation
from src.logger_print import get_logger

logger = get_logger(__name__)
symbol = config.BINANCE_SYMBOL.lower()
interval = config.BINANCE_INTERVAL
streaming_url = config.BINANCE_URL


async def stream_data():
    async with websockets.connect(streaming_url, ping_interval=20) as ws:
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
                    "v": float(kline["v"]),
                }
                try:
                    candle_schema = DataValidation(**candle)
                    await insert_candle(candle_schema)
                    logger.info(f"Saved candle: {candle_schema}")
                except Exception as e:
                    logger.warning(f"Invalid candle: {e}")
