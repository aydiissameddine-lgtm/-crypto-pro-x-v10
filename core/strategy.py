from core.indicators import add_indicators

def analyze(df):

    df = add_indicators(df)

    last = df.iloc[-1]

    buy_score = 0
    sell_score = 0

    reasons_buy = []
    reasons_sell = []

    # ==========================
    # EMA TREND
    # ==========================

    if last["EMA9"] > last["EMA21"]:
        buy_score += 15
        reasons_buy.append("EMA9 > EMA21")
    else:
        sell_score += 15
        reasons_sell.append("EMA9 < EMA21")

    if last["EMA21"] > last["EMA50"]:
        buy_score += 15
        reasons_buy.append("EMA21 > EMA50")
    else:
        sell_score += 15
        reasons_sell.append("EMA21 < EMA50")

    if last["EMA50"] > last["EMA200"]:
        buy_score += 20
        reasons_buy.append("EMA50 > EMA200")
    else:
        sell_score += 20
        reasons_sell.append("EMA50 < EMA200")

    # ==========================
    # RSI
    # ==========================

    rsi = last["RSI"]

    if rsi < 35:
        buy_score += 20
        reasons_buy.append("RSI Oversold")

    elif rsi > 65:
        sell_score += 20
        reasons_sell.append("RSI Overbought")

    # ==========================
    # MACD
    # ==========================

    if last["MACD"] > last["MACD_SIGNAL"]:
        buy_score += 20
        reasons_buy.append("MACD Bullish")

    else:
        sell_score += 20
        reasons_sell.append("MACD Bearish")

    # ==========================
    # ATR
    # ==========================

    if last["ATR"] > 0:
        buy_score += 5
        sell_score += 5

    # ==========================
    # FINAL DECISION
    # ==========================

    if buy_score > sell_score:

        signal = "BUY"
        confidence = buy_score
        reasons = reasons_buy

    elif sell_score > buy_score:

        signal = "SELL"
        confidence = sell_score
        reasons = reasons_sell

    else:

        signal = "WAIT"
        confidence = buy_score
        reasons = ["No clear signal"]

    return {
        "signal": signal,
        "confidence": confidence,
        "buy_score": buy_score,
        "sell_score": sell_score,
        "reasons": reasons
    }
