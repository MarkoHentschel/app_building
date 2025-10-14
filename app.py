import yfinance as yf
import pandas as pd

def pull_top_holdings(etf_symbol):

    spy = yf.Ticker(etf_symbol).funds_data
    df_top = pd.DataFrame(spy.top_holdings)
    df_top = df_top.reset_index()
    my_list = df_top.iloc[:, 0].tolist() 
    return my_list,df_top

etf_symbol = 'H4ZX.DE'
#print(pull_top_holdings(etf_symbol))


ticker = yf.Ticker('01211')
ticker = ticker.info
df = pd.DataFrame([ticker])
if df.iloc[:, 0].isna().any():
    return None
else:
    print(df)
