import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Settings
sns.set(style="darkgrid")
plt.rcParams["figure.figsize"] = (14, 6)

# Load Data
df = pd.read_csv("../data/raw/reliance_stock_data.csv")
df.columns = [col.replace(" ", "_") for col in df.columns]

# Set Date as index ONCE
df.sort_values("Date", inplace=True)
df.set_index("Date", inplace=True)

# Basic EDA
print(df.head())
print(df.info())
print(df.describe())
print("\nMissing values:\n", df.isnull().sum())
# Plot Closing Price