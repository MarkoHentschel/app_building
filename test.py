
from src.pull_stock_details import pull_stock_details
from config.config import load_env
import pandas as pd

etf_ticker = 'H4ZX.DE'

stock_data = pull_stock_details(etf_ticker)[0]
df_weight = pull_stock_details(etf_ticker)[1]

#trail_peg = stock_data[stock_data["attribute"]=="trailingPegRatio"].reset_index()


# Add the "fund" column with a fixed value "test"
stock_data['fund'] = etf_ticker

stock_data['stockprice_potential'] = (stock_data['targetMedianPrice'].fillna(0) -
                       stock_data['previousClose'].fillna(0))

# Let's assume df is your DataFrame with the 8 columns already present

# Define which features are "lower is better" and which are "higher is better"
lower_is_better = ['recommendationMean', 'trailingPegRatio', 'trailingPE']
higher_is_better = ['quickRatio', 'trailingEps', 'revenuePerShare', 'stockprice_potential','profitMargins']

# Normalize all features using min-max scaling
for col in lower_is_better:
    min_val, max_val = stock_data[col].min(), stock_data[col].max()
    stock_data[col + '_norm'] = 1 - (stock_data[col] - min_val) / (max_val - min_val)  # Invert
    stock_data[col + '_norm'] = stock_data[col + '_norm'].clip(0, 1)  # Optional: keep in bounds

for col in higher_is_better:
    min_val, max_val = stock_data[col].min(), stock_data[col].max()
    stock_data[col + '_norm'] = (stock_data[col] - min_val) / (max_val - min_val)
    stock_data[col + '_norm'] = stock_data[col + '_norm'].clip(0, 1)  # Optional: keep in bounds

# Combine into a single composite score (equal weighting)
norm_cols = [col + '_norm' for col in lower_is_better + higher_is_better]
stock_data['composite_score'] = stock_data[norm_cols].mean(axis=1)


# Sort by score if desired
df_sorted = stock_data.sort_values('composite_score', ascending=False)
# Example: add a weight column (replace with your real one)

# 1. Merge by ticker
merged = pd.merge(stock_data,df_weight, left_on='ticker', right_on='Symbol', how='inner')

# 2. Normalize weights (optional but recommended)
merged['weight'] = merged['Holding Percent'] / merged['Holding Percent'].sum()

# 3. Compute weighted score
overall_score = (merged['composite_score'] * merged['weight']).sum()


print(stock_data[['ticker','composite_score']]) # individuell holding scores of the fund
print(overall_score) # overall score of the ETF based on its top holdings