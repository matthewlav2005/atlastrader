def select_best_trade(opportunities):
    if not opportunities:
        print("No trade opportunities.")
        return None

    best_trade = max(opportunities, key=lambda x: x["score"])
    print("\nBest setup selected:")
    print(best_trade)
    return best_trade


if __name__ == "__main__":
    test_trades = [
        {"symbol": "AAPL", "score": 75},
        {"symbol": "AMZN", "score": 68},
    ]
    select_best_trade(test_trades)
