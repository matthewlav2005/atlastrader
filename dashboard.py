import streamlit as st
import json
from pathlib import Path

st.set_page_config(page_title="Atlas Trader Dashboard", layout="wide")
st.title("🤖 Atlas Trader Dashboard")

ROOT = Path(__file__).resolve().parent

# Sidebar
with st.sidebar:
    st.header("Navigation")
    page = st.radio("Select Page", ["Overview", "Positions", "Performance", "Settings"])

# Load data functions
def load_account():
    try:
        from account.virtual_account import get_balance, load_account as load_acc
        balance = get_balance()
        account = load_acc()
        return balance, account
    except:
        return None, None

def load_trades():
    trade_file = ROOT / "trade_history.json"
    if trade_file.exists():
        with open(trade_file, "r") as f:
            return json.load(f)
    return []

if page == "Overview":
    st.header("Account Overview")
    balance, account = load_account()
    if balance:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Balance", f"£{balance:.2f}")
        with col2:
            st.metric("Daily P/L", f"£{account.get('daily_profit_loss', 0):.2f}")
        with col3:
            st.metric("Total Trades", account.get('total_trades', 0))

elif page == "Positions":
    st.header("Open Positions")
    try:
        from alpaca.trading.client import TradingClient
        import os
        from dotenv import load_dotenv
        load_dotenv()
        client = TradingClient(os.getenv("ALPACA_API_KEY"), os.getenv("ALPACA_SECRET_KEY"), paper=True)
        positions = client.get_all_positions()
        if positions:
            for pos in positions:
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.write(f"**{pos.symbol}**")
                with col2:
                    st.write(f"Entry: ${float(pos.avg_entry_price):.2f}")
                with col3:
                    st.write(f"Current: ${float(pos.current_price):.2f}")
                with col4:
                    pnl_pct = ((float(pos.current_price) - float(pos.avg_entry_price)) / float(pos.avg_entry_price)) * 100
                    st.write(f"P/L: {pnl_pct:.2f}%")
        else:
            st.info("No open positions")
    except Exception as e:
        st.error(f"Error loading positions: {e}")

elif page == "Performance":
    st.header("Trade Performance")
    trades = load_trades()
    if trades:
        st.write(f"Total Trades: {len(trades)}")
        wins = sum(1 for t in trades if t.get('result') == 'WIN')
        st.write(f"Win Rate: {wins/len(trades)*100:.1f}%")
        st.dataframe([{k: v for k, v in t.items() if k != 'date'} for t in trades[-10:]])
    else:
        st.info("No trades recorded yet")

elif page == "Settings":
    st.header("Settings")
    st.write("Configure Atlas Trader settings here")
    min_score = st.slider("Minimum Score", 0, 100, 70)
    max_positions = st.slider("Max Open Positions", 1, 10, 1)
    if st.button("Save Settings"):
        st.success("Settings saved!")

st.divider()
st.info("Atlas Trader Dashboard - Real-time trading insights")
