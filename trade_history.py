import json
import os
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

HISTORY_FILE = ROOT / "trade_history.json"


def load_history():
    if not HISTORY_FILE.exists():
        return []
    with HISTORY_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_history(history):
    with HISTORY_FILE.open("w", encoding="utf-8") as file:
        json.dump(history, file, indent=4)


def record_trade(symbol, entry, exit_price, shares, score):
    history = load_history()
    pnl = (exit_price - entry) * shares
    trade = {
        "date": str(datetime.now()),
        "symbol": symbol,
        "entry": entry,
        "exit": exit_price,
        "shares": shares,
        "score": score,
        "pnl": pnl,
        "result": "WIN" if pnl > 0 else "LOSS",
    }
    history.append(trade)
    save_history(history)
    print("Trade recorded:")
    print(trade)


if __name__ == "__main__":
    record_trade("AAPL", 100, 104, 2, 75)
