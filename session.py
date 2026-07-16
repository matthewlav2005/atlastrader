from datetime import datetime
import pytz
from pathlib import Path


def market_is_open():
    timezone = pytz.timezone("America/New_York")
    now = datetime.now(timezone)

    if now.weekday() > 4:
        return False

    market_open = now.replace(hour=9, minute=30, second=0, microsecond=0)
    market_close = now.replace(hour=16, minute=0, second=0, microsecond=0)

    return market_open <= now <= market_close


if __name__ == "__main__":
    if market_is_open():
        print("✅ Market session open")
    else:
        print("⛔ Market session closed")
