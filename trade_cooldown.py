import json
import os
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

COOLDOWN_FILE = ROOT / "trade_cooldown.json"


def load_history():
    if not COOLDOWN_FILE.exists():
        return {}
    with COOLDOWN_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_history(history):
    with COOLDOWN_FILE.open("w", encoding="utf-8") as file:
        json.dump(history, file, indent=4)


def can_trade_symbol(symbol):
    history = load_history()
    today = str(datetime.now().date())

    if symbol in history and history[symbol] == today:
        print(f"❌ {symbol} already traded today.")
        return False

    print(f"✅ {symbol} cooldown clear.")
    return True


def record_trade(symbol):
    history = load_history()
    history[symbol] = str(datetime.now().date())
    save_history(history)


if __name__ == "__main__":
    test_symbol = "AAPL"
    if can_trade_symbol(test_symbol):
        print("Recording test trade...")
        record_trade(test_symbol)
