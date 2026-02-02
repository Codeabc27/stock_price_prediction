import yfinance as yf
 

data = yf.download("RELIANCE.NS", start="2020-01-01", end="2025-01-01")

data.to_csv("data/raw/reliance_stock_data.csv")

