#pull detail performance metrics from the top 10 holdings of etf

import yfinance as yf
import pandas as pd
import urllib.error


pd.set_option('display.max_rows', None)

def pull_top_holdings(etf_symbol):

    spy = yf.Ticker(etf_symbol).funds_data
    df_top = pd.DataFrame(spy.top_holdings)
    df_top = df_top.reset_index()
    my_list = df_top.iloc[:, 0].tolist() 
    return my_list


def pull_stock_details(symbol):

    ticker = yf.Ticker(symbol)
    stock_info = ticker.info
    df = pd.DataFrame([stock_info])
    if df.iloc[:, 0].isna().any():
        return None
    else:
        return df


def main():

    etf_symbol = 'H4ZX.DE'
    all_data = []

    symbol_list = pull_top_holdings(etf_symbol)

    for symbol in symbol_list:

        stock_data = pull_stock_details(symbol)

        if stock_data is not None:
            stock_data['Symbol'] = symbol 
            all_data.append((stock_data))

    df_data = pd.concat(all_data, ignore_index=True)
    return df_data

test = main()
print(test)
