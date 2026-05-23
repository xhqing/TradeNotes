# Copyright (c) 2026 TradeNotes Authors
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
