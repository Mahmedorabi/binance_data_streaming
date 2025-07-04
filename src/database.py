import asyncpg
from dotenv import load_dotenv
import uuid
from src import config
from src.data_validation import DataValidation

load_dotenv()


async def insert_candle(market_data: DataValidation):
    conn = await asyncpg.connect(
        host=config.DATABASE_HOST,
        port=config.DATABASE_PORT,
        database=config.DATABASE_NAME,
        user=config.DATABASE_USER,
        password=config.DATABASE_PASSWORD,
    )
    await conn.execute(
        """
        INSERT INTO ohlcv(id, timestamp, open, high, low, close, volume)
        VALUES($1, $2, $3, $4, $5, $6, $7)
        """,
        uuid.uuid4(),
        market_data.t,
        market_data.o,
        market_data.h,
        market_data.l,
        market_data.c,
        market_data.v,
    )
    await conn.close()
