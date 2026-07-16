import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scanner.risk.reports.performance import calculate_performance


if __name__ == "__main__":
    calculate_performance()
