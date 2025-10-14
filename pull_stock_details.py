#pull detail performance metrics from the top 20 holdings of etf

import yfinance as yf
import pandas as pd

#https://finance.yahoo.com/quote/RHM.DE/key-statistics/

pd.set_option('display.max_rows', None)
ticker_var = 'RHM.DE' #todo:turn into list to loop through

def pull_stock_details(symbol):
    ticker = yf.Ticker(symbol)

    # Retrieve the info dictionary
    stock_details = pd.DataFrame([ticker.info])

    print(stock_details)

pull_stock_details(ticker_var) #todo: add loop
