import json
import os
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ACCOUNT_FILE = ROOT / "virtual_account.json"

DEFAULT_ACCOUNT = {
    "starting_balance": 1000,
    "balance": 1000,
    "daily_profit_loss": 0,
    "total_trades": 0,
    "winning_trades": 0,
    "losing_trades": 0,
    "last_reset": str(datetime.now().date()),
}


def load_account():
    if not ACCOUNT_FILE.exists():
        save_account(DEFAULT_ACCOUNT)
        return DEFAULT_ACCOUNT

    with ACCOUNT_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_account(account):
    with ACCOUNT_FILE.open("w", encoding="utf-8") as file:
        json.dump(account, file, indent=4)


def get_balance():
    account = load_account()
    return account["balance"]


def show_account():
    account = load_account()
    print(
        f"""
ATLAS VIRTUAL ACCOUNT
---------------------
Balance: £{account['balance']:.2f}
Trades: {account['total_trades']}
Daily P/L: £{account['daily_profit_loss']:.2f}
"""
    )


if __name__ == "__main__":
    show_account()
