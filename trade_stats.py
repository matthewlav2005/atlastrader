import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

JOURNAL_FILE = ROOT / "trade_journal.json"


def load_trades():
    if not JOURNAL_FILE.exists():
        return []
    with JOURNAL_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def calculate_stats():
    trades = load_trades()
    if not trades:
        print("No trades available.")
        return

    total = len(trades)
    wins = 0
    losses = 0
    total_profit = 0
    total_loss = 0

    for trade in trades:
        pnl = trade.get("pnl", 0)
        if pnl > 0:
            wins += 1
            total_profit += pnl
        elif pnl < 0:
            losses += 1
            total_loss += abs(pnl)

    win_rate = wins / total * 100

    print("====================")
    print("ATLAS TRADE REPORT")
    print("====================")
    print(f"Total Trades: {total}")
    print(f"Wins: {wins}")
    print(f"Losses: {losses}")
    print(f"Win Rate: {win_rate:.1f}%")

    if losses > 0:
        profit_factor = total_profit / total_loss
        print(f"Profit Factor: {profit_factor:.2f}")

    print("====================")


if __name__ == "__main__":
    calculate_stats()
