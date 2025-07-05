from fastapi import FastAPI
import uvicorn
import asyncio
from src.binance_client import stream_data

app = FastAPI()

@app.get("/health")
async def health():
    return {"status": "ok"}

async def run_streamer():
    await stream_data()

if __name__ == "__main__":
    # start data streamer in the background
    asyncio.create_task(run_streamer())
    # run HTTP server
    uvicorn.run(app, host="0.0.0.0", port=8000)
