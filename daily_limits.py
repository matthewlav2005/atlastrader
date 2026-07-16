import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scanner.risk.risk.daily_limits import check_daily_loss


if __name__ == "__main__":
    check_daily_loss(1000, 985)
