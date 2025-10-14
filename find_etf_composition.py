#pull top 20 stock symbols of input etf
#https://www.justetf.com/de/etf-profile.html?isin=IE00B3XXRP09
#https://www.justetf.com/de/etf-profile.html?isin=IE00B3XXRP09#zusammensetzung

import yfinance as yf
import pandas as pd

etf_symbol = 'H4ZX.DE'
spy = yf.Ticker(etf_symbol).funds_data
df_top = pd.DataFrame(spy.top_holdings)
print(df_top)