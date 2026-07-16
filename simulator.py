import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from backtesting.engine import load_data


def run_backtest(symbol="AAPL"):
    data = load_data(symbol)
    if data is None:
        return

    print(f"\nStarting backtest for {symbol}...")
    print("-" * 40)
    for index, row in data.iterrows():
        close_price = row['Close'] if isinstance(row['Close'], (int, float)) else row['Close'].iloc[0]
        print(f"{index.date()} | Close: {close_price:.2f}")
    print("-" * 40)
    print("Backtest complete.")


if __name__ == "__main__":
    run_backtest()
