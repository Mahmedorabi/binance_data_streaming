from app.binance_client import stream_data
import asyncio

if __name__ == "__main__":
    asyncio.run(stream_data())