#calculate evaluation of overall risk/performance/value of etf based on red and green flagging the underlying stock metrics 
# from the pull_stock_details
from src.calc_metrics import calc_metric
from src.pull_stock_details import pull_stock_details
from config.config import load_env

etf_ticker = 'H4ZX.DE'

stock_data = pull_stock_details(etf_ticker)

print(stock_data.head())
