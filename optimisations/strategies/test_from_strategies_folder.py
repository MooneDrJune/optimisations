import sys
from pathlib import Path

file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))


from strategy import strategy
from backtest import backtest
from utilities.utility import now

print(now)
print(strategy)
print(backtest)
