# Data engineering

```bash
.
├── app/
│   ├── binance_client.py     # Streams and processes Binance candles
│   ├── config.py             # Loads .env and config.toml settings
│   └── database.py           # Handles DB insertion logic
├── config/
│   └── config.toml           # Binance config (symbol, interval, etc.)
├── test/
│   └── notebook.ipynb        # Jupyter notebook for testing
├── main.py                   # Entry point to start streaming
├── .env.example              # Environment variable template
├── .gitignore
├── pyproject.toml            # Poetry project config
└── README.md                 # 📄 You're here!
```
