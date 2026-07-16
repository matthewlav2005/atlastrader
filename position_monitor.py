import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scanner.strategy.monitoring.position_monitor import check_positions


if __name__ == "__main__":
    check_positions()
