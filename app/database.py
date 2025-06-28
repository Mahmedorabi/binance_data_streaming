import os
import asyncpg
from dotenv import load_dotenv
import uuid
from app import config

load_dotenv()

async def insert_candle(candle):
    conn = await asyncpg.connect(
        host=config.DATABASE_HOST,
        port=config.DATABASE_PORT,
        database=config.DATABASE_NAME,
        user=config.DATABASE_USER,
        password=config.DATABASE_PASSWORD
    )
    await conn.execute(
        """
        INSERT INTO ohlcv(id, timestamp, open, high, low, close, volume)
        VALUES($1, $2, $3, $4, $5, $6, $7)
        """,
        uuid.uuid4(),
        candle["t"], candle["o"], candle["h"],
        candle["l"], candle["c"], candle["v"]
    )
    await conn.close()
