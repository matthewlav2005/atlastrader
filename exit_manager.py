def check_exit(symbol, entry_price, current_price, stop_loss, target_price):
    print(f"\nChecking {symbol} exit...")

    if current_price <= stop_loss:
        print(f"🛑 Stop loss hit for {symbol}")
        return "SELL"

    if current_price >= target_price:
        print(f"🎯 Target reached for {symbol}")
        return "SELL"

    print(f"✅ Holding {symbol}")
    return "HOLD"


if __name__ == "__main__":
    result = check_exit("AAPL", 100, 104, 98, 104)
    print("Action:", result)
