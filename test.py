
from src.pull_stock_details import pull_stock_details
from config.config import load_env
import pandas as pd

etf_ticker = 'H4ZX.DE'

# map peg ratio to valuation wording
def classify_value(x):
    if pd.isna(x):
        return "unknown" 
    elif x < 1:
        return "undervalued"
    elif 1 <= x < 1.01:
        return "fairly_valued"    
    else:
        return "overvalued"

stock_data = pull_stock_details(etf_ticker)

#trail_peg = stock_data[stock_data["attribute"]=="trailingPegRatio"].reset_index()


# Add the "fund" column with a fixed value "test"
stock_data['fund'] = etf_ticker

# Group by "fund" and calculate the mean of "current_value"
#rec_mean = rec_mean.groupby('fund')['current_value'].mean()
#recommendation = recommendation['current_value'].value_counts()


# Apply transformation
#trail_peg['valuation'] = trail_peg['current_value'].apply(classify_value)
#trail_peg = trail_peg['valuation'].value_counts()

print(stock_data.head())

