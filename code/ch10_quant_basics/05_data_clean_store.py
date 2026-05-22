# Copyright (c) 2026 TradeNote Authors
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import pandas as pd
import numpy as np
import sqlite3
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
OUTPUT_DIR = os.path.join(PROJECT_ROOT, 'output')
os.makedirs(OUTPUT_DIR, exist_ok=True)

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

df.to_parquet(os.path.join(OUTPUT_DIR, 'clean_data.parquet'))
print("Parquet saved.")

conn = sqlite3.connect(os.path.join(OUTPUT_DIR, 'trading.db'))
df.to_sql('daily_prices', conn, if_exists='replace')
print("SQLite saved.")

df_loaded = pd.read_parquet(os.path.join(OUTPUT_DIR, 'clean_data.parquet'))
print(f"Loaded from Parquet: {len(df_loaded)} rows")

df_sql = pd.read_sql('SELECT * FROM daily_prices LIMIT 5', conn)
print(df_sql)

conn.close()
