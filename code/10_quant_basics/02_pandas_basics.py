# Copyright (c) 2026 TradeNotes Authors
# Licensed under CC BY-NC-SA 4.0: https://creativecommons.org/licenses/by-nc-sa/4.0/

import pandas as pd
import numpy as np

np.random.seed(42)
dates = pd.date_range('2023-01-01', periods=200)
prices = 100 + np.cumsum(np.random.randn(200) * 0.5)
df = pd.DataFrame({'close': prices, 'volume': np.random.randint(100000, 500000, 200)}, index=dates)
df.index.name = 'date'

df['MA20'] = df['close'].rolling(20).mean()
df['returns'] = df['close'].pct_change()

print(df[['close', 'MA20', 'returns']].tail(10))
