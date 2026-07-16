import os
import pandas as pd
from dotenv import load_dotenv

try:
    from .market_data import (
        calculate_vwap,
        calculate_relative_volume,
    )
except ImportError:
    from market_data import (
        calculate_vwap,
        calculate_relative_volume,
    )

from strategy.scoring import calculate_atlas_score

from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame, TimeFrameUnit

try:
    from .indicators import add_indicators
except ImportError:
    from indicators import add_indicators


load_dotenv()

API_KEY = os.getenv("ALPACA_API_KEY")
SECRET_KEY = os.getenv("ALPACA_SECRET_KEY")


data_client = StockHistoricalDataClient(
    API_KEY,
    SECRET_KEY,
)


symbols = [
    "AAPL",
    "MSFT",
    "NVDA",
    "TSLA",
    "AMZN",
    "META",
    "AMD",
    "GOOGL",
]


def calculate_score(data):
    return calculate_atlas_score(data)


def scan_market():
    print("\n📈 ATLAS SCANNER")
    print("----------------")

    opportunities = []

    for symbol in symbols:
        try:
            request = StockBarsRequest(
                symbol_or_symbols=[symbol],
                timeframe=TimeFrame(5, TimeFrameUnit.Minute),
                limit=100,
            )
            bars = data_client.get_stock_bars(request)
            stock_data = bars.df

            if stock_data.empty:
                print(f"{symbol}: no data returned")
                continue

            if isinstance(stock_data.index, pd.MultiIndex):
                if symbol in stock_data.index.get_level_values("symbol"):
                    stock_data = stock_data.xs(symbol, level="symbol")
                else:
                    print(f"{symbol}: no data returned")
                    continue

            stock_data = add_indicators(stock_data)
            stock_data["vwap"] = calculate_vwap(stock_data)
            stock_data["rvol"] = calculate_relative_volume(stock_data)

            score = calculate_score(stock_data)
            latest = stock_data.iloc[-1]

            print(
                f"""
{symbol}
Score: {score}/100
Price: ${latest['close']:.2f}
RSI: {latest['rsi']:.1f}
"""
            )

            if score >= 70:
                opportunities.append(
                    {
                        "symbol": symbol,
                        "score": score,
                        "price": latest['close'],
                    }
                )

        except Exception as e:
            print(f"{symbol}: Error {e}")

    return opportunities


def run_scanner():
    return scan_market()


if __name__ == "__main__":
    run_scanner()