import yfinance as yf


def load_data(symbol, period="6mo", interval="1d"):
    print(f"Loading {symbol}...")
    data = yf.download(symbol, period=period, interval=interval, progress=False)
    if data.empty:
        print("No data found.")
        return None
    print(f"Loaded {len(data)} candles.")
    return data


if __name__ == "__main__":
    df = load_data("AAPL")
    if df is not None:
        print(df.tail())
