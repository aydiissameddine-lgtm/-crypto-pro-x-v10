import time
import ccxt

from config import SYMBOLS, TIMEFRAME, CHECK_INTERVAL
from core.scanner import get_ohlcv
from core.strategy import analyze

print("=" * 60)
print("🚀 Crypto Pro X V10 Started")
print("=" * 60)

while True:

    try:

        for symbol in SYMBOLS:

            df = get_ohlcv(symbol)

            result = analyze(df)

            print(
                f"{symbol} | "
                f"{result['signal']} | "
                f"Confidence: {result['confidence']} | "
                f"BUY:{result['buy_score']} "
                f"SELL:{result['sell_score']}"
            )

        print("-" * 60)

        time.sleep(CHECK_INTERVAL)

    except Exception as e:

        print("ERROR:", e)

        time.sleep(10)
