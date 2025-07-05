import asyncio
from src.binance_client import stream_data


if __name__ == "__main__":
    asyncio.run(stream_data())