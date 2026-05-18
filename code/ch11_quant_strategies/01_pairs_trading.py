# Copyright (c) 2025 TradeNote Authors
# Licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0).
# See LICENSE.txt for the full license text.

import numpy as np
import pandas as pd
from statsmodels.tsa.stattools import coint

np.random.seed(42)
n = 500
base = np.cumsum(np.random.randn(n) * 0.5) + 100
stock_a = pd.Series(base + np.random.randn(n) * 0.3, name='StockA')
stock_b = pd.Series(base * 0.8 + np.random.randn(n) * 0.2, name='StockB')

hedge_ratio = np.polyfit(stock_a, stock_b, 1)[0]

score, pvalue, _ = coint(stock_a, stock_b)
print(f"协整检验 p-value: {pvalue:.4f}")

if pvalue < 0.05:
    spread = stock_b - hedge_ratio * stock_a
    z_score = (spread - spread.mean()) / spread.std()
    print(f"当前 Z-Score: {z_score.iloc[-1]:.2f}")
    if z_score.iloc[-1] > 2:
        print("信号: 做空StockA + 做多StockB")
    elif z_score.iloc[-1] < -2:
        print("信号: 做多StockA + 做空StockB")
    else:
        print("信号: 无交易机会，等待价差偏离")
else:
    print("两股票不协整，不适合配对交易")
