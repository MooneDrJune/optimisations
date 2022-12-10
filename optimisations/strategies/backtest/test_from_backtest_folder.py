import sys
from pathlib import Path

file = Path(__file__).resolve()
package_root_directory = file.parents[2]
sys.path.append(str(package_root_directory))

from strategies.strategy import strategy
from utilities.utility import now
from backtest import backtest

print(now)
print(strategy)
print(backtest)
