import ccxt
import pandas as pd
from config import API_KEY, SECRET, PASSWORD, TIMEFRAME

exchange = ccxt.okx({
    "apiKey": API_KEY,
    "secret": SECRET,
    "password": PASSWORD,
    "password": PASSWORD,
    "enableRateLimit": True,
})

def get_ohlcv(symbol, limit=300):
    candles = exchange.fetch_ohlcv(
        symbol,
        timeframe=TIMEFRAME,
        limit=limit
    )

    df = pd.DataFrame(
        candles,
        columns=[
            "timestamp",
            "open",
            "high",
            "low",
            "close",
            "volume"
        ]
    )

    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")

    df["open"] = df["open"].astype(float)
    df["high"] = df["high"].astype(float)
    df["low"] = df["low"].astype(float)
    df["close"] = df["close"].astype(float)
    df["volume"] = df["volume"].astype(float)

    return df
