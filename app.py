from src.calc_metrics import calc_metric
from src.pull_stock_details import pull_stock_details
from config.config import load_env

etf_ticker = 'H4ZX.DE'

def main(etf_ticker):
    load_env()
    stock_data = pull_stock_details(etf_ticker)
    return stock_data

if __name__ == "__main__":
    print(main(etf_ticker))

