import os
import tomllib
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parents[1]

# LOAD environment variables
BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_PORT = os.getenv("DATABASE_PORT")

# LOAD config file
config_path = BASE_DIR / "config" / "config.toml"

with open(config_path, "rb") as f:
    cfg = tomllib.load(f)["binance"]

# Configurations
BINANCE_SYMBOL = cfg["symbol"]
BINANCE_INTERVAL = cfg["interval"]
BINANCE_LIMIT = cfg["limit"]
BINANCE_URL = cfg["stream_url"].format(
    symbol=BINANCE_SYMBOL.lower(), interval=BINANCE_INTERVAL
)
