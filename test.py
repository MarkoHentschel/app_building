
from src.pull_stock_details import pull_stock_details
from config.config import load_env

etf_ticker = 'H4ZX.DE'

stock_data = pull_stock_details(etf_ticker)
trail_peg = stock_data[stock_data["attribute"]=="trailingPegRatio"].reset_index()
trail_pe = stock_data[stock_data["attribute"]=="trailingPE"].reset_index()
trail_eps = stock_data[stock_data["attribute"]=="trailingEps"].reset_index()
avg_analyst_rating = stock_data[stock_data["attribute"]=="averageAnalystRating"].reset_index()


print(avg_analyst_rating)

#peg <1 = undervalued
# recommandation 1=Strong Buy,2=Buy,3=Hold,4=Underperform, 5=sell