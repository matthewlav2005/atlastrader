from account.virtual_account import show_account, get_balance

from risk.daily_limits import check_daily_loss

from monitoring.position_monitor import check_positions

from reports.performance import calculate_performance

from scanner.session import market_is_open

from scanner.scanner import run_scanner


def run_atlas():

    print(
        """
========================
🤖 ATLAS TRADER ONLINE
========================
"""
    )


    # 1. Market session check

    print("Checking market session...")

    if not market_is_open():

        print(
            "⛔ Market closed. Atlas stopping."
        )

        return

    print(
        "✅ Market open"
    )


    # 2. Account status

    print("\nAccount status:")

    show_account()


    # 3. Daily risk protection

    print(
        "\nChecking daily limits..."
    )

    balance = get_balance()

    allowed = check_daily_loss(
        1000,
        balance
    )


    if not allowed:

        print(
            "🚫 Trading disabled."
        )

        return


    # 4. Monitor positions

    print(
        "\nChecking positions..."
    )

    check_positions()


    # 5. Scan markets

    print(
        "\nScanning markets..."
    )

    print("SCANNER STARTED")
    opportunities = run_scanner()
    print("SCANNER FINISHED")
    print("DEBUG SCANNER RETURN:")
    print(opportunities)

    if not opportunities:
        print(
            "\nNo qualifying setups found."
        )
    else:
        print(
            "\nOpportunities detected:"
        )

        for trade in opportunities:
            print(trade)


    # 6. Performance

    print(
        "\nPerformance:"
    )

    calculate_performance()


    print(
        """
========================
Atlas cycle complete
========================
"""
    )


if __name__ == "__main__":

    run_atlas()