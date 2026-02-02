import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Settings
sns.set(style="darkgrid")
plt.rcParams["figure.figsize"] = (14, 6)

# Load Data
current_folder = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_folder, "..", "data", "raw", "reliance_stock_data.csv")

df = pd.read_csv(csv_path, parse_dates=["Date"])
df.columns = [col.replace(" ", "_") for col in df.columns]

# Set Date as index ONCE
df.sort_values("Date", inplace=True)
df.set_index("Date", inplace=True)

# Basic EDA
print(df.head())
print(df.info())
print(df.describe())
print("\nMissing values:\n", df.isnull().sum())

# Closing Price Plot
plt.figure(figsize=(15, 6))

plt.plot(
    df.index, df["Close_values"], color="royalblue", linewidth=2, label="Closing Price"
)

plt.title("RELIANCE Closing Price Over Time", fontsize=14)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Price (INR)", fontsize=12)

plt.locator_params(axis="x", nbins=8)
plt.xticks(rotation=45)

plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()
