import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from account.virtual_account import get_balance

MIN_SCORE = 70
MAX_OPEN_POSITIONS = 1


def check_trade_allowed(trade, open_positions):
    if not trade:
        print("❌ No trade provided.")
        return False

    symbol = trade["symbol"]
    score = trade["score"]

    print("\n🛡️ Trade Guard Check")

    if score < MIN_SCORE:
        print(f"❌ Score too low: {score}")
        return False
    print(f"✅ Score approved: {score}")

    if len(open_positions) >= MAX_OPEN_POSITIONS:
        print("❌ Maximum positions reached.")
        return False
    print("✅ Position limit OK")

    existing_symbols = [p.symbol for p in open_positions]
    if symbol in existing_symbols:
        print("❌ Already holding this symbol.")
        return False
    print("✅ No duplicate position")

    balance = get_balance()
    if balance <= 0:
        print("❌ Account balance invalid.")
        return False
    print(f"✅ Account OK: £{balance}")

    print("🟢 Trade approved")
    return True


if __name__ == "__main__":
    test_trade = {"symbol": "AAPL", "score": 75}
    check_trade_allowed(test_trade, [])
