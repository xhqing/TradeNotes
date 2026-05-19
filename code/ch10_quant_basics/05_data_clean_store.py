# Copyright (c) 2026 TradeNote Authors
# Licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0).
# See LICENSE.txt for the full license text.

import pandas as pd
import numpy as np
import sqlite3
import os

os.makedirs('output', exist_ok=True)

np.random.seed(42)
dates = pd.date_range('2023-01-01', periods=200)
prices = 100 + np.cumsum(np.random.randn(200) * 0.5)
df = pd.DataFrame({
    'close': prices,
    'volume': np.random.randint(100000, 500000, 200)
}, index=dates)
df.index.name = 'date'

df.dropna(inplace=True)
df = df[df['volume'] > 0]

df.to_parquet('output/clean_data.parquet')
print("Parquet saved.")

conn = sqlite3.connect('output/trading.db')
df.to_sql('daily_prices', conn, if_exists='replace')
print("SQLite saved.")

df_loaded = pd.read_parquet('output/clean_data.parquet')
print(f"Loaded from Parquet: {len(df_loaded)} rows")

df_sql = pd.read_sql('SELECT * FROM daily_prices LIMIT 5', conn)
print(df_sql)

conn.close()
