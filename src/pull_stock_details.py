#pull detail performance metrics from the top 10 holdings of etf

import yfinance as yf
import pandas as pd

pd.set_option('display.max_rows', None)

def pull_stock_details(etf_symbol):

    ticker_data={}

    spy = yf.Ticker(etf_symbol).funds_data
    df_top = pd.DataFrame(spy.top_holdings)
    df_top = df_top.reset_index()
    ticker_list = df_top.iloc[:, 0].tolist() 
    
    for ticker in ticker_list:
        ticker_object = yf.Ticker(ticker)
        df_temp = pd.DataFrame.from_dict(ticker_object.info, orient="index")
        df_temp.reset_index(inplace=True)
        df_temp.columns=["Attribute","current_value"]
        ticker_data[ticker] = df_temp

    combined_data = pd.concat(ticker_data)
    combined_data = combined_data.reset_index()
    del combined_data["level_1"]
    combined_data.columns=["ticker","attribute","current_value"]
    return combined_data
