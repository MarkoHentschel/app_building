
from src.pull_stock_details import pull_stock_details
from config.config import load_env
import pandas as pd
from scipy.stats import rankdata

etf_ticker = 'EUNL.DE'

# pull analytic measures and the fund weight of the top etf holdings
stock_data = pull_stock_details(etf_ticker)[0]
df_weight = pull_stock_details(etf_ticker)[1]


# Add the "fund" column and calculated strockprice potential (as the difference between target and current stock price)
stock_data['fund'] = etf_ticker
stock_data['stockprice_potential'] = (stock_data['targetMedianPrice'].fillna(0) -
                       stock_data['previousClose'].fillna(0))

# Define which stock features are "lower is better" and which are "higher is better" to base the overall score on
lower_is_better = ['recommendationMean', 'trailingPegRatio', 'trailingPE']
higher_is_better = ['quickRatio', 'trailingEps', 'revenuePerShare', 'stockprice_potential','profitMargins']

# Normalize all features using percentile ranking
from scipy.stats import rankdata

for col in lower_is_better + higher_is_better:
    if col in lower_is_better:
        stock_data[col + '_norm'] = 1 - (rankdata(stock_data[col]) / len(stock_data))
    else:
        stock_data[col + '_norm'] = rankdata(stock_data[col]) / len(stock_data)

# Combine into a single composite score (pre-defined weighting of the metrics -> tbd if plausible)
norm_cols = [col + '_norm' for col in lower_is_better + higher_is_better]
#print(norm_cols)

weights = {
    'recommendationMean_norm': 0.2,
    'trailingPegRatio_norm': 0.2,
    'trailingPE_norm': 0.1,
    'quickRatio_norm': 0.15,
    'trailingEps_norm': 0.15,
    'revenuePerShare_norm': 0.1,
    'stockprice_potential_norm': 0.05,
    'profitMargins_norm': 0.05
}

stock_data['composite_score'] = sum(
    stock_data[col] * weights.get(col, 1/len(weights)) for col in norm_cols
)

# to skip NaN missing values
stock_data['composite_score'] = stock_data[norm_cols].mean(axis=1, skipna=True)

# to replace missing data with defined value (e.g 0.5)
#stock_data[norm_cols] = stock_data[norm_cols].fillna(0.5)


# Sort by score if desired
stock_score_sorted = stock_data.sort_values('composite_score', ascending=False)

# 1. Merge by ticker
merged = pd.merge(stock_data,df_weight, left_on='ticker', right_on='Symbol', how='inner')

# 2. Normalize weights (optional but recommended)
merged['weight'] = merged['Holding Percent'] / merged['Holding Percent'].sum()

# 3. Compute weighted score
overall_score = (merged['composite_score'] * merged['weight']).sum()


print(stock_score_sorted[['longName','composite_score']]) # individuell holding scores of the fund
print(overall_score) # overall score of the ETF based on its top holdings