import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mplfinance as mpf
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# -----------------------------
# Basic Settings
# -----------------------------

# -----------------------------
# Load Data
# -----------------------------
df = pd.read_csv("../data/raw/reliance_stock_data.csv", parse_dates=["Date"])
df = df.sort_values("Date").set_index("Date")
df.columns = df.columns.str.replace(" ", "_")


# -----------------------------
# 1. Closing Price Trend
# -----------------------------
def plot_closing_price(df):
    plt.figure()
    plt.plot(df.index, df["Close_values"])
    plt.title("Closing Price Over Time")
    plt.xticks(rotation=45)
    plt.show()


# -----------------------------
# 2. High vs Low Price
# -----------------------------
def plot_high_low(df):
    plt.figure()
    plt.plot(df.index, df["High_values"], label="High")
    plt.plot(df.index, df["Low_values"], label="Low")
    plt.legend()
    plt.title("High vs Low Price")
    plt.xticks(rotation=45)
    plt.show()


# -----------------------------
# 3. Trading Volume
# -----------------------------
def plot_volume(df):
    plt.figure()
    plt.bar(df.index, df["Volume_values"])
    plt.title("Trading Volume")
    plt.xticks(rotation=45)
    plt.show()


# -----------------------------
# 4 & 5. Moving Averages (20 & 50)
# -----------------------------
def plot_moving_average(df, window):
    ma = df["Close_values"].rolling(window).mean()
    plt.figure()
    plt.plot(df.index, df["Close_values"], label="Close")
    plt.plot(df.index, ma, label=f"{window}-Day MA")
    plt.legend()
    plt.title(f"{window}-Day Moving Average")
    plt.xticks(rotation=45)
    plt.show()


# -----------------------------
# 6. Daily Returns Distribution
# -----------------------------
def plot_returns_distribution(df):
    returns = df["Close_values"].pct_change()
    plt.figure()
    sns.histplot(returns.dropna(), bins=50, kde=True)
    plt.title("Daily Returns Distribution")
    plt.show()


# -----------------------------
# 7. Price Distribution
# -----------------------------
def plot_price_distribution(df):
    plt.figure()
    sns.histplot(df["Close_values"], bins=50, kde=True)
    plt.title("Closing Price Distribution")
    plt.show()


# -----------------------------
# 8. Correlation Heatmap
# -----------------------------
def plot_correlation(df):
    plt.figure(figsize=(8, 6))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.show()


# -----------------------------
# 9. Rolling Volatility
# -----------------------------
def plot_volatility(df, window=20):
    volatility = df["Close_values"].rolling(window).std()
    plt.figure()
    plt.plot(df.index, volatility)
    plt.title(f"{window}-Day Rolling Volatility")
    plt.xticks(rotation=45)
    plt.show()


# -----------------------------
# 10. Candlestick Chart
# -----------------------------
def plot_candlestick(df):
    mpf.plot(df, type="candle", style="charles", title="Candlestick Chart", volume=True)


# -----------------------------
# Run All Plots
# -----------------------------
plot_closing_price(df)
plot_high_low(df)
plot_volume(df)
plot_moving_average(df, 20)
plot_moving_average(df, 50)
plot_returns_distribution(df)
plot_price_distribution(df)
plot_correlation(df)
plot_volatility(df, 20)
plot_candlestick(df)
